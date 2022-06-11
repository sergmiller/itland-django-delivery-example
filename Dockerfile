FROM python:3.7

WORKDIR /usr/src/app

EXPOSE 8000:8000

RUN pip install --upgrade pip
RUN pip install django==3.1.5 django-extensions==3.1.5 numpy==1.19.4

COPY . .

CMD tail -f /dev/null
