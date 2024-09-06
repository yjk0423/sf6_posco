# 리스트 자료
# 상대경로 - source 폴더 : 내 파일 기준으로 같은 계층이면 ./
# 내기준 상위이면 ../

season = ["봄","여름","가을","겨울"]
f = open("./sourse/season.txt", "w")

for i in season:
    f.write(i)
    f.write("\n")

f.close()

f = open("./sourse/season.txt", "r")

data = f.read()
print(data)

f.close()

