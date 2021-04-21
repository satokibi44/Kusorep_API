FROM python:3.7.9

# basic libs
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y wget build-essential gcc zlib1g-dev git

ENV PYTHONIOENCODING "utf-8"

WORKDIR /usr/local/bin/
# mecab
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /usr/local/bin/mecab-ipadic-neologd/
RUN apt-get install -y wget curl file sudo
RUN ./bin/install-mecab-ipadic-neologd -n -u -y --prefix $HOME/local/lib/mecab/dic/mecab-ipadic-neologd

# python app settings
WORKDIR /usr/local/bin/
COPY ./Kusorep_API/Docker/MeCab/requirements.txt ./requirements.txt
RUN yes | pip install -r requirements.txt
RUN pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install sentencepiece==0.1.95
RUN pip install transformers==2.9.0
RUN pip install ipadic

WORKDIR /
COPY ./Kusorep_API ./Kusorep_API

WORKDIR /Kusorep_API