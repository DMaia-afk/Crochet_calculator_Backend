# Crochet Calculator Backend

A Django REST API backend for calculating crochet piece prices. This application allows users to register, authenticate, and manage crochet project notes with automatic price calculations based on material costs, labor time, fixed expenses, and profit margins.

## Frontend

The frontend for this application is available at: [Crochet Calculator Frontend](https://github.com/DMaia-afk/Crochet_calculator)

## Features

- **User Authentication**: JWT-based authentication with registration and token refresh
- **Project Notes Management**: Create, list, and store crochet project notes
- **Automatic Price Calculation**: Calculates total selling price based on:
  - Material costs
  - Labor time (hours and minutes)
  - Hourly rates
  - Fixed expenses
  - Profit margins
- **RESTful API**: Built with Django REST Framework
- **CORS Support**: Configured for cross-origin requests
- **Production Ready**: Configured for deployment on Heroku

## Tech Stack

- **Backend**: Django 5.2.7
- **API Framework**: Django REST Framework 3.16.1
- **Authentication**: JWT (djangorestframework-simplejwt 5.5.1)
- **Database**: SQLite (default) or PostgreSQL via DATABASE_URL
- **CORS**: django-cors-headers 4.9.0
- **Deployment**: Gunicorn 23.0.0
- **Python Version**: 3.12.7

## Installation

### Prerequisites

- Python 3.12.7
- pip

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/DMaia-afk/Crochet_calculator_Backend.git
   cd Crochet_calculator_Backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Authentication

- `POST /api/token/`: Obtain JWT token pair (login)
- `POST /api/token/refresh/`: Refresh JWT token
- `POST /api/register/`: Register a new user

### Notes

- `GET /api/notes/`: List user's notes (authenticated)
- `POST /api/notes/`: Create a new note (authenticated)

### Calculation

- `POST /api/calculate/`: Calculate price without saving (public)

### Admin

- `/admin/`: Django admin interface

## Usage

### Authentication

1. Register a new user:
   ```bash
   curl -X POST http://localhost:8000/api/register/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}'
   ```

2. Obtain JWT token:
   ```bash
   curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "testuser", "password": "testpass"}'
   ```

### Creating a Note

```bash
curl -X POST http://localhost:8000/api/notes/ \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Baby Blanket",
    "material_cost": 25.00,
    "hours": 10,
    "minutes": 30,
    "hourly_rate": 15.00,
    "fixed_expenses": 5.00,
    "profit_margin": 20.00
  }'
```

### Price Calculation Logic

The selling price is calculated as:
```
total_hours = hours + (minutes / 60)
labor_cost = total_hours * hourly_rate
total_cost = material_cost + labor_cost + fixed_expenses
selling_price = total_cost / (1 - (profit_margin / 100))
```

If profit_margin >= 100%, selling_price = total_cost.

## Environment Variables

- `SECRET_KEY`: Django secret key (required in production)
- `DEBUG`: Set to 'True' for development
- `DATABASE_URL`: Database connection string (defaults to SQLite)
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Deployment

This project is configured for Heroku deployment:

1. Set environment variables in Heroku dashboard
2. Push to Heroku git
3. The Procfile specifies: `web: gunicorn Cc.wsgi --log-file -`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or support, please open an issue on GitHub.