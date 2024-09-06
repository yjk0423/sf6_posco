# try ~ except ~ finally






def divide(x,y):
    try:
        result = x/y
        print(result)
    except ZeroDivisionError:
        print(ZeroDivisionError)

    finally:
        # 실행이 성공하든 실패하던 반드시 실행
        # 예 마이크로 프로세서에서 재부팅하는 경우
        print("여기는 반드시 수행됩니다.")


divide(2,3)
divide(2,0)


