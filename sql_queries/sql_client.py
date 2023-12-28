import psycopg2
import config


def db_add_new_user(telegram_id: int, firstname: str, username: str, phone_number: str):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (telegram_id, firstname, username, phone_number) VALUES ({telegram_id}, '{firstname}', '{username}', '{phone_number}')")
    conn.commit()
    cursor.close()
    conn.close()

def db_select_one_product(callback_data):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE id = {callback_data}")
    meal = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return meal

def db_select_all_products(products):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM products WHERE type = '{products}'")
    products = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return products

def db_select_products_for_generate_keyboard(products, offset):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    if offset == 0:
        cursor.execute(f"SELECT * FROM products WHERE type = '{products}' LIMIT 6")
    else:
        cursor.execute(f"SELECT * FROM products WHERE type = '{products}' LIMIT 6 OFFSET {offset}")
    products = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return products


def db_meal_withdrawal_for_keyboard(breakfasts_or_sandwich):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT id, name FROM products WHERE type = '{breakfasts_or_sandwich}'")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

