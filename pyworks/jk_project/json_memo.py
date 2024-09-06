# 개인공부
# json 메모장에 저장하고 불러오는 로직

import json
file_path = "C:/kdt_sf6/json.txt"


def set_json():
    data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "courses": ["Math", "Science", "Literature"]
    }
    with open(file_path,"w")as file:
        json.dump(data,file,indent=4)
    print("joson 값 저장완료")

def get_json():
    with open(file_path, "r") as file:
        data = json.load(file)
    return data
    # print("Data loaded from data.json:")
    # print(data)
    # print(data["name"])

get_json()