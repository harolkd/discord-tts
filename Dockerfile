FROM alpine:3.17

WORKDIR /home/app

RUN apk add --no-cache --update python3 py3-pip ffmpeg
COPY requirements.txt /home/app
RUN python3 -m pip install -r requirements.txt --ignore-installed six

COPY . /home/app

CMD ["python3", "main.py"]
