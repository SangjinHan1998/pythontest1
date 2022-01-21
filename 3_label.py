from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+100+100")

label1 = Label(root, text="Nice to meet you")
label1.pack()

photo = PhotoImage(file="gui_basic/img1.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text = "See you next Time")
    
    global photo2   # 레이블의 이미지를 바꾸기 위해 이미지 값을 전역 변수로 바꿈
    # 전역변수(global veriabel) :  어떤 변수 영역에서도 접근할 수 있는 변수
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

    # Garbage Collection : 불필요한 메모리 공간 해제

btn = Button(root, text = "Click" , command = change)
btn.pack()



root.mainloop()