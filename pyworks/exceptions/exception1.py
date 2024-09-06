# 다중 예외 처리
# try:
#     num = [1,2,3,4]
#
#     num[11] #IndexError
#     num[3] / 0 #ZeroDivisionError
#     # print(ink) #NameError
#
# except IndexError:
#     print(IndexError)
# except ZeroDivisionError:
#     print(ZeroDivisionError)
# except NameError:
#     print(NameError)
# except:
#     print("예외 없음")

try:
    num = int(input("숫자 입력: "))

except ValueError as e:
    # print("정수가 아님")
    print(e)