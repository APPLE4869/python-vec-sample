#coding: UTF-8
'''
本スクリプト実行前に必ず同ディレクトリのlearn.pyを実行して学習モデルを作成しておく必要がある。
'''
from gensim.models.doc2vec import Doc2Vec

# 学習モデルの読み込み
model = Doc2Vec.load('model/doc2vec.model')

#引数は文書id
similar = model.docvecs.most_similar("text/livedoor-homme/livedoor-homme-4568088.txt")
s = model.docvecs.similarity("text/livedoor-homme/livedoor-homme-4568088.txt", "text/livedoor-homme/livedoor-homme-4568088.txt")
print(similar)
print(s)

# 例えば、以下の４つの新規文書の、いくつかの組み合わせの類似度を計算してみる
doc_words1 = ["ラスト", "展開", "早い", "他", "作品", "衝撃", "受ける", "裏の裏", "つく", "トリック", "毎度", "こと", "脱帽", "する", "読む", "やすい", "め", "ミステリー"]
doc_words2 = ["ラスト", "展開", "早い", "他", "作品", "衝撃", "受ける", "裏の裏", "つく", "トリック", "毎度", "こと", "脱帽", "する", "読む", "やすい", "め", "ミステリー"]
doc_words3 = ["ラスト", "展開", "早い", "他", "作品", "衝撃", "受ける", "裏の裏", "つく", "ミステリー"]
doc_words4 = ["昔々", "ある", "ところ", "に"]

print("\n1-2 sim")
print("（全く同じ）")
sim_value = model.docvecs.similarity_unseen_docs(model, doc_words1, doc_words2, alpha=1, min_alpha=0.0001, steps=5)
print(sim_value)

print("\n1-3 sim")
print("（後半が少し違う）")
print(model.docvecs.similarity_unseen_docs(model, doc_words1, doc_words3, alpha=1, min_alpha=0.0001, steps=5))

print("\n1-4 sim")
print("（全然違う）")
print(model.docvecs.similarity_unseen_docs(model, doc_words1, doc_words4, alpha=1, min_alpha=0.0001, steps=5))

print("\n2-3 sim")
print("（後半が少し違う）")
print(model.docvecs.similarity_unseen_docs(model, doc_words2, doc_words3, alpha=1, min_alpha=0.0001, steps=5))

newvec = model.infer_vector(doc_words1)

print('\nnewvec')
print(newvec)
