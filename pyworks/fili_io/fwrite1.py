#파일 쓰기

# 파일열기 (open()) > 파일쓰기(write()) > 종료 close()
# 모드 w쓰기, r읽기 , a추가


f = open("C:/pyfile/file1.txt","w")
f.write("Hello~ Python")


f.close()