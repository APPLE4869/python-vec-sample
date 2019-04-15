#coding: UTF-8
import MeCab
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from os import listdir, path
from tqdm import tqdm

def corpus_dirs():
    dirs = [path.join('text', x)
            for x in listdir('text') if not x.endswith('.txt')]
    return dirs

def corpus_files():
    dirs = corpus_dirs()
    docs = [path.join(x, y)
            for x in dirs for y in listdir(x) if not x.startswith('LICENSE')]
    return docs

corpus = corpus_files()
corpus = [path.join('text/livedoor-homme', x) for x in listdir('text/livedoor-homme') if x.endswith('.txt')]

tagger = MeCab.Tagger("-Owakati")

# １文書ずつ、単語に分割してリストに入れていく[([単語1,単語2,単語3], 文書id),...]こんなイメージ
# words：文書に含まれる単語のリスト（単語の重複あり）
# tags：文書の識別子（リストで指定．1つの文書に複数のタグを付与できる）
print("文章読み込み中...")
trainings = []
for doc in tqdm(corpus):
    f = open(doc)
    for i, data in enumerate(f):
        if i == 0 or i == 1: # URLと掲載時刻は除外
            continue
        trainings.append(TaggedDocument(words = tagger.parse(data).strip().split(), tags = [doc]))
print("記事数 : " + str(len(corpus)))
print("文章数 : " + str(len(trainings)))
print("文章読み込み完了")

# 学習
print("\n学習中...")
# dm=0 : DBoW
# dm=1 : dmpv
model = Doc2Vec(documents= trainings, dm=1, vector_size=300, window=8, min_count=10, workers=5, epochs=10)
print("\n学習完了")

# 学習モデルの保存
model.save("model/doc2vec.model")
print("\n学習モデルを保存しました！")
