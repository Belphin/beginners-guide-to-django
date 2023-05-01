# Development server

- ### Set environment variables

  - `cp .env.example .env`

- ### Build docker

  - `docker-compose build`

### Set up back-end

- ### Update the database schema

  - `docker-compose run server python manage.py makemigrations`

- ### Apply the migration

  - `docker-compose run server python manage.py migrate`

- ### Run docker

  - `docker-compose up`
