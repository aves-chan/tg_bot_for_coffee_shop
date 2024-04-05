FROM python:3.11

WORKDIR /tg_bot_for_coffee_shop

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

LABEL authors="aves-chan"