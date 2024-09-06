from tkinter import *

def click():
    # entry.get() 입력된 이름 가지고 오기
    label.config(text=entry.get())


root = Tk()
root.title('이름 입력')
root.geometry('400x200+500+500')

frame = Frame(root)
frame.pack() # 한줄을 차지

Label(frame,text="이름: ").grid(row=0,column=0)
# 입력상자(Entry())
entry = Entry(frame)
entry.grid(row=0, column=1)
Button(frame,text="확인", command=click).grid(row=1,columnspan=2)
label = Label(frame,text="")
label.grid(row=2,columnspan=2)


root.mainloop()


