# itland-django-delivery-example
Educational example of Django python project

# Delivery

### Установка и запуск локально через pip

(сначала нужно установить python3.7 и pip для него)

```sh
python3.7 -m pip install django==3.1.5 django-extensions==3.1.5 numpy==1.19.4
cd delivery
python3.7 manage.py migrate
python3.7 manage.py initialize
python3.7 manage.py runserver 0.0.0.0:8000
```

### Установка и запуск внутри docker контейнера

(сначала нужно установить docker)

```sh
docker build -t delivery-service -f Dockerfile .
docker run --rm -v $(pwd):/opt -it -p 8000:8000 --entrypoint bash delivery-service
#FYI: Дальнейшие команды выполняются уже в терминале который внутри контейнера с сервисом
cd delivery
python3.7 manage.py migrate
python3.7 manage.py initialize
python3.7 manage.py runserver 0.0.0.0:8000
```


Сервис будет запущен по адресу http://127.0.0.1:8000/
