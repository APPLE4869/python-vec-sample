REPOSITORY='python-vec-sample'

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
  tar xvfz livedoor-corpus.tar.gz
  echo 'livedoor ニュースコーパスのデータを解凍しました！'
fi

GZIP_FILE='amazon_reviews.json'
if [ ! -e "$GZIP_FILE" ]; then
  echo 'Amazonレビューのデータを解凍中...'
  SPLITTED_FILE_PREFIX='amazon_reviews_'
  GZIP_REVIEW_FOLDER='gzip_amazon_reviews'

  for suffix in aa ab ac ad ae af ag ah ai aj ak al
  do
    gzip -d ${GZIP_REVIEW_FOLDER}/${SPLITTED_FILE_PREFIX}${suffix}.gz -c > ${SPLITTED_FILE_PREFIX}${suffix}
  done

  cat ${SPLITTED_FILE_PREFIX}* >> ${GZIP_FILE}

  for suffix in aa ab ac ad ae af ag ah ai aj ak al
  do
    rm ${SPLITTED_FILE_PREFIX}${suffix}
  done

  echo 'Amazonレビューのデータを解凍しました！'
fi

# コンテナを起動 & コンテナの中に入る
PWD=$(pwd)
WORKDIR='/app'
docker run --rm -v ${PWD}:${WORKDIR} -it ${IMAGE_ID} /bin/bash
