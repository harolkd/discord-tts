#ubuntu envarionment
FROM alpine:3.14

RUN apk add --no-cache python3 py3-pip py3-pynacl py3-aiohttp ffmpeg build-base

COPY . /home/app
WORKDIR /home/app
#RUN python3 -m pip install --upgrade setuptools wheel
RUN python3 -m pip install -r requirements.txt --ignore-installed six

CMD ["python3", "main.py"]
#it takes like 8min to deploy, sorry
