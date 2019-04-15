REPOSITORY='python-vec'

IMAGE_ID=$(docker images ${REPOSITORY} --format='{{.ID}}')
if [ -n "$IMAGE_ID" ]; then
  docker rmi ${IMAGE_ID}
fi

# livedoor ニュースコーパスのデータを解凍
# @see https://www.rondhuit.com/download.html#ldcc
THAWING_DIR='text'
if [ -d "$THAWING_DIR" ]; then
  rm -rf $THAWING_DIR
  echo 'livedoor ニュースコーパスのデータを解凍データを削除しました。'
fi
