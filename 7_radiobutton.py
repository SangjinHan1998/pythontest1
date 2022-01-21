from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

label1 = Label(root, text="Radiobutton : Choose one out of several.")
label1.pack()

label2 = Label(root, text = "Select Menu")
label2.pack()

color_var = IntVar()   # 여기에 int 형으로 값을 저장.
btn_color1 = Radiobutton(root, text="red", value = 1,  variable = color_var)
btn_color1.select()     # 기본값 선택
btn_color2 = Radiobutton(root, text="blue", value = 2,  variable = color_var)
btn_color3 = Radiobutton(root, text="white", value = 3,  variable = color_var)

btn_color1.pack()
btn_color2.pack()
btn_color3.pack()


label3 = Label(root, text = "=================================")
label3.pack()

code_var = StringVar()  # 문자 또는 숫자로 자료형 저장
btn_programming1 = Radiobutton(root, text = "Python", value = "a", variable = code_var)
btn_programming1.select()   # 기본값 선택
btn_programming2 = Radiobutton(root, text = "Java", value = "b", variable = code_var)
btn_programming3 = Radiobutton(root, text = "C++", value = "c", variable = code_var)

btn_programming1.pack()
btn_programming2.pack()
btn_programming3.pack()

def btncmd():
    print(color_var.get()) # 색깔 중 선택된 라디오 항목의 값(value) 을 출력
    print(code_var.get())

btn = Button(root, text = "Seloct Color", command = btncmd)
btn.pack()

label4 = Label(root, text = "=================================")
label4.pack()

label5 = Label(root, text = "combo box")
label5.pack()



root.mainloop()