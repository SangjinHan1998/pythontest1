import os 
from tkinter import *

root = Tk()
root.title("제목없음 - Windows 메모장")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right", fill = "y")

# 열기, 저장 파일 이름
filename = "mynote.txt"

# 명령어 집합
def open_file():
    if os.path.isfile(filename): # 파일이 있다면 True 없다면 False
        with open(filename, "r", encoding = "utf8") as file : 
            txt.delete("1.0", END)  # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read())    # 파일 내용을 본문에 입력
    
        

def save_file():
    with open(filename, "w", encoding = "utf8") as file : 
        file.write(txt.get("1.0", END))    # 모든 내용을 가져와서 저장

# 메뉴창
menu = Menu(root)

menu_file = Menu(menu, tearoff= 0)
menu_file.add_command(label="Open", command = open_file)
menu_file.add_command(label="Save", command = save_file)
# 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command = root.quit)
menu.add_cascade(label="File" , menu = menu_file)

menu_file = Menu(menu, tearoff= 0)
menu.add_cascade(label="Edit" , menu = menu_file)
menu.add_cascade(label="Form" , menu = menu_file)
menu.add_cascade(label="Example" , menu = menu_file)
menu.add_cascade(label="Form" , menu = menu_file)
menu.add_cascade(label="Help" , menu = menu_file)


frame = Frame(root)
frame.pack()
# 본문 영역 
txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side = "left", fill = "both" , expand = True)

scrollbar.config(command = txt.yview)

root.config(menu=menu)
root.mainloop()