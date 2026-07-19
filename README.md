# Event Management System

A Django-based web application for managing events, categories, and participants with user authentication.

## Features
- User signup/login/logout with custom user model
- Event CRUD (Create, Read, Update, Delete)
- Category and Participant management
- RSVP system for events
- Dashboard with statistics
- Image upload for events and profiles
- Tailwind CSS styling

## Setup

1. Clone the repo
2. Create virtual environment: `python -m venv event_env`
3. Activate it: `event_env\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Install Tailwind: `npm install -D tailwindcss@3`
6. Build CSS: `npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch`
7. Run migrations: `python manage.py migrate`
8. Create superuser: `python manage.py createsuperuser`
9. Run server: `python manage.py runserver`