# 실습 1

while True:
    try:
        value = int(input("숫자를 입력해주세요: "))
        if isinstance(value, int):
            print("정수 입력 성공")
            break
    except ValueError as e:
        print("정수가 아님! 정수를 입력해주세요.")

