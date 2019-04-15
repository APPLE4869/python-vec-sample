# Doc2Vecの仕組みとgensimを使った文書類似度算出チュートリアル
# @see https://deepage.net/machine_learning/2017/01/08/doc2vec.html

import sys
from os import listdir, path
from pyknp import Jumanpp
from gensim import models
from gensim.models.doc2vec import LabeledSentence

def corpus_files():
    dirs = [path.join('../text', x)
            for x in listdir('../text') if not x.endswith('.txt')]
    docs = [path.join(x, y)
            for x in dirs for y in listdir(x) if not x.startswith('LICENSE')]
    return docs

def read_document(path):
    with open(path, 'r') as f:
        return f.read()

def split_into_words(text):
    result = Jumanpp().analysis(text)
    return [mrph.midasi for mrph in result.mrph_list()]

def doc_to_sentence(doc, name):
    words = split_into_words(doc)
    return LabeledSentence(words=words, tags=[name])

def corpus_to_sentences(corpus):
    docs   = [read_document(x) for x in corpus]
    for idx, (doc, name) in enumerate(zip(docs, corpus)):
        sys.stdout.write('\r前処理中 {}/{}'.format(idx, len(corpus)))
        yield doc_to_sentence(doc, name)

corpus = corpus_files()
sentences = corpus_to_sentences(corpus)

model = models.Doc2Vec(sentences, dm=0, size=300, window=15, alpha=.025,
        min_alpha=.025, min_count=1, sample=1e-6)

print('\n訓練開始')
for epoch in range(20):
    print('Epoch: {}'.format(epoch + 1))
    model.train(sentences)
    model.alpha -= (0.025 - 0.0001) / 19
    model.min_alpha = model.alpha

model.save('doc2vec.model')
model = models.Doc2Vec.load('doc2vec.model')
