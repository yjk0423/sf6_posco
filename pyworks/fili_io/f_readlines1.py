# readlines() - 데이터를 리스트로 반환
try:
    f = open("./sourse/season.txt", "r")

    seasons = f.readlines() # 데이터를 리스트로 저장
    print(seasons)
    print(seasons[0])

    for season in seasons:
        print(season.strip())

    f.close()

except FileNotFoundError:
    print(FileNotFoundError, ": 파일을 찾을수 없음")
#       내부의 에러 메세지 보고 싶을때