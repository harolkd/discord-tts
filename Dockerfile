#ubuntu envarionment
FROM alpine:3.14

RUN apk add --no-cache python3.10 python3-pip ffmpeg

COPY . /home/app
WORKDIR /home/app
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py"]
#it takes like 8min to deploy, sorry
