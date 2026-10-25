## Installation


# CubeHub

CubeHub is a Django web application for managing speedcubers,
Rubik's cubes, and solving records. It allows users to create and
manage cuber profiles, maintain a cube collection, and record
solving times.

## Features

- Create, view, edit, and delete cuber profiles.
- Manage cubes and their owners.
- Record and browse solve history.
- Filter and sort available records.
- Validate form submissions and display error messages.
- Use a custom 404 page and a consistent navigation layout.

## Project structure

The project consists of three Django apps:

- `cubers` — manages cuber profiles.
- `cubes` — manages cubes and their owners.
- `solves` — manages solving records and time formatting.

The `cubehub` package contains the main Django settings,
URL configuration, and project-level views.

## Database relationships

- A solve references one cuber through a foreign key.
- A solve references one cube through a foreign key.
- Cubers and cubes have a many-to-many ownership relationship.

The application uses SQLite and can be initialized by applying
the migrations. Required objects can be created through the
application interface without using Django admin.


### Prerequisites
- Python 3.12 or another Python version supported by the project's dependencies
- Git

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/B0zhidar-GH/CubeHub.git
   cd CubeHub
   ```

2. Create a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

### Notes
- Run the management commands from the directory containing `manage.py`.
- The application uses Django's configured database. Migrations create the database schema; they do not necessarily populate it with sample data.
