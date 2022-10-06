FROM ubuntu:22.04

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN apt update

RUN apt install python3-pip -y

RUN apt install ffmpeg -y

RUN pip3 install -r requirements.txt

#CMD streamlit run app.py
CMD streamlit run --server.port $PORT app.py