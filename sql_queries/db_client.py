import typing

import psycopg2
import config

class DB_client:
    def add_new_user(self,
             telegram_id: int,
             firstname: str,
             username: str,
             phone_number: str
        ) -> None:

        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO users (telegram_id, firstname, username, phone_number) VALUES ({telegram_id}, '{firstname}', '{username}', '{phone_number}')")
        conn.commit()
        cursor.close()
        conn.close()

    def select_client_cart(self, telegram_id: int) -> typing.Dict:
        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"SELECT cart FROM users WHERE telegram_id = {telegram_id}")
        cart_json = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return cart_json

    def change_in_cart(self, telegram_id: int, new_cart) -> None:
        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET cart = '{new_cart}' WHERE telegram_id = {telegram_id}")
        conn.commit()
        cursor.close()
        conn.close()

    def select_categories(self) -> typing.List[str]:
        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"SELECT category FROM products GROUP BY category")
        category = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return category

    def select_subcategories(self, product_category: str) -> typing.List[str]:
        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"SELECT subcategory FROM products WHERE category = '{product_category}' GROUP BY category, subcategory")
        category = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return category

    def select_products(self, subcategory: str) -> typing.List:
        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM products WHERE subcategory = '{subcategory}'")
        products = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return products

    def select_product(self, name_product: str) -> typing.Tuple:
        conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL,host=config.IP_MY_SERVER, port="5432")
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM products WHERE name = '{name_product}'")
        products = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return products

    def select_products_linked_to_pages(self, products: str, offset: int) -> typing.List:
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

