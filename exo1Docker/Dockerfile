FROM ubuntu:bionic
RUN apt-get update && apt-get install -y git python3
WORKDIR app
COPY hello.py .
CMD python3 hello.py