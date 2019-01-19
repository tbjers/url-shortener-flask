# URL Shortener application

An application powered by Flask and PostgreSQL.

## Installation

In order to install depencencies run:

```sh
pip install -r requirements.txt
```

### Install profanity-filter database

URL Shortener uses the profanity-filter package to ensure that generated URL hashes do not contain profane words.

Install the English dictionary:

```sh
python -m spacy download en
```

## Set up env configuration

Create a file called `.env` in the project root.

```ini
FLASK_APP=urlshortener
FLASK_ENV=development
FLASK_SECRET_KEY=<SUPER_SECRET_KEY>
SQLALCHEMY_DATABASE_URI=postgresql://urlshortener_app:<RANDOM_PASSWORD>@localhost/urlshortener
SQLALCHEMY_TRACK_MODIFICATIONS=True
```

## Database configuration

The URL Shortener service uses PostgreSQL as a database backend.

### Prepare the database

Prepare the database for usage:

```sql
CREATE DATABASE urlshortener;
CREATE USER urlshortener_app WITH NOCREATEDB PASSWORD '<RANDOM_PASSWORD>';
GRANT ALL PRIVILEGES ON urlshortener TO urlshortener_app;
```

### Initialize database

In order to initialize the database run:

```sh
flask init-db
```

## Run the application

Running the application locally is as easy as:

```sh
flask run
```

## Testing the application

This command starts the test suites:

```sh
pytest
```

### Coverage output

HTML Coverage can be found in the `htmlcov` directory.

## Remaining out-of-scope exercises

This application serves as an example of how one would create a URL Shortener application in Flask. Missing are a few vital features such as:

* Authentication for admins
* Store URLs for the current user by setting a cookie
* Caching with Redis
* Dockerize cluster with PostgreSQL, Redis and WSGI server
* Log users in with social logins such as Google or Facebook
* Support user/password authentication
* Make backend entirely API/JSON
* Convert frontend to React
* Generate frontend via asset pipeline
* Create deployment scripts
* Support analytics tracking via external services such as Google Analytics
* Mobile device support for App/Play Store links
* Analytics dashboard for users
* Roll up statistics by year, month and day
