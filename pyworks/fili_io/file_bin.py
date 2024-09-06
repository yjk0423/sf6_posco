# 바이너리 파일(binary file) 읽고 쓰기
# mode : 쓰기("wb"), 읽기("rd")
# 바이너리 기계어로 바꿈 -> encode
# 기계어를 텍스트로 변환하는 함수 -> decode

with open("./output/data.bin","wb") as f:

    txt = "드론이 날아간다" # TypeError str 안됨
    # f.write(txt)
    f.write(txt.encode())
with open("./output/data.bin","rb") as f2:

    print(f2.read().decode())
