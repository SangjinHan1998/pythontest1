from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode = "extended", height = 3)    # height -> 보여주는 데이터 갯수
listbox.insert(0, "Apple")
listbox.insert(1, "clock")
listbox.insert(2, "melon")
listbox.insert(END, "large")
listbox.insert(END, "gram")
listbox.pack()

def btncmd():
    # 맨 뒤에 항목을 삭제 괄호 안 숫자에 따라 순서 갈림
    # listbox.delete(0) 

    
    # 갯수 확인
    # print ("리스트에는", listbox.size(), "개가 있어요")
    
    # 항목 확인 (시작 index, 끝 index)
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0,2))

    # 선택된 항목 확인  (위치로 반환 (ex), (1,2,3))
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text = "클릭", command = btncmd)
btn.pack()

root.resizable(False, False) #  x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

root.mainloop()