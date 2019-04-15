FROM python:3.7

ADD . app
WORKDIR /app

RUN apt-get update -qq
RUN apt-get install -y --no-install-recommends
# Mecabを使うための前準備
RUN apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 swig

# Pythonで利用するライブラリをインストール
RUN pip install -r ./requirements.txt
