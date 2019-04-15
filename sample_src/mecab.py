#coding: UTF-8
'''
mecab-python3
https://github.com/SamuraiT/mecab-python3

mecab
https://github.com/taku910/mecab
'''
import MeCab

'''
Taggerメソッドの引数
mecabrc: (デフォルト)
-Ochasen: (ChaSen 互換形式)
-Owakati: (分かち書きのみを出力)
-Oyomi: (読みのみを出力)
'''

TEXT = '美しい女性を口説こうと思った時、ライバルの男がバラの花を10本贈ったら、君は15本贈るかい？そう思った時点で君の負けだ。ライバルが何をしようと関係ない。その女性が本当に何を望んでいるのかを、見極めることが重要なんだ。'
print('# 「元文章」出力結果')
print(TEXT)

# 分ち書き
tagger = MeCab.Tagger("-Owakati")
result = tagger.parse(TEXT)
print('\n# 「分ち書き」出力結果')
print(result)

# 読みのみ出力
tagger = MeCab.Tagger("-Oyomi")
result = tagger.parse(TEXT)
print('\n# 「読みのみ」出力結果')
print(result)

# 形態素解析
tagger = MeCab.Tagger('-Ochasen')
result = tagger.parse(TEXT)
print('\n# 「形態素解析」出力結果')
print(result)
