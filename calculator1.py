import tkinter as tk

disValue = 0
operator = {'+' : 1, '-' : 2, '/' : 3, '*' : 4, 'C' : 5, '=': 6}
stoValue = 0
opPre = 0

# 숫자를 넣었을 때 처리  

def number_click(value):
    # print('숫자', value)
    global disValue
    disValue = (disValue * 10) + value
    str_value.set(disValue)
    
# 명령을 넣었을 때 처리     
    
def clear():    
    global disValue, stoValue, opPre
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(disValue)

def oprator_click(value):
    # print('명령', value)  
    global disValue, operator, stoValue, opPre
    op = operator[value]
    if op == 5: # C
        clear()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(str(disValue))
    elif op == 6: #'=
        if opPre == 1:
            disValue = stoValue + disValue
        if opPre == 2:
            disValue = stoValue - disValue            
        if opPre == 3:
            disValue = stoValue / disValue    
        if opPre == 4:
            disValue = stoValue * disValue
            
        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        opPre = 0
    else:
        clear()        


def button_click(value):
    # print(value)
    try:
        value = int(value)
        number_click(value)
    except:
        oprator_click(value)
        
    
win = tk.Tk()
win.title('Calculator')

disValue = 0
str_value = tk.StringVar()  # 결과를 문자로 변환. StringVar 로 받아옴 
str_value.set(str(disValue))    # tk.StringVar 에 값을 넣어서 문자로 변해서 set을 함
dis = tk.Entry(win, textvariable = str_value, justify = 'right', bg = 'white', fg = 'red')
dis.grid(column = 0, row = 0, columnspan = 4, ipadx = 80, ipady = 30)

cal_Item = [['1','2','3','4'],
            ['5','6','7','8'],
            ['9','0','+','-'],
            ['/','*','C','=']]

for i, items in enumerate(cal_Item):
    for k,item in enumerate(items):
        
        try:
            color = int(item)
            color = 'black'
        except:
            color = 'green'
        
        bt = tk.Button(win, 
            text = item, 
            width = 10, 
            height = 5,
            bg = color,
            fg = 'hotpink',
            command = lambda cmd = item: button_click(cmd)  # 받아온 item 을 command 라는 변수에 넣고 변수를 cmd 값에 넣는다
            )
        bt.grid(column = k, row = (i+1))
# 1열

#tk.Button(win, text = '1', width = 10, height = 5).grid(column = 0, row = 1)
#tk.Button(win, text = '2', width = 10, height = 5).grid(column = 1, row = 1)
#tk.Button(win, text = '3', width = 10, height = 5).grid(column = 2, row = 1)
#tk.Button(win, text = '4', width = 10, height = 5).grid(column = 3, row = 1)

# 2열

#tk.Button(win, text = '5', width = 10, height = 5).grid(column = 0, row = 2)
#tk.Button(win, text = '6', width = 10, height = 5).grid(column = 1, row = 2)
#tk.Button(win, text = '7', width = 10, height = 5).grid(column = 2, row = 2)
#tk.Button(win, text = '8', width = 10, height = 5).grid(column = 3, row = 2)

# 3열

#tk.Button(win, text = '9', width = 10, height = 5).grid(column = 0, row = 3)
#tk.Button(win, text = '0', width = 10, height = 5).grid(column = 1, row = 3)
#tk.Button(win, text = '+', width = 10, height = 5).grid(column = 2, row = 3)
#tk.Button(win, text = '-', width = 10, height = 5).grid(column = 3, row = 3)

# 4열

#tk.Button(win, text = '/', width = 10, height = 5).grid(column = 0, row = 4)
#tk.Button(win, text = '*', width = 10, height = 5).grid(column = 1, row = 4)
#tk.Button(win, text = 'C', width = 10, height = 5).grid(column = 2, row = 4)
#tk.Button(win, text = '=', width = 10, height = 5).grid(column = 3, row = 4)

# grid 는 위치 배치 columnspan -> 위치 조정

win.mainloop()

