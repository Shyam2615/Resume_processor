# ResumeProcessor

## Overview

**ResumeProcessor** is a Django project designed to process resumes and extract candidate information such as first name, email ID, and mobile number. It provides a REST API endpoint that accepts resume files in PDF or Word format and returns the extracted data.

## Project Structure

- `ResumeProcessor/`
  - `ResumeProcessor/` (Django project folder)
    - `__init__.py`
    - `settings.py`
    - `urls.py`
    - `wsgi.py`
  - `resume/` (Django app folder)
    - `migrations/` (Migration files)
    - `__init__.py`
    - `admin.py`
    - `apps.py`
    - `models.py` (Defines the `Candidate` model)
    - `serializers.py` (Serializes the `Candidate` model)
    - `urls.py` (URL routing for the `resume` app)
    - `views.py` (Handles resume extraction)
  - `manage.py` (Django management script)

## Prerequisites

- Python 3.9 or higher
- PostgreSQL (for database)
- Virtual environment (recommended)

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd ResumeProcessor
