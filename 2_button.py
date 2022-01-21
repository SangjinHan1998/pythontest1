from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")

btn1 = Button(root, text = "버튼 1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text = "버튼 2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text = "버튼 3")
btn3.pack()
 
btn4 = Button(root, width = 10, height = 3,  text = "버튼 4")
btn4.pack()

# padx는 글자 길이에 따라 버튼 크기 바뀜 width 는 고정된 크기 값을 가짐 

btn5 = Button(root, fg = "white", bg = "green",  padx=15, pady=20, text = "버튼 5")
btn5.pack()

photo = PhotoImage(file = "gui_basic/img1.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("Click Button :) ")

btn7 = Button(root, text = "Button that moves", command = btncmd)
btn7.pack()

# In btn7, The function executes.


root.mainloop()