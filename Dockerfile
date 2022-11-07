#ubuntu envarionment
FROM ubuntu:20.04 AS builder-image
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update

RUN apt-get install -y python3.10 python3-pip

RUN apt-get install --no-install-recommends -y ffmpeg build-essential
	
WORKDIR /bot
COPY requirements.txt /bot/
RUN python3 -m pip install --no-cache-dir -r requirements.txt
COPY . /bot
CMD python3 main.py
#it takes like 8min to deploy, sorry
