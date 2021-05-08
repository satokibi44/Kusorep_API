FROM python:3.7.9

# basic libs
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y wget tar build-essential gcc zlib1g-dev git vim curl file sudo

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
RUN mkdir /Kusorep_API/KusorepCalculater/Bert/Data/tokenizer
WORKDIR /Kusorep_API/KusorepCalculater/Bert/Data
RUN apt-get install -y unzip
RUN wget "https://www.dropbox.com/s/dmie210yuc1t9pt/bert5.pickle"
RUN wget "https://www.dropbox.com/s/2i2xr0va3ciwb8f/best_epoche5"

WORKDIR /Kusorep_API/KusorepCalculater/Bert/Data/tokenizer
RUN wget "https://www.dropbox.com/s/0ghohdgzxcgq7z0/special_tokens_map.json"
RUN wget "https://www.dropbox.com/s/feu5rx7musbvl0o/tokenizer_config.json"
RUN wget "https://www.dropbox.com/s/f7i1rqygsnb6obm/vocab.txt"

WORKDIR /Kusorep_API

EXPOSE 8001