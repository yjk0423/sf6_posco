import random
import time

with open("word.txt","r") as f:
    word = f.read().split()

n = 1

input("[타자게임] 준디되면 엔터!")
start = time.time()
while n < 11:
    question = random.choice(word)
    print(f"{n}번: {question}")
    user = input()
    if user == question:
        print("정답")
        n += 1

    else:
        print("오타, 다시 도전")

end = time.time()
et = end - start

print(f'타자 시간: {et : .2f}초')
print("프로그램 종료")
