FROM alpine:3.14

RUN apk update && apk upgrade --available
RUN apk add --no-cache --update python3 py3-pip ffmpeg

WORKDIR /home/app
COPY . /home/app
RUN python3 -m pip install -r requirements.txt --ignore-installed six

CMD ["python3", "main.py"]
