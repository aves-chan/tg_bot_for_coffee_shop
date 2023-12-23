import psycopg2
import config


def db_add_new_user(telegram_id: int, firstname: str, username: str, phone_number: str):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (telegram_id, firstname, username, phone_number) VALUES ({telegram_id}, '{firstname}', '{username}', '{phone_number}')")
    conn.commit()
    cursor.close()
    conn.close()

def db_select_one_sandwich(callback_data):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = {callback_data}, type = 'Сэндвич' ")
    sandwiches = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

def db_select_one_breakfasts(callback_data):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = {callback_data}, type = 'Завтрак' ")
    breakfasts = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return breakfasts

def db_select_all_sandwich():
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE type = 'Сэндвич' ")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

def db_select_all_breakfasts():
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE type = 'Завтрак' ")
    breakfasts = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return breakfasts

def db_sandwich_withdrawal_for_keyboard():
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM products WHERE type = 'Сэндвич' ")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

def db_breakfasts_withdrawal_for_keyboard():
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM products WHERE type = 'Завтрак' ")
    breakfasts = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return breakfasts

