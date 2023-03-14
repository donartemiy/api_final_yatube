# api_final

API_FINAL_YATUBE is final project of yatube on django rest_framework.
It shows main ability rest_framework which we have used in class of Yandex Practicum.
##  Main functions:
- posts
- comments
- subsribe

## Installation

Download and create envirement.
```bash
git clone git@github.com:donartemiy/api_final_yatube.git
cd api_final_yatube
python -m venv venv
source env/bin/activate
pip install -r requirements
```

## Usage
```bash
cd yatube_api
python3 manage.py migrate
python manage.py runserver
```
Project has API documentation redoc. It be able on the page [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)