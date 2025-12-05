## Environment Setup
- `cd server`
- `pip install virtualenv`
- `virtualenv djangoenv`
- `source djangoenv/bin/activate`
- `python3 -m pip install -U -r requirements.txt`
- `python3 manage.py makemigrations`
- `python3 manage.py migrate`

## Run Server
- `python3 manage.py runserver`

## Frontend
- `cd server/frontend`
- `npm install`
- `npm run build`

## Docker
- `cd server/database`
- `docker build . -t nodeapp`
  - Run command if there are changes made to data/app.js
- `docker-compose up`
