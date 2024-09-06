# with open(파일경로,모드) as 파일객체 구문
# 자원 누수 방지를 위해 f.close()를 사용하지 않음
try:
    with open("./sourse/data.txt", "w") as f1:
        f1.write("Heelo World\n")
        f1.write("폭염이 극성이다.\n")
        num = "1KB는 %dB이다" % 1024
        f1.write(num)
    with open("./sourse/data.txt", "r") as f2:
        data = f2.read()
        print(data)
except FileNotFoundError:
    print(FileNotFoundError)

