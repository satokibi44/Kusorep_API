FROM python:3.7.9

# basic libs
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y wget build-essential gcc zlib1g-dev git vim curl file sudo

ENV PYTHONIOENCODING "utf-8"

WORKDIR /usr/local/bin/
# mecab
RUN apt-get install -y mecab libmecab-dev mecab-ipadic mecab-ipadic-utf8
# mecab-ioadic-neologd
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
WORKDIR /usr/local/bin/mecab-ipadic-neologd/
RUN ./bin/install-mecab-ipadic-neologd -n -u -y --prefix $HOME/local/lib/mecab/dic/mecab-ipadic-neologd
RUN ln -s /etc/mecabrc /usr/local/etc/mecabrc

# python app settings
WORKDIR /usr/local/bin/
COPY ./Docker/Django_Bert/requirements.txt ./requirements.txt
RUN pip install torch==1.7.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN yes | pip install -r requirements.txt

WORKDIR /
COPY ./code/Kusorep_API ./Kusorep_API

RUN mkdir /Kusorep_API/KusorepCalculater/Bert/Data
WORKDIR /Kusorep_API/KusorepCalculater/Bert/Data
RUN wget -O data.zip "https://www.dropbox.com/sh/waj2hqp2zfox3o4/AACF9yMr-VHUYYrW6zP9PmCka"
RUN unzip data.zip

WORKDIR /Kusorep_API

EXPOSE 8001