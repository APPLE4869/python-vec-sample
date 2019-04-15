#coding: UTF-8
from gensim.models import word2vec
from gensim.models.keyedvectors import KeyedVectors

'''
処理３ Word2Vec 学習モデルを利用

スクレイピングした文章で学習したモデルを実際に使って、文字のベクトルや類似度などを見ていく。
'''

print('# 処理３ Word2Vec 学習モデルを利用 開始')

# モデルを読み込む
model = word2vec.Word2Vec.load("./model/pwiki.model")
# model = KeyedVectors.load_word2vec_format("./min_model/entity_vector/entity_vector.model.txt")


# 単語のベクトルを見る
word_vector_word = "リンゴ"
word_vector = model.wv[word_vector_word]
print("「" + word_vector_word + "」という言葉のベクトル")
print(word_vector)


# 尾張と類似している単語を見る
most_similar_word = "人"
similar_words = model.wv.most_similar(positive=[most_similar_word], topn=5)
print("\n「" + most_similar_word + "」に最も類似した単語トップ5")
for i in similar_words:
    print(i[0])
    print(i[1])


# 尾張と類似している単語を見る
most_similar_word = "信長"
    similar_words = model.wv.most_similar(positive=[most_similar_word], topn=5)
    print("\n「" + most_similar_word + "」に最も類似した単語トップ5")
    for i in similar_words:
        print(i[0])
        print(i[1])


# ２つの単語の類似度を計算。
similarity_1 = model.wv.similarity(w1="リンゴ", w2="梨")
similarity_2 = model.wv.similarity(w1="将軍", w2="リンゴ")
similarity_3 = model.wv.similarity(w1="将軍", w2="信長")

print("\nsimilarity")
print(similarity_1)
print(similarity_2)
print(similarity_3)

print('# 処理３ Word2Vec 学習モデルを利用 終了')

# print(model.wv.index2word)
# print(model.wv.syn0)
