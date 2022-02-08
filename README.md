# Network file exercise
This is project to realize task from some company. I get network file and I had to present his data by frontend technology.

## Tools

- django (pip install django)
- django restframework (pip install djangorestframework)
- re2 (pip install pyre2)

## Run

1. Clone repository
2. Run `generateDataFiles.py` in `backend/network_backend` directory (`python generateDataFiles.py`)
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py runserver` and wait for data to apply
6. Exit and create superuser by `python manage.py createsuperuser`
7. `python manage.py runserver` and browse models in `localhost:8000/admin`
