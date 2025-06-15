# Superheroes API Project
A RESTful API built with Flask that allows you to manage superheroes, their powers, and the relationships between them.

## Description
This project is a simple backend system that models a superhero universe. Users can view a list of heroes and powers, associate heroes with powers (with a strength level), and update information via standard RESTful routes. It includes custom validation logic to ensure data consistency

## Owner
Sammy Dennis
Software Engineer & Backend Developer

## Features
- View all superheroes and their powers

- Assign powers to heroes with strength ratings (Strong, Average, Weak)

- Update power descriptions with validations

- Validation errors return structured JSON

- RESTful route naming conventions

- SQLAlchemy ORM integration

- Flask app context and environment setup

## Setup Instructions
Prerequisites
- 3.8.10
- pip (Python package installer)
- Virtualenv (recommended)

## Installation
```bash
    # Clone the repository
    git clone https://github.com/dennissammy77/superheroes.git
    cd superheroes

    # Set up virtual environment
    pipenv install
    pipenv shell

    cd server

    # Migrate Db
    flask db init
    flask db migrate -m "inital migration"
    flask db upgrade head

    # To seed data()
    python seed.py

    # Run the server
    flask run
```

## Running Tests
```bash
    pytest
```

## API Endpoints
| Method | Endpoint       | Description                   |
| ------ | -------------- | ----------------------------- |
| GET    | `/heroes`      | Get all heroes                |
| GET    | `/heroes/<id>` | Get a specific hero           |
| GET    | `/powers`      | Get all powers                |
| GET    | `/powers/<id>` | Get a specific power          |
| PATCH  | `/powers/<id>` | Update a power's description  |
| POST   | `/hero_powers` | Associate a hero with a power |


## Support
If you encounter any issues, feel free to contact me at:
`dennissammy77@gmail.com`