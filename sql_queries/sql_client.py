import psycopg2
import config


def db_add_new_user(telegram_id: int, firstname: str, username: str, phone_number: str):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (telegram_id, firstname, username, phone_number) VALUES ({telegram_id}, '{firstname}', '{username}', '{phone_number}')")
    conn.commit()
    cursor.close()
    conn.close()

def db_select_one_drink(callback_data):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = '{callback_data}")
    drink = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return drink

def db_select_one_meal(callback_data):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = '{callback_data}")
    breakfasts = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return breakfasts

def db_select_all_drinks(coffee_or_tea):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE type = '{coffee_or_tea}'")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

def db_select_all_meal(breakfasts_or_sandwich):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE type = '{breakfasts_or_sandwich}'")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches


def db_meal_withdrawal_for_keyboard(breakfasts_or_sandwich):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, name FROM products WHERE type = '{breakfasts_or_sandwich}'")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

