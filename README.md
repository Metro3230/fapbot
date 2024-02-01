# fapbot
Телеграм бот, который развлекается с твими фотографиями. 

Отлажено на Python 3.9.1 
Используется библиотека Aiogram 2.23.1


Telegram bot in Python that will enjoy your photos.

Debugged on Python 3.9.1
The library used is Aiogram 2.23.1


Докерфайл опирается на специально настроеный мной образ metro3230/telebots_basis  (о нём в конце)

Более менее декватный запуск контейнера:
docker run --restart always -d --name fap_bot metro3230/fapbot

??? чего это он не пишет мне паралельно в личку? 
??? разобраться, как адекватно логировать вне образа например 
??? разобраься в докер компос?





++++++++++++++++++++++++++
сделал образ metro3230/telebots_basis на debian:bookworm-20231218
на него встал питон Python 3.11.7
и pip 23.3 from /usr/lib/python3/dist-packages/pip (python 3.11)
    так же пакеты пайтон:
     aiogram==2.23.1
     pillow==10.2.0
     apscheduler==3.10.4
     datetime==5.4
     wget==3.2
(Cтавились командой "pip3 install --break-system-packages *ИМЯ ПАКЕТА*" без вопросов)