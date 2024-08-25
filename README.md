=====================================



 Available translations (English / German / Ukrainian)       ||| 11  - 110 |||  Pages
 Verfügbare Übersetzungen (Englisch / Deutsch / Ukrainisch)  ||| 110 - 211 |||  Seiten
 Доступні переклади (англійською / німецькою / українською)  ||| 211 - 309 |||  Cторінки



=====================================

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

=====================================



# Django Zitat-Webseite

Dies ist eine auf Django basierende Webanwendung zur Verwaltung und Anzeige von Zitaten. Benutzer können eine Liste von Zitaten einsehen, neue Zitate hinzufügen und Details zu Autoren anzeigen. Die Anwendung umfasst Funktionen zur Benutzerauthentifizierung für die Registrierung, Anmeldung und Abmeldung.

## Funktionen

- **Benutzerauthentifizierung**: Registrierung, Anmeldung und Abmeldung.
- **Zitaterverwaltung**: Anzeige einer paginierten Liste von Zitaten, Hinzufügen neuer Zitate.
- **Autorenverwaltung**: Anzeige von Details zu Autoren.
- **Paginierung**: Navigation durch Seiten von Zitaten.

## Voraussetzungen

- Python 3.8+
- Poetry (zur Verwaltung von Abhängigkeiten)

## Installation

1. **Repository klonen**:

    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Abhängigkeiten mit Poetry installieren**:

    ```bash
    poetry install
    ```

3. **Datenbank einrichten**:

    ```bash
    poetry run python manage.py migrate
    ```

4. **Superuser erstellen (optional, für Administratorzugang)**:

    ```bash
    poetry run python manage.py createsuperuser
    ```

5. **Entwicklungsserver starten**:

    ```bash
    poetry run python manage.py runserver
    ```

6. **Auf die Anwendung zugreifen**:

    Öffnen Sie Ihren Webbrowser und gehen Sie zu `http://127.0.0.1:8000`, um die Anwendung zu sehen.

## Konfiguration

- **Umgebungsvariablen**: Stellen Sie sicher, dass Sie die erforderlichen Umgebungsvariablen für Ihre Django-Einstellungen konfiguriert haben. Möglicherweise müssen Sie `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` und Datenbankeinstellungen in `settings.py` konfigurieren.

- **Statische Dateien**: Sammeln Sie statische Dateien für die Produktion mit:

    ```bash
    poetry run python manage.py collectstatic
    ```

## Nutzung

- **Registrieren**: Gehen Sie zu `/signup/`, um ein neues Benutzerkonto zu erstellen.
- **Anmelden**: Gehen Sie zu `/login/`, um sich in Ihr Konto einzuloggen.
- **Abmelden**: Verwenden Sie die Abmeldefunktion, die in der Navigation verfügbar ist.
- **Zitate hinzufügen**: Gehen Sie zu `/new_quote/`, um ein neues Zitat hinzuzufügen (Authentifizierung erforderlich).
- **Autoren hinzufügen**: Gehen Sie zu `/add_author/`, um einen neuen Autor hinzuzufügen (Authentifizierung erforderlich).
- **Zitate ansehen**: Gehen Sie zu `/quotes/`, um die Liste der Zitate anzuzeigen.
- **Autoren-Details ansehen**: Gehen Sie zu `/author/<author_id>/`, um Details zu einem bestimmten Autor anzuzeigen.

## Entwicklung

- **Tests ausführen**:

    ```bash
    poetry run python manage.py test
    ```

- **Code-Stil**: Befolgen Sie die PEP 8-Richtlinien für Python-Code. Verwenden Sie Linter und Formatter wie `flake8` und `black`.

## Mitwirkung

1. Forken Sie das Repository.
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/your-feature`).
3. Committen Sie Ihre Änderungen (`git commit -am 'Add some feature'`).
4. Pushen Sie zum Branch (`git push origin feature/your-feature`).
5. Erstellen Sie einen neuen Pull Request.


## Danksagungen

- **Django**: Das für dieses Projekt verwendete Web-Framework.
- **Poetry**: Das für die Verwaltung der Projektabhängigkeiten verwendete Tool.

=====================================

# Django Сайт Цитат

Це веб-додаток на основі Django для управління та відображення цитат. Користувачі можуть переглядати список цитат, додавати нові цитати та переглядати деталі про авторів. Додаток включає функції аутентифікації користувачів для реєстрації, входу та виходу.

## Функціонал

- **Аутентифікація користувачів**: Реєстрація, вхід та вихід.
- **Управління цитатами**: Перегляд списку цитат з пагінацією, додавання нових цитат.
- **Управління авторами**: Перегляд деталей про авторів.
- **Пагінація**: Переміщення між сторінками цитат.

## Передумови

- Python 3.8+
- Poetry (для управління залежностями)

## Встановлення

1. **Клонуйте репозиторій**:

    ```bash
    git clone https://github.com/yourusername/yourprojectname.git
    cd yourprojectname
    ```

2. **Встановіть залежності за допомогою Poetry**:

    ```bash
    poetry install
    ```

3. **Налаштуйте базу даних**:

    ```bash
    poetry run python manage.py migrate
    ```

4. **Створіть суперкористувача (необов'язково, для доступу до адмінки)**:

    ```bash
    poetry run python manage.py createsuperuser
    ```

5. **Запустіть сервер розробки**:

    ```bash
    poetry run python manage.py runserver
    ```

6. **Доступ до додатку**:

    Відкрийте веб-браузер і перейдіть на `http://127.0.0.1:8000`, щоб переглянути додаток.

## Налаштування

- **Змінні середовища**: Переконайтесь, що ви налаштували необхідні змінні середовища для вашого Django налаштування. Можливо, вам потрібно буде налаштувати `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` та налаштування бази даних у `settings.py`.

- **Статичні файли**: Зберіть статичні файли для продакшну за допомогою:

    ```bash
    poetry run python manage.py collectstatic
    ```

## Використання

- **Реєстрація**: Перейдіть на `/signup/`, щоб створити новий обліковий запис користувача.
- **Вхід**: Перейдіть на `/login/`, щоб увійти в обліковий запис.
- **Вихід**: Використовуйте функцію виходу, доступну в навігації.
- **Додавання цитат**: Перейдіть на `/new_quote/`, щоб додати нову цитату (необхідна аутентифікація).
- **Додавання авторів**: Перейдіть на `/add_author/`, щоб додати нового автора (необхідна аутентифікація).
- **Перегляд цитат**: Перейдіть на `/quotes/`, щоб переглянути список цитат.
- **Перегляд деталей автора**: Перейдіть на `/author/<author_id>/`, щоб переглянути деталі про конкретного автора.

## Розробка

- **Запустіть тести**:

    ```bash
    poetry run python manage.py test
    ```

- **Стиль коду**: Дотримуйтеся вказівок PEP 8 для коду Python. Використовуйте лінтери та форматери, такі як `flake8` та `black`.

## Участь

1. Створіть форк репозиторію.
2. Створіть гілку функціоналу (`git checkout -b feature/your-feature`).
3. Зробіть коміт ваших змін (`git commit -am 'Add some feature'`).
4. Запуште в гілку (`git push origin feature/your-feature`).
5. Створіть новий Pull Request.


## Подяки

- **Django**: Веб-фреймворк, використаний для цього проекту.
- **Poetry**: Інструмент управління залежностями, використаний для управління залежностями проекту.
