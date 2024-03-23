import config_gitignore
from sqlalchemy import Integer, String, Column, JSON, create_engine
from sqlalchemy.orm import DeclarativeBase


TOKEN = config_gitignore.TOKEN_GITIGNORE


URL_POSTGRESQL = config_gitignore.URL_POSTGRESQL_GITIGNORE


engine = create_engine(URL_POSTGRESQL)


class Base(DeclarativeBase):
    pass


class UsersDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(Integer, nullable=False)
    firstname = Column(String)
    username = Column(String)
    phone_number = Column(String)
    tag = Column(String, default="client")
    cart = Column(JSON)


class ProductsDB(Base):
    __tablename__ = "products"

    name = Column(String, nullable=False, primary_key=True, unique=True)
    description = Column(String)
    photo = Column(String)
    count = Column(Integer)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    subcategory = Column(String, nullable=False)
