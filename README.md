# Django Quotes Site

This is a Django-based web application for managing and displaying quotes. Users can view a list of quotes, add new quotes, and view details about authors. The application includes user authentication features for signing up, logging in, and logging out.

## Features

- **User Authentication**: Sign up, log in, and log out.
- **Quotes Management**: View a paginated list of quotes, add new quotes.
- **Author Management**: View details about authors.
- **Pagination**: Navigate through pages of quotes.

## Prerequisites

- Python 3.8+
- Poetry (for dependency management)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Install dependencies using Poetry**:

    ```bash
    poetry install
    ```

3. **Set up the database**:

    ```bash
    poetry run python manage.py migrate
    ```

4. **Create a superuser (optional, for admin access)**:

    ```bash
    poetry run python manage.py createsuperuser
    ```

5. **Run the development server**:

    ```bash
    poetry run python manage.py runserver
    ```

6. **Access the application**:

    Open your web browser and go to `http://127.0.0.1:8000` to view the application.

## Configuration

- **Environment Variables**: Ensure that you have the necessary environment variables set up for your Django settings. You may need to configure `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and database settings in your `settings.py`.

- **Static Files**: Collect static files for production using:

    ```bash
    poetry run python manage.py collectstatic
    ```

## Usage

- **Sign Up**: Navigate to `/signup/` to create a new user account.
- **Log In**: Navigate to `/login/` to log into your account.
- **Log Out**: Use the logout functionality available in the navigation.
- **Add Quotes**: Navigate to `/new_quote/` to add a new quote (requires authentication).
- **Add Authors**: Navigate to `/add_author/` to add a new author (requires authentication).
- **View Quotes**: Navigate to `/quotes/` to see a list of quotes.
- **View Author Details**: Navigate to `/author/<author_id>/` to see details about a specific author.

## Development

- **Run Tests**:

    ```bash
    poetry run python manage.py test
    ```

- **Code Style**: Follow PEP 8 guidelines for Python code. Use linters and formatters like `flake8` and `black`.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.


## Acknowledgments

- **Django**: The web framework used for this project.
- **Poetry**: Dependency management tool used for managing project dependencies.
