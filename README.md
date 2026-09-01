# Weather App

A small Django application that turns live OpenWeather data into a responsive, weather-aware interface.

## What it demonstrates

- Python and Django request handling
- Third-party REST API integration
- Secure configuration through environment variables
- Resilient network and invalid-city error handling
- Responsive, accessible UI
- Automated view tests with mocked API responses

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` values into your environment and add an OpenWeather API key.
4. Start the application:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000`.

## Tests

```bash
python manage.py test
```

## Security

Secrets are read from environment variables and are never meant to be committed. The project uses SQLite for local development.
