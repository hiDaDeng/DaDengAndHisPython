import pandas as pd
import re
import jieba
from pyecharts import WordCloud

df = pd.read_json('data/27182640.json', lines=True)
df['content'] = df['content'].str.replace("[^\u4e00-\u9fa5]", "")
text = ''.join(df['content'].to_list())
f = open('data.txt', 'a+', encoding='utf-8')
f.write(text)
f.close()
"""
words = jieba.lcut(text)
wordfreq = []
for w in set(words):
    if len(w)>1:
        freq = words.count(w)
        wordfreq.append((w, freq))
sortwords = sorted(wordfreq, key=lambda k:k[1], reverse=True)

print(sortwords)
"""