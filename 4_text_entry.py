from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

txt = Text(root, width = 30, height = 5)
txt.pack()
txt.insert(END, "Insert text")

e = Entry(root, width = 30)
e.pack()
e.insert(0, "Insert Only 1 line")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))      #  1 -> 첫번째 라인, 0 -> 0번째 column 위치
    print(e.get())  # 아래 Text

    # 내용 삭제 (데이터 입력후 처음 텍스트 사라짐)
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()