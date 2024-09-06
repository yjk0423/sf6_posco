# 실습1
import random

numbers = []
for i in range(4):
    n = random.randint(1, 100) #랜덤 요소
    numbers.append(n)

numbers.sort()  #오름 차순
print(numbers)

# 실습 2
# 리스트로 구현하기
lotto = []
while True:
    n = random.randint(1, 45) #랜덤 요소
    if n not in lotto:
        lotto.append(n)
    if len(lotto) == 6:
        break
lotto.sort()
print(lotto)

numbers1 = set()  # 빈 집합 생성
while True:
    n = random.randint(1, 45)  # 1부터 45 사이의 랜덤 숫자 생성
    numbers1.add(n)  # 집합에 숫자 추가
    if len(numbers1) == 6:
        break
print(sorted(numbers1))