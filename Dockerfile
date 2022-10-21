FROM python:3.10.8-alpine3.16
WORKDIR /bot
RUN apk add --no-cache ffmpeg musl-dev linux-headers python3-dev
COPY requirements.txt /bot/
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /bot
COPY . .
CMD python main.py
RUN apk add --no-cache ffmpeg