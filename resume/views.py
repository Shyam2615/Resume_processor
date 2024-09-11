import re
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PyPDF2 import PdfReader
from docx import Document
from .models import Candidate
from .serializers import CandidateSerializer

class ExtractResumeView(APIView):
    def post(self, request):
        resume_file = request.FILES.get('resume')

        if resume_file.name.endswith('.pdf'):
            text = self.extract_text_from_pdf(resume_file)
        elif resume_file.name.endswith('.docx'):
            text = self.extract_text_from_docx(resume_file)
        else:
            return Response({"error": "Unsupported file format"}, status=status.HTTP_400_BAD_REQUEST)

        first_name = self.extract_first_name(text)
        email = self.extract_email(text)
        mobile_number = self.extract_mobile_number(text)

        candidate = Candidate.objects.create(first_name=first_name, email=email, mobile_number=mobile_number)
        candidate.save()
        serializer = CandidateSerializer(candidate)

        return Response(serializer.data)

    def extract_text_from_pdf(self, pdf_file):
        reader = PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text

    def extract_text_from_docx(self, docx_file):
        doc = Document(docx_file)
        text = '\n'.join([para.text for para in doc.paragraphs])
        return text

    def extract_first_name(self, text):
        match = re.search(r'\b[A-Z][a-z]+\b', text)
        return match.group(0) if match else 'Unknown'

    def extract_email(self, text):
        match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return match.group(0) if match else 'Unknown'

    def extract_mobile_number(self, text):
        match = re.search(r'\b\d{10}\b|\b\d{3}[-.\s]\d{3}[-.\s]\d{4}\b', text)
        return match.group(0) if match else 'Unknown'
