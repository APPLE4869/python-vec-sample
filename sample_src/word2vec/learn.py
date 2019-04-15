#coding: UTF-8
import MeCab
# import codecs
import urllib.parse as parser
import urllib.request as request
from bs4 import BeautifulSoup
from gensim.models import word2vec
from tqdm import tqdm

'''
処理１ スクレイピングで文章情報収集

Wikipediaをスクレイピングして文章情報を収集。
MeCabで「分かち書き」した状態でWord2Vecの処理に備える。
'''

print('# 処理１ スクレイピングで文章情報収集 開始')

tagger = MeCab.Tagger("-Owakati")
link = "https://ja.wikipedia.org/wiki/"
keyword = ["果物", "カリン", "チュウゴクナシ", "白梨", "ナシ", "マルメロ", "セイヨウカリン", "ジューンベリー", "リンゴ", "アメリカンチェリー", "アンズ", "ウメ", "サクランボ", "スミミザクラ", "スピノサスモモ", "スモモ", "モモ", "アーモンド", "イチョウ", "クリ", "クルミ", "ペカン", "アケビ", "イチジク", "カキ", "カシス", "キイチゴ", "キウイフルーツ", "グミ", "クワ", "クランベリー", "コケモモ", "ザクロ", "サルナシ", "シーバックソーン", "スグリ", "ナツメ", "ニワウメ", "ハスカップ", "ビルベリー", "フサスグリ", "ブドウ", "ブラックベリー", "ブルーベリー", "ポーポー", "マツブサ", "ラズベリー", "ユスラウメ", "オリーブ", "ビワ", "ヤマモモ", "織田信長", "徳川家康", "豊臣秀吉", "伊達政宗", "武田信玄", "上杉謙信", "明智光秀", "島津義弘", "北条氏康", "長宗我部元親", "毛利元就", "真田幸村", "立花宗茂", "石田三成", "浅井長政"]

corpus = []
for word in tqdm(keyword):
    # 記事をダウンロード
    with request.urlopen(link + parser.quote_plus(word)) as response:
        # responseはhtmlのformatになっている
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")
        # <p>タグを取得
        p_tags = soup.find_all('p')
        for p in p_tags:
            corpus.append(tagger.parse(p.text).strip())

# ファイルに保存するなら以下のような処理が利用される。
# with codecs.open("./scraping_data/pwiki.txt", "w", "utf-8") as f:
#     f.write("\n".join(corpus))
# with codecs.open("./scraping_data/pwiki.txt", "r", "utf-8") as f:
#     corpus = f.read().splitlines()

print('# 処理１ スクレイピングで文章情報収集 終了')



'''
処理２ Word2Vec 学習

スクレイピングした情報を元に学習モデルを作成する。
'''

print('# 処理２ Word2Vec 学習 開始')

corpus = [sentence.split() for sentence in corpus]

print(len(corpus))
print(corpus[0])
#モデルを作る
model = word2vec.Word2Vec(corpus, size=200, min_count=20, window=10)

# モデルを保存
model.save("./model/pwiki.model")

print('# 処理２ Word2Vec 学習 終了')
