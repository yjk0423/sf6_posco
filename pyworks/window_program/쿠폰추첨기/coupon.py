# 추첨 버튼을 누르면 3명이 랜덤하게 출력됨
from  tkinter import *
import random

def click():
    name_list = ['김용준','김용혁','임현수','윤종관','정지은','오민선','윤다빈','박민우','최준영','고지수','조형주']
    member = []

    win = set()

    while len(win) < 3:
        ran1 = random.choice(name_list)
        # if ran1 not in member:
        #     member.append(ran1)
        win.add(ran1)
    text.delete(0.0, END)
    text.insert(END,win)

window = Tk()
window.title("쿠폰 추첨기")
lbl_img = Label(window)
# 이미지 객체 생성
img = PhotoImage(file="bronx.png")
lbl_img.config(image=img)
lbl_img.grid(row=0,column=0, sticky=W)

#추첨 버튼
Button(window, text="추첨", command=click).grid(row=1,column=0,sticky=E)
# 출력상자
text = Text(window, width=47, height=3, bg="yellow")
text.grid(row=2,column=0, sticky=W)



window.mainloop()
