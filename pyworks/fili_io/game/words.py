# 영어 단어장 만들기
# 경로 - game

import random

word = ["sky","earth","moon","flower","tree","apple","mountanin","garlic","onion","poatato"]

with open("word.txt","w") as f :
    for a in word:
      f.write(a + ' ')

with open("word.txt","r") as f :

    # print(f.read())
    data = f.read().split()
    print(random.choice(data))