# Disability Assistance Mapping Project

A Django-based web application for mapping and assisting people with disabilities. This project helps to visualize the location of disabled persons and categorize them by disability type, making it easier for support organizations to provide targeted assistance.

## Features

- Interactive map showing the location of disabled persons
- Filtering by disability types
- RESTful API for data access and management
- User-friendly interface for adding new entries

## Technology Stack

- **Backend**: Django with Django REST Framework
- **Database**: PostgreSQL (in production), SQLite (in development)
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Configured for deployment with WhiteNoise for static files

## API Endpoints

- `/api/disabled-persons/` - List all persons or create a new one (GET, POST)
- `/api/disabled-persons/{id}/` - Retrieve, update, or delete a specific person (GET, PUT, PATCH, DELETE)
- `/api/disabled-persons/disability_types/` - Get all disability types
- `/` - Main map view

## Installation

1. Clone the repository:

   ```
   git clone <your-repository-url>
   cd project
   ```

2. Install requirements:

   ```
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```
   python manage.py migrate
   ```

4. Run the development server:
   ```
   python manage.py runserver
   ```

## Environment Variables

For production, the following environment variables can be set:

- `DEBUG` - Set to 'True' for development, 'False' for production
- `SECRET_KEY` - Django secret key
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Database connection string (for production)

## Deployment

This project is configured for deployment on platforms that support Django applications. The project uses WhiteNoise for serving static files in production.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
