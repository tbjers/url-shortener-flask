# URL Shortener application

An application powered by Flask and PostgreSQL.

## Installation

In order to install depencencies run:

```sh
pip install -r requirements.txt
```

### Install profanity-filter database

```sh
python -m spacy download en
```

## Set up env configuration

Create a file called `.env` in the project root.

```ini
FLASK_APP=urlshortener
FLASK_ENV=development
SQLALCHEMY_DATABASE_URI=postgresql://bugout_app:<RANDOM_PASSWORD>@localhost/urlshortener
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
python -m unittest
```
