import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+500+300")  # 가로 * 세로 + x좌표 + y좌표

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료됨")
    
def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진됨")
    
def error():
    msgbox.showerror("에러", "결제 오류 발생")
    
def okcancel():
    msgbox.askokcancel("확인 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")    
       
def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까??")
    
def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = "예매내역이 저장되지 않았습니다. \n 저장 후 프로그램을 종료하시겠습니까??") 
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소(현재 화면에서 계속 작업)
    print("응답 : ", response )     # True, False, None -> 예 1, 아니오 0 , 그 외
    if response == 1: # ok
        print("OK")
    elif response == 0: # NO
        print("NO")
    else:
        print("Cancel")
    
    
# ask test    
def ask1():
    msgbox.askyesno("ask1", "ask123")

# Button
Button(root, command = info, text = "알림").pack()
Button(root, command = warn, text = "경고").pack()
Button(root, command = error, text = "에러").pack()

Button(root, command = okcancel, text = "취소").pack()
Button(root, command = retrycancel, text = "재시도 취소").pack()
Button(root, command = yesno, text = "예 아니오").pack()
Button(root, command = yesnocancel, text = "예 아니오 취소").pack()




# ask test
Button(root, command = ask1, text = "ask1").pack()



root.mainloop()