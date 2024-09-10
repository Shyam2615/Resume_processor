Installation
Clone the Repository

git clone <repository-url>
cd ResumeProcessor

Set Up Virtual Environment

python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Configure Database

Update the DATABASES section in ResumeProcessor/settings.py to match your PostgreSQL setup:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Apply Migrations

python manage.py makemigrations
python manage.py migrate

Usage
Run the Development Server

python manage.py runserver

Access the API Endpoint

Send a POST request to /api/extract_resume/ with a resume file attached. The API accepts PDF and DOCX formats.

Example using curl:

curl -X POST -F 'resume=@path_to_resume.pdf' http://127.0.0.1:8000/api/extract_resume/
The response will be in JSON format:

{
    "first_name": "John",
    "email": "john.doe@example.com",
    "mobile_number": "123-456-7890"
}
