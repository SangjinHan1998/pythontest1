import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI ProgressBar")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표


#progressbar = ttk.Progressbar(root, maximum = 100, mode = "indeterminate")  # indeterminate = 쉽게 가늠할 수 없는
progressbar = ttk.Progressbar(root, maximum = 100, mode = "determinate") 
progressbar.start(10)   # 10 ms 마다 움직임
progressbar.pack()

def btncmd():
    progressbar.stop()  # 작동 중지


btn = Button(root, text = "STOP", command = btncmd)
btn.pack()

root.mainloop()