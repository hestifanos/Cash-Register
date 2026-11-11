# Cash Register

A Django application for looking up products by their 12-digit UPC code and displaying the product name and price.

## Features

- Search products by unique UPC code.
- Show product details after a successful lookup.
- Validate UPC input and display a clear message when the code is invalid or unknown.
- Manage products through Django's admin site.
- Seed a small example catalog with an idempotent script.

## Requirements

- Python 3.10 or newer
- pip

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python populate_db.py
python manage.py runserver
```

Open [http://127.0.0.1:8000/sales/cash_register/](http://127.0.0.1:8000/sales/cash_register/).

For deployment, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` in the environment. The development server is not intended for production.

## Tests

```bash
python manage.py test
```

## Project structure

```text
cashregister/       Django project configuration
sales/              Product model, lookup view, templates, and tests
populate_db.py      Idempotent example-product seeder
requirements.txt    Python dependencies
```
