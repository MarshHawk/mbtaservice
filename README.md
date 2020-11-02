## Run
- add API_KEY to docker-compose.yml, e.g.: API_KEY=77abf4eeb66f4b81b3f4dc73e2daaaaa
- docker-compose up

## Installation (steps taken)
```
conda create -n mbta-env python=3
conda activate mbta-env
pip install django
pip install graphene-django
pip install requests
pip install django-cors-headers
pip install python-dotenv
```

## ToDo
- env package for api key
- service class
- unit tests