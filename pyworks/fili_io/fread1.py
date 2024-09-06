# 파일 열기 - 기존의 파일의 내용을 읽어오는

file_fath = "C:/pyfile/file1.txt"

f = open(file_fath,"r")
data = f.read()
print(data)

f.close()
