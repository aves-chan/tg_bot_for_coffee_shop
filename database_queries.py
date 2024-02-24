import typing

from sqlalchemy import Engine
from sqlalchemy.orm import Session

from config import engine, Users_db, Products_db


class DB_queries:
    def __init__(self, engine: Engine, autoflush: bool = False):
        self.__engine = engine
        self.__autoflush = autoflush

    def check_user(self, telegram_id: int) -> typing.Union[Users_db, None]:
        with Session(bind=self.__engine, autoflush=self.__autoflush) as db:
            user = db.query(Users_db).filter(Users_db.telegram_id == telegram_id).first()
            return user

    def set_new_user(self,
                     telegram_id: int,
                     firstname: str,
                     username: str,
                     phone_number: str
                     ) -> None:
        with Session(bind=self.__engine, autoflush=self.__autoflush) as db:
            user = Users_db(telegram_id=telegram_id,
                            firstname=firstname,
                            username=username,
                            phone_number=phone_number)
            db.add(user)
            db.commit()

    def get_profile(self, telegram_id: int) -> typing.Union[Users_db, None]:
        with Session(bind=self.__engine, autoflush=self.__autoflush) as db:
            user = db.query(Users_db).filter(Users_db.telegram_id == telegram_id).first()
            return user

    def get_categories(self) -> typing.List:
        with Session(bind=self.__engine, autoflush=self.__autoflush) as db:
            categories = db.query(Products_db.category).all()
            return categories


db_queries = DB_queries(engine=engine)


