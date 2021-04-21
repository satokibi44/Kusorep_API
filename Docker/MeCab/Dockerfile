FROM ubuntu:18.04

# basic libs
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y wget build-essential gcc zlib1g-dev

# latest openssl for python
WORKDIR /root/
RUN wget https://www.openssl.org/source/openssl-1.1.1d.tar.gz \
    && tar zxf openssl-1.1.1d.tar.gz \
    && cd openssl-1.1.1d \
    && ./config \
    && make \
    && make install

# python
WORKDIR /root/
RUN wget https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tgz \
    && tar zxf Python-3.9.0.tgz \
    && cd Python-3.9.0 \
    && ./configure \
    && make altinstall
ENV PYTHONIOENCODING "utf-8"

WORKDIR /usr/local/bin/
RUN ln -s python3.9 python
RUN ln -s pip3.9 pip
RUN pip install --upgrade pip

# mecab
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8

# python app settings
ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

WORKDIR /