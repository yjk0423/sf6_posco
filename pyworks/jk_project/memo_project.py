# 개인공부 
# 메모장에 변수 및 값을 저장하고 불러오는 로직 구현

def save_variable():
    file_name = input("변수 값을 저장할 파일 이름을 입력하세요 (예: variables.txt): ")
    file_path = "C:/kdt_sf6/" + file_name
    with open(file_path, "w") as file:
        while True:
            key = input("저장할 변수 이름 입력 (종료하려면 '종료' 입력): ")
            if key.lower() == '종료':
                break
            value = input(f"{key}의 값을 입력하세요: ")
            file.write(f"{key}={value}\n")

    print(f"변수와 값이 {file_path}에 저장되었습니다.")


def get_variable_value():
    file_name = input("변수 값을 읽어올 파일 이름을 입력하세요 (예: variables.txt): ")
    file_path = "C:/kdt_sf6/" + file_name

    try:
        with open(file_path, "r") as file:
            variables = {}
            for line in file:
                key, value = line.strip().split('=')
                variables[key] = value

            while True:
                query = input("값을 조회할 변수 이름 입력 (종료하려면 '종료' 입력): ")

                if query in variables:
                    print(f"{query}의 값: {variables[query]}")
                else:
                    print("해당 변수는 존재하지 않습니다.")
                if query.lower() == '종료':
                    break

    except FileNotFoundError:
        print("파일이 존재하지 않습니다.")

def memo_variable_app():
    while True:
        print("\n1. 변수와 값 저장")
        print("2. 변수 값 조회")
        print("3. 종료")
        choice = input("선택하세요: ")

        if choice == '1':
            save_variable()
        elif choice == '2':
            get_variable_value()
        elif choice == '3':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

memo_variable_app()