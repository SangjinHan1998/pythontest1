import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI ProgressBar")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표


#progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")  # indeterminate = 쉽게 가늠할 수 없는
p_var1 = DoubleVar()
progressbar1 = ttk.Progressbar(root, maximum = 100, length = 250, variable = p_var1) 
progressbar1.pack()

def btncmd1():
    for i in range(1, 101): # 1 ~ 100
        time.sleep(0.01)    # 0.01 초 대기 
        
        p_var1.set(i)   # progress bar 의 값 설정
        progressbar1.update()   # ui 업데이트
        print(p_var1.get)

btn = Button(root, text = "START", command = btncmd1)
btn.pack()

root.mainloop()