# pickle 모듈 - 객체(리스트, 딕셔너리)의 형태 그래도 저장하고 읽을 수있는 모듈
# dump 쓰기 , load 읽기
import pickle

# 파일에 쓰기
with open("./output/data.txt","wb") as f:
    li = ["강아지", "닭","고양이","소"]
    dict = {1:"고구마",
            2:"옥수수",
            3:"감자떡",
            }


    pickle.dump(li,f)   #자료(리스트) 객체, 파일 객체
    pickle.dump(dict,f) #자료(딕셔너리) 객체,파일 객체

with open("./output/data.txt","rb") as f:

    li = pickle.load(f)
    li2 = pickle.load(f)
    print(li)
    print(li2)