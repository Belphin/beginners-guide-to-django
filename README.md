# Development server

- ### Set environment variables

  - `cp .env.example .env`

- ### Build docker

  - `docker compose build`

### Set up back-end

- ### Update the database schema

  - `docker compose run server python manage.py makemigrations`

- ### Apply the migration

  - `docker compose run server python manage.py migrate`

- ### Create superuser

  - `docker compose run server python manage.py createsuperuser`

- ### Django shell

  - `docker compose run server python manage.py shell`

- ### Run docker

  - `docker compose up`

- ### Run tests

  - `docker compose run server python manage.py test`
