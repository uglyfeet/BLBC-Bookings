# Deployment

## Local Setup

1. Install Python 3.12.
2. Clone the `BLBC-Bookings` repository from GitHub.
3. Open the project folder in Visual Studio Code.
4. Create and activate a virtual environment:

```text
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

5. Install the required dependencies:

```text
pip install -r requirements.txt
```

6. Configure the required environment variables:

- `SECRET_KEY`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`
- `DATABASE_URL`

Values for these variables must not be stored in the GitHub repository.

7. Run the database migrations:

```text
python manage.py migrate
```

8. Start the development server:

```text
python manage.py runserver
```

9. Open the local application in a web browser and test the main booking features.

## Cloud Deployment

The application is deployed to Heroku.

The production environment uses:

- Heroku for hosting
- PostgreSQL for the production database
- Cloudinary for room image storage
- Gunicorn as the web server
- WhiteNoise for static files

The same environment variables listed above must be configured in the Heroku application settings.

The Heroku deployment uses the project's `Procfile` to run database migrations and start Gunicorn.

After deployment, the live application should be tested to confirm that the main booking features, email verification, room images and administration functions work correctly.