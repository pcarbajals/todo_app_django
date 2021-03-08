# README
## This Project

A simple To Do backend application implemented that allows to:
- Add new task
- Edit existing task
- List all tasks
- Delete a task

This is an attempt to reimplement [this Ruby on Rails](https://github.com/pcarbajals/todo_api_app) project on Django. Read the [Development notes](#development-notes) for details on what was accomplished.

## Installation
### Prerequisites

The development environment for this app uses `pipenv`, [a virtualenv for Python](https://github.com/pypa/pipenv). Therefore, to get you started you'll need to [install `pipenv`](https://pypi.org/project/pipenv/). 


### Running the server

From the project root, switch to the `api` directory:
```
$ cd api
```

Then activate a virtual environment:

```
$ pipenv shell
```

If this is the first time running the app:

1. Apply database migrations

```
$ ./manage.py migrate todo
```

2.  Create a "superuser" account to access the app admin interface

```
$ ./manage.py createsuperuser
```

Start the server:
```
$ ./manage.py runserver
```

### Accessing the admin interface
To access the app admin interface, go to:
```
http://127.0.0.1:8000/admin/
```
(or whatever URL the server log indicates when starting it) and use the credentials specificied when creating the "superuser" account.


## Browsing the API
The admin interface also offers a web browsable API for testing request submissions to the endpoints.

The API root is:
```
http://127.0.0.1:8000/api/v1/
```

Currently, the only functional endpoint is:
```
http://127.0.0.1:8000/api/v1/tasks
```


## Tests and coverage

To run the test cases, execute:
```
$ ./manage.py test
```

For coverage an inline report: 
```
$ coverage report
```

And for an HTML report:
```
$ coverage html
```


## Built With

* [Python 3.7.7](https://www.python.org/)
* [pip 21.0.1](https://pip.pypa.io/en/stable/)  - package installer for Python
* [pipenv 2020.11.15](https://pypi.org/project/pipenv/) - virtual environments for Python
* [Django](https://www.djangoproject.com/) - a Python web framework
* [Django REST Framework](https://www.django-rest-framework.org/) - a Django toolkit for building web APIs


## Development notes
This project is an attempt to reimplement [this Ruby on Rails (RoR) project](https://github.com/pcarbajals/todo_api_app) on Python + Django. Not all features, funtional and non-functional requirements were reimplemented. Notably, the follow is missing:

### Tags
The ability to tag tasks were not implemented.

### OpenAPI
This project doesn't comply with OpenAPI specification as the original RoR project does, therefore the serialization has to be modified accordingly.

### Versioning
Versioning hasn't been implemented, however to maintain compatibility with existing Postman tests, the URL `api/v1/` was maintained. 

### Postman tests
The existing RoR has a companion Postman collection for testing the APIs (included in the RoR project integration tests), however due to missing features described above, the Postman tests fail. Once the features have been implemented and the Postman tests pass, this project will be considered fully reimplemented.


