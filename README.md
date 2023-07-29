# Lunch Decision API

This project is a Django application that provides an API for making decisions about lunch in a restaurant. The system allows you to add restaurants, menus, and employees, as well as vote for menus.

## Tech Stack

The Lunch Decision API is built using the following technologies:

- Django
- Django Rest Framework (DRF)
- JSON Web Token (JWT) for authentication
- PostgreSQL
- Flake8 for linting and code style checks

## Getting Started

To run the Lunch Decision API, follow these steps:

1. Clone the repository

2. Install the project dependencies using pip install -r requirements.txt.

3. Create the database and perform migrations with python manage.py migrate.

4. Create a superuser (admin) to manage the API with python manage.py createsuperuser.

5. Start the development server using python manage.py runserver.\
The API should now be accessible at http://127.0.0.1:8000/.

## Authentication

The Lunch Decision API uses JWT for authentication. To get an access token, first create a user (either a superuser or regular user) using the Django shell. Then, make a POST request to http://127.0.0.1:8000/api/token/ with the user's credentials to obtain the access token. The token should be included in the request headers as Authorization: Bearer <your_token> for subsequent API requests.

## Endpoints

The following endpoints are available in the Lunch Decision API:
- POST /api/restaurants/: Create a new restaurant with a name.
- POST /api/menus/: Create a new menu for a restaurant with date, appetizer, main_course, and dessert.
- POST /api/employees/: Create a new employee with a name and email.
- GET /api/menus/?date=<year-month-day>&restaurant=<restaurant_id>: Get menus for a specific date and restaurant.
- GET /api/menus/?date=<year-month-day>: Get menus for a specific date across all restaurants.
- POST /api/votes/: Vote for a menu by providing the menu_id in the request data.

## API Versioning
The Lunch Decision API includes a custom middleware (middleware.py) that adds a response header, Lunch-Decision-API-Version, indicating the version of the API being used.