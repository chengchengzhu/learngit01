import tkinter

# 创建tkinter主窗口
root = tkinter.Tk()
root.minsize(320,600)
root.title('Calculator')

# 分屏显示结果，up显示计算式子，down显示数字与最终结果
result_down = tkinter.StringVar()
result_down.set('0')
result_up   = tkinter.StringVar()
result_up.set('')

# 显示结果绑定标签并定位
# bd = borderwidth 线框宽度
label_down = tkinter.Label(root, font=('微软雅黑',40), bg='#EEE9E9', bd='6', anchor='se', textvariable=result_down)
label_down.place(x=0, y=200, width=320, height=80)
label_up = tkinter.Label(root, font=('微软雅黑',30), bg='#EEE9E9', bd='6', anchor='se', textvariable=result_up)
label_up.place(x=0, y=0, width=320, height=200)


# 创建数字按钮并绑定函数
b7 = tkinter.Button(root, text='7', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('7'))
b7.place(x=0 , y=345, width=80, height=65)
b8 = tkinter.Button(root, text='8', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('8'))
b8.place(x=80, y=345, width=80, height=65)
b9 = tkinter.Button(root, text='9', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('9'))
b9.place(x=160, y=345, width=80, height=65)

b4 = tkinter.Button(root, text='4', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('4'))
b4.place(x=0 , y=410, width=80, height=65)
b5 = tkinter.Button(root, text='5', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('5'))
b5.place(x=80, y=410, width=80, height=65)
b6 = tkinter.Button(root, text='6', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('6'))
b6.place(x=160, y=410, width=80, height=65)

b1 = tkinter.Button(root, text='1', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('1'))
b1.place(x=0 , y=475, width=80, height=65)
b2 = tkinter.Button(root, text='2', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('2'))
b2.place(x=80, y=475, width=80, height=65)
b3 = tkinter.Button(root, text='3', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('3'))
b3.place(x=160, y=475, width=80, height=65)

b0 = tkinter.Button(root, text='0', font=('微软雅黑',30),  bg='#EEE9E9', bd='1', command=lambda : pressNum('0'))
b0.place(x=80, y=540, width=80, height=65)



# 创建功能按钮并绑定函数
bAC = tkinter.Button(root, text='AC', font=('微软雅黑',30), fg='orange', bg='#EEE9E9', bd='1', command=lambda :pressCompute('AC'))
bAC.place(x=0, y=280, width=80, height=65)
bdel = tkinter.Button(root, text='←', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('del'))
bdel.place(x=80, y=280, width=80, height=65)
bdiv = tkinter.Button(root, text='÷', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('/'))
bdiv.place(x=160, y=280, width=80, height=65)
btimes = tkinter.Button(root, text='×', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('*'))
btimes.place(x=240, y=280, width=80, height=65)
bminus = tkinter.Button(root, text='－', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('-'))
bminus.place(x=240, y=345, width=80, height=65)
bplus = tkinter.Button(root, text='＋', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('+'))
bplus.place(x=240, y=410, width=80, height=65)

bpoint = tkinter.Button(root, text='.', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('.'))
bpoint.place(x=160, y=540, width=80, height=65)
bpercen = tkinter.Button(root, text='%', font=('微软雅黑',30), bg='#EEE9E9', bd='1', command=lambda :pressCompute('%'))
bpercen.place(x=0, y=540, width=80, height=65)

bequ = tkinter.Button(root, text='＝', font=('微软雅黑',30), bg='orange', bd='1', command=lambda :pressEqual())
bequ.place(x=240, y=475, width=80, height=130)


# 初始化
# lists用于存放最终计算的式子，含数字与四则运算符（计算过程中并不会显示）
# isPressFunc用于指示是否按下运算符
lists=[]
isPressFunc = False
isPressDel = False


# 数字按钮绑定函数，只用于数字标签的显示
def pressNum(num):
    global lists,isPressFunc
    # 如果还未按下运算按钮，则pass
    if isPressFunc == False:
        pass
    # 如果已经按下，则将之前的结果清零，指示值重设为False
    else:
        result_down.set('0')
        isPressFunc = False

    # 将原有数字存为oldnum，如果为0，则新按数字为显示结果，若不为0，则老“拼接”新为显示结果
    oldnum = result_down.get()
    if oldnum == '0':
        result_down.set(num)
    else:
        newnum = oldnum + num
        result_down.set(newnum)


# 功能按钮绑定函数，用于式子的组件与隐形的逻辑
def pressCompute(func):
    global lists,isPressFunc,isPressDel
    num = result_down.get()

    # 如果为删除，则显示的数字删除一位，重新显示，然后将结果添加的lists中
    # 同时，将删除指示调整为True，以保证删除后屏幕显示的数值不在其他函数被重新添加到list中
    # 直到遇到其他四则运算符，将指示重置为False，否则equal函数就不能获取后续的显示值
    if func == 'del':
        a = num[0:-1]
        result_down.set(a)
        num = result_down.get()
        #lists.remove(lists.size()-1)
        #del lists[-1]
        lists.append(num)
        isPressDel = True

    elif func == 'AC':
        lists.clear()
        result_down.set('0')
        result_up.set('')
        isPressDel = False
        isPressFunc = False
    else:
        if isPressDel != True:
            lists.append(num)
            print(lists)
        lists.append(func)
        isPressFunc = True
        isPressDel = False  # 一旦出现四则运算，则之前删除指示重置为False


# 等号按钮的绑定函数，使用eval函数进行计算，并将两个结果分别投到屏幕上
def pressEqual():
    global lists,isPressFunc,isPressDel
    # 获取最后一次输入的数值
    num_nd = result_down.get()
    # 如果该数值之前被del功能删除过后（指示值为True），会自动添加进列表，则此时不需要再添加
    # 如果是其他功能的话，则需要将该数值添加进列表
    if isPressDel != True:
        lists.append(num_nd)
    # 使用join函数将单独分离的lists列表合成字符串，其中‘’空字符串代表用来合成时使用的间隔为空
    equation = ''.join(lists)
    # 使用eval函数返回传入字符串的表达式的结果。eval()实现list、dict、tuple与str之间的转化
    resultNum = eval(equation)
    # 将计算结果投至下显示屏，计算表达式投至上显示屏
    result_down.set(resultNum)
    result_up.set(equation)
    # 情况列表
    lists.clear()

root.mainloop()