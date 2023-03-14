FROM python:3

RUN apt update && apt upgrade -y && apt autoremove && apt autoclean

RUN mkdir /myproject
COPY . /myproject/
WORKDIR /myproject

RUN pip install --upgrade pip
RUN pip install django
RUN pip install django-widget-tweaks

ENTRYPOINT [ "python", "manage.py" ]
CMD [ "runserver", "0.0.0.0:8000" ]