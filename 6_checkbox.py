from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표


chkvar = IntVar() # chkvar 에 int 형으로 값을 저장
chkbox = Checkbutton(root, text = "오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text = "일주일 동안 보지 않기" , variable = chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제 1 : 체크
    print(chkvar2.get())

btn = Button(root, text = "Click", command = btncmd)
btn.pack()

root.mainloop()