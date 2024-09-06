# 이미지 읽고 쓰기

with open("space.png","rb") as f1:
    img = f1.read()

with open("./output/space.png","wb") as f2:
    f2.write(img)
