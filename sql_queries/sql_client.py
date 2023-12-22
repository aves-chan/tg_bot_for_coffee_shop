import psycopg2
import config


def db_add_new_user(telegram_id: int, firstname: str, username: str, phone_number: str):
    conn = psycopg2.connect(dbname="db_users", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (telegram_id, firstname, username, phone_number) VALUES ({telegram_id}, '{firstname}', '{username}', '{phone_number}')")
    conn.commit()
    cursor.close()
    conn.close()


def sandwich_withdrawal():
    conn = psycopg2.connect(dbname="products_menu", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sandwich")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches

def breakfasts_withdrawal():
    conn = psycopg2.connect(dbname="products_menu", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM breakfasts")
    breakfasts = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return breakfasts

def sandwich_withdrawal_for_keyboard():
    conn = psycopg2.connect(dbname="products_menu", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM sandwich")
    sandwiches = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return sandwiches


def breakfasts_withdrawal_for_keyboard():
    conn = psycopg2.connect(dbname="products_menu", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM breakfasts")
    breakfasts = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return breakfasts