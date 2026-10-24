# CubeHub

## Description

CubeHub is a Django web application for cubing enthusiasts. It allows users to manage cubers, cubes, and solve records through a web interface.

## Technologies

- Python
- Django 6.1.1
- SQLite
- HTML and CSS

## Project Structure

The project contains three Django applications:

- **cubers** — manages cuber profiles.
- **cubes** — manages cubes and their owners.
- **solves** — manages solve records, including the cuber, cube, time, and scramble.

## Requirements

- Python compatible with Django 6.1.1
- pip

## Installation and Setup

1. Clone or download the project.
2. Open a terminal in the project root directory, where `manage.py` is located.
3. Create and activate a virtual environment.

   Windows PowerShell:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

4. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. Apply database migrations:

   ```powershell
   python manage.py migrate
   ```

6. Start the development server:

   ```powershell
   python manage.py runserver
   ```

7. Open the local address shown in the terminal, usually http://127.0.0.1:8000/.

## Database

The project uses SQLite. The database is created when migrations are applied. The application should work with an empty database, and users can create records through the website.

## Environment Variables and Security

Document any environment variables required to configure the project here, including the Django secret key and debug setting if the project reads them from the environment.

Do not publish real secret keys, passwords, or other credentials in the repository.

## Usage

Use the website navigation to access the cubers, cubes, and solves sections. Available actions depend on the features implemented in the application.

## License

This project was created for educational purposes.