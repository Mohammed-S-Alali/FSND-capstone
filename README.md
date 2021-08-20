
#  Casting Agency

## Full Stack Nano - Capstone Project

Udacity has decided to open a new digitally enabled casting agency for students to search movies and actors. But they need help setting up agency experience.

You have been called on to demonstrate your newly learned skills to create a casting agency application. The application must:

1.  Allow only authouriazed user to use it.
2.  Allow casting assistant users to view actors and movies.
3.  Allow the casting director to add or delete an actor, modify actors or movies, and all permissions of casting assistant.
4.  Allow the executive producer to add or delete a movie and all permissions of casting director.

The link of heroku app (Capstone Project) [https://fsnd-capstone-msa.herokuapp.com/](https://fsnd-capstone-msa.herokuapp.com/)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `models.py`.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```
psql casting_agency < casting_agency.pgsql
```

## Tasks

### Setup Models
1. Create two main classes which are actors and movies
2. Define the suitable attributes for each class
3. Define required methods according to object-relation mapping (ORM) in SQLAlchemy like add, insert, delete and etc.
4. Connect classes to a SQLAlchemy instance.

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
   - in API Settings:
     - Enable RBAC
     - Enable Add Permissions in the Access Token
5. Create new API permissions:
   - `get:movies`
   - `get:actors`
   - `post:movies`
   - `post:actors`
   - `patch:movies`
   - `patch:actors`
   - `delete:movies`
   - `delete:actors`
6. Create new roles for:
   - Casting Assistant
		- can `get:movies`
		- can `get:actors`
   - Casting Director
		- can perform all actions of casting assistant
		- can `post:actors`
		- can `delete:actors`
		- can `patch:actors`
		- can `patch:movies`
	- Executive Producer
		- can perform all actions of casting director
		- can `post:movies`
		- can `delete:movies`
7. Test your endpoints (Public API not local) with [Postman](https://getpostman.com).
   - Register 3 users - assign the Casting Assistant role to one, Casting Director role to one and Executive Producer to the other.
   - Sign into each account and make note of the JWT.
   - Import the postman collection `udacity-fsnd-capstone.postman_collection.json`
   - Right-clicking the collection folder for casting assistant, casting director and executive producer, then navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
   - Run the collection and correct any errors.
   - Export the collection overwriting the one we've included so that we have your proper JWTs during review!


## Running the server

Firstly, ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically. Then, you can perform the testing.