REPOSITORY='python-vec-sample'

IMAGE_ID=$(docker images ${REPOSITORY} --format='{{.ID}}')
if [ -n "$IMAGE_ID" ]; then
  docker rmi ${IMAGE_ID}
  echo 'Dockerイメージを削除しました！'
fi

# livedoor ニュースコーパスの解凍データを削除
# @see https://www.rondhuit.com/download.html#ldcc
THAWING_DIR='text'
if [ -d "$THAWING_DIR" ]; then
  rm -rf $THAWING_DIR
  echo 'livedoor ニュースコーパスのデータを解凍データを削除しました。'
fi

# Amazonレビューの解凍データを削除
GZIP_FILE='amazon_reviews.json'
if [ -e "$GZIP_FILE" ]; then
  rm -rf $GZIP_FILE
  echo 'Amazonレビューのデータを解凍データを削除しました。'
fi
