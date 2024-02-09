# Fapbot  
Телеграм бот, который развлекается с твими фотографиями.   
  
Отлажено на Python 3.9.1   
Используется библиотека Aiogram 2.23.1  
  
  
Telegram bot in Python that will enjoy your photos.  
  
Debugged on Python 3.9.1  
The library used is Aiogram 2.23.1  
  
  
<<<<<<< HEAD
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

=======
Докерфайл опирается на специально настроеный мной образ metro3230/telebots_basis 

Введение в эксплуатацию:
1. Клонируем папку к себе на машину
 (например 'gh repo clone Metro3230/fapbot')
2. Правим айди чата и токен телеги в config.py
3. Билдим образ:
docker build --tag fapbot .
4. правильный запуск контейнера:  
docker run --restart always -d --name fapbot fapbot  
>>>>>>> 141179902221be521275e95c77680a7723ce090d
