from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

Label(root, text = "Select Menu.").pack(side="top")

Button(root, text = "Country").pack(side = "bottom")

# Europe frame
frame_europe = Frame(root, relief = "solid", bd = 1)
frame_europe.pack(side = "left", fill = "both", expand = True)

Button(frame_europe, text = "France").pack()
Button(frame_europe, text = "Germany").pack()
Button(frame_europe, text = "Spain").pack()

# Asia frame
frame_asia = LabelFrame(root, text = "Asia")
frame_asia.pack(side = "right", fill = "both", expand = True)

Button(frame_asia, text = "South Korea").pack()
Button(frame_asia, text = "Japan").pack()

root.mainloop()