FROM ubuntu:latest
MAINTAINER ourstartlw "ourstartlw@gmail.com"
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev curl iputils-ping dnsutils git\
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
  && pip3 install -r requirements.txt

COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["main.py"]