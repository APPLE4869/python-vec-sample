REPOSITORY='python-vec'

IMAGE_ID=$(docker image ls -q ${REPOSITORY})
# イメージがまだ存在しなければイメージを作成
if [ -z "$IMAGE_ID" ]; then
  # Imageを作成
  docker build ./ -t ${REPOSITORY}
  IMAGE_ID=$(docker image ls -q ${REPOSITORY})
fi

# livedoor ニュースコーパスのデータを解凍
# @see https://www.rondhuit.com/download.html#ldcc
THAWING_DIR='text'
if [ ! -d "$THAWING_DIR" ]; then
  tar xvfz ldcc-20140209.tar.gz
  echo 'livedoor ニュースコーパスのデータを解凍しました！'
fi

# コンテナを起動 & コンテナの中に入る
PWD=$(pwd)
WORKDIR='/app'
docker run --rm -v ${PWD}:${WORKDIR} -it ${IMAGE_ID} /bin/bash
