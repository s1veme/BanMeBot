# BanMeBot

Создаём и активируем виртаульное окружение:

```
virtualenv venv
source venv/Script/activate
```

Устанавливаем нужные библиотеки:

```
pip install -r requirements.txt
```

Создаём файл `.env` в корне, где указываем переменные `ADMINS`, `BOT_TOKEN`.

```
ADMINS=id1,id2,id3
BOT_TOKEN=Ваш токен
```

Запускаем `app.py`.

```
python app.py
```
