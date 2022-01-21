import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

values = [str(i) + "일" for i in range (1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height = 5, values =values)   # 최초 목록 5개
combobox.pack()
combobox.set("카드 결제일")

readonly_combobox = ttk.Combobox(root, height = 10, values =values, state = "readonly") # 읽기 전용 최초 목록 10개
readonly_combobox.current(0)    # 0번째 인덱스 값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())   # 선택된 값 표시
    print(readonly_combobox.get())


btn = Button(root, text = "ORDER", command = btncmd)
btn.pack()

root.mainloop()