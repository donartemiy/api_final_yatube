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

## Start a project

```bash
cd yatube_api
python3 manage.py migrate
python manage.py runserver
```

## Usage
### Posts
Request:
```bash
curl http://127.0.0.1:8000/api/v1/posts/
```
Response:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

### Other enpoints
Requests:
```bash
curl http://127.0.0.1:8000/api/v1/groups/
curl http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
curl http://127.0.0.1:8000/api/v1/follow/
```

### Get JWT-token
Request:
```bash
curl X POST http://127.0.0.1:8000/api/v1/jwt/create/
   -H "Accept: application/json"
   -H "Authorization: Bearer <ACCESS_TOKEN>"
   -d '{"username": "string", "password": "string"}'
```
Resonse:
```json
{
  "username": "string",
  "password": "string"
}
```
   
   
### Add post
Request:
```bash
curl X POST http://127.0.0.1:8000/api/v1/posts/
   -H "Accept: application/json"
   -H "Authorization: Bearer <ACCESS_TOKEN>"
   -d '{"test": string"", "image": "string","group": 0}'
```
Resonse:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

Project has API documentation redoc. It be able on the page [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)