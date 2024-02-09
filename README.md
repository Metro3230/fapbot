# Fapbot  
Телеграм бот, который развлекается с твими фотографиями.   
  
Отлажено на Python 3.9.1   
Используется библиотека Aiogram 2.23.1  
  
  
Telegram bot in Python that will enjoy your photos.  
  
Debugged on Python 3.9.1  
The library used is Aiogram 2.23.1  
  
  
---
Вариант развёртывания у себя на машине в контейнере Docker:

1. Клонируем папку к себе на машину, например:
```
gh repo clone Metro3230/fapbot
```
2. Билдим образ (специально созданный и настроенный под этот бот):
```
docker build --tag fapbot .
```
3. Вариант запуска контейнера:  
```
docker run --restart always -d --name fapbot fapbot  
```

