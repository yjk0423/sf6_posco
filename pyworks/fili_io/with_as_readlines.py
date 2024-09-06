team = ["서울","인천","부산","광주","대전","대구"]
with open("./sourse/city.txt","w") as f:
    for i in team:
        f.write(i + "\n")
with open("./sourse/city.txt","r") as f:
    # print(f.readlines())
    # print(f.readline().split())
    a = []
    for i in range(6):
        a.append(f.readline().split()) # 구분 기호로 요소분리

    # print(a[:])
    # print(a[0][0])
    # print(a[0][0])
    # print(a[-1][0])
    for i in a:
        print(i[0])