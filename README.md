# tg_bot_for_coffie


# ПЕРВАЯ НАСТРОЙКА

### ИСПОЛЬЗУЕМЫЕ ФРЕЙМВОРКИ
aiogram `pip install aiogram`\
aiohttp `pip install aiohttp`\
psycopg2(для работы с postgresql) `pip install psycopg2-binary`\
NGINX(веб-серврер) [официальный сайт nginx для установки](https://nginx.org/ru/download.html)

### ПЕРЕОПРЕДЕЛЕНИЕ ПЕРЕМЕННЫХ
Обязательно перед использованием нужно в модуле `config.py` определить переменные:

```
TOKEN = "токен телеграм бота"

PASSWORD_POSTGRESQL = "пароль от postgresql"

IP_MY_SERVER = "адрес postgresql(в моем случае ip)"
```

### СОЗДАНИЕ БАЗЫ ДАННЫХ ДЛЯ БОТА

Базой данных будет PostgrSQL. **Более подробной информации как создать бд напишу позже**