#readline() - 한줄을 읽음
#readlines() - 모두 값을 가지고 오고 리스트 로 재정의 함

f = open("c:/pyfile/file1.txt", "r")

# print(f.readline())
# print(f.readlines())
# print(f.readable())
while True:
    line = f.readline()
    if not line:
        break
    print(line.strip()) # 공백제거
f.close()
