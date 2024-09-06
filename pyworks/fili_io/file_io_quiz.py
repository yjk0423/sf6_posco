# 실습 1
#
# file_fath = open("C:/pyfile/gugudan.txt","w")
#
# for i in range(2, 10):
#     for j in range(1, 10):
#         file_fath.write(f"{i} x {j} = {i * j}"+"\n")
#
# file_fath.close()
#
# file_fath = open("C:/pyfile/gugudan.txt","r")
# data=file_fath.read()
#
# print(data)
#

# 실습 2

try:
    member_id = []
    member_pw = []
    for i in range(3):
        name = input("이름 입력: ")
        pw = input("pw 입력: ")
        member_id.append(name)
        member_pw.append(pw)

    with open("./output/member.txt", "w") as f:
        for i in range(3):
            f.write(f"{member_id[i]} {member_pw[i]}\n")
except:
    print("파일 경로 못찾음")

try:
    with open("./output/member.txt", "r") as f1:
        data = f1.read()
        print(data)
except:
    print("경로 못찾음")

# 로그인
name = input("이름 입력: ")
pw = input("pw 입력: ")
user = f"{name} {pw}"

with open("./output/member.txt", "r") as f1:
    member_list = f1.readlines()

sw = False
for member in member_list:
    if member.strip() == user:
        sw = True
        break

if sw == True:
    print("로그인 성공")
else:
    print("로그인 실패")
