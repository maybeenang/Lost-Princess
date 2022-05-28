FROM ubuntu:latest

COPY . ./home/app/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-pygame \
    x11-apps \
    pulseaudio 

WORKDIR /home/app/

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]