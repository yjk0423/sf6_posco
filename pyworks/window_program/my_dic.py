# 컴퓨터 작은 사전 만들기
from tkinter import *
def click():
    try:
        word = entry.get()
        text.delete(0.0, END) #END - 최종입력지점 #앞0-행, 뒤0-열
        definition = dic[word]
    except KeyError:
        definition = "단어를 찾을 수 없습니다."
    text.insert(END, definition)

dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료 구조"
}



root = Tk()
root.title("컴퓨터 소사전")

Label(root, text="단어를 입력하고 제출 버튼을 누르세요").grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=1, column=0, sticky=W)

Button(root, text="제출", width=10, command=click).grid(row=2, column=0, sticky=W)

Label(root, text="정의: ").grid(row=3, column=0, sticky=W)
#출력상자 - Text()
text = Text(root, width=80, height=10, bg="light sky blue")
text.grid(row=3, column=0, sticky=W)

root.mainloop()