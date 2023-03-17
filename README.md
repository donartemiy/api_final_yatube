# api_final

API_FINAL_YATUBE is final project of yatube on django rest_framework.
It shows main ability rest_framework which we have used in class of Yandex Practicum.
##  Main functions:
- posts
- groups
- comments
- subsribe

## Installation
Download and create envirement.
```bash
git clone git@github.com:donartemiy/api_final_yatube.git
cd api_final_yatube
python -m venv venv
source venv/Scripts/activate
pip install -r requirements
```

## Start a progect

```bash
cd yatube_api
python3 manage.py migrate
python manage.py runserver
```

## Usage
Example of request
```bash
# Enpoints:
curl http://127.0.0.1:8000/api/v1/posts/
curl http://127.0.0.1:8000/api/v1/groups/
curl http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
curl http://127.0.0.1:8000/api/v1/follow/

# Get JWT-token
curl X POST http://127.0.0.1:8000/api/v1/jwt/create/
   -H "Accept: application/json"
   -H "Authorization: Bearer <ACCESS_TOKEN>"
   -d '{"username": "string", "password": "string"}'
   
# Post requests
curl X POST http://127.0.0.1:8000/api/v1/posts/
   -H "Accept: application/json"
   -H "Authorization: Bearer <ACCESS_TOKEN>"
   -d '{"test": string"", "group": 0}'
```
Project has API documentation redoc. It be able on the page [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)