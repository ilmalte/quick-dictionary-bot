#FROM --platform=linux/amd64 python:3
FROM python:3

LABEL maintaner="Krotov Artem <timmson666@mail.ru>"

WORKDIR /app

COPY ./src/ ./

RUN pip3 install -r requirements.txt

CMD ["python3","bot.py"]
