# Frobshop

Digital product e-commerce site built with Django Oscar

## Requirements

* Python (3.6.2)

* Django (1.11)

## Installation

Clone this repo

` git clone https://github.com/kristinburg/oscar-frobshop.git `

Install Python packages

` pip install -r requirements.txt `

## Configuration

Run migrations

` python manage.py migrate `

Create admin

` python manage.py createsuperuser `

Add country data (for shipping) from pycountry

` python manage.py oscar_populate_countries `
