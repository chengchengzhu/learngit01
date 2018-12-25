# 第一步：画出图形界面-上部
from tkinter import *

root = Tk() # 创建舞台
# 定义面板的大小
root.geometry('250x380')
root.title('Calculator')

# 定义面板
# Frame：框架，在屏幕上创建一块矩形区域，多作为容器来布局窗体
# bg代表背景颜色background，#dddddd是十六进制表示颜色的一个串
frame_show = Frame(width=300,height=150,bg='#dddddd')
frame_show.pack()

# 定义顶部区域，设置字符串-初始化为0
sv = StringVar()
sv.set('0')

# anchor:定义控件的锚点，西对齐”w”，东对齐”e”，北对齐”n”，南对齐”s”，默认为” center”
# 还有“nw”, “sw”, “se”, “ne”
# Label中的width和height单位不是像素，而是占据字符的位数
# font代表字体
show_label = Label(frame_show,textvariable=sv, \
                  bg='green', width=12, height=1, \
                  font=("黑体", 20, 'bold'), \
                  justify=LEFT, anchor='e')  #用label显示字符串
# padx和pady用于设置框架的外部填充显示，ipadx和ipady用于设置框架的内部显示
show_label.pack(ipadx=5, ipady=5, padx=10, pady=10)
#frame_show.pack()


# 第二步：画出图形界面-下部
# 定义退格函数
def delete():
    # 先用get获取sv的值，然后删掉其最后一位
    sv.set(sv.get()[:-1])

# 定义取反函数
def inverse():
    # 先用get获取sv的值，然后转换为整形，再乘-1
    inverse_value = float(sv.get()) * -1
    sv.set(inverse_value)

# 定义清零函数
def clear():
    global num1, num2, operator
    sv.set('0')
    num1 = ''
    num2 = ''
    operator = ''


# 定义下部按键区域
frame_bord = Frame(width=400, height=350, bg='#cccccc')

button_del = Button(frame_bord, text="←", width=5, height=1, \
               command=delete).grid(row=0, column=1)
button_clear = Button(frame_bord, text='C', width=5, height=1, \
                      command=clear).grid(row=0, column=0)
button_inverse = Button(frame_bord, text='±', width=5, height=1, \
                    command=inverse).grid(row=0, column=2)
button_ce = Button(frame_bord, text='CE', width=5, height=1, \
                   command=clear).grid(row=0, column=3)
'''
考虑以下几种情况：
1. 按下数字
2. 按下操作符号
3，只考虑两个操作数操作，比考虑复杂情况
'''
# 初始化两个数字与运算符
num1 = ''
num2 = ''
operator = ''

def operation(op):
    # 显示运算符
    global num1, num2, operator
    if op in ['+', '-', 'x', '/']:
        # 用于在屏幕上显示并存储
        operator = op
        sv.set(num1 + operator)
    if num2:  # 当num2被赋值时
        rst = 0
        # 由于当num2被赋值时，并不会调用该函数，因此需要在op为“=”时，使用上步四则运算符信息进行运算
        # operator代表用于存储上次调用该函数时的运算符
        if operator == "+":
            rst = float(num1) + float(num2)
        if operator == "-":
            rst = float(num1) - float(num2)
        if operator == "x":
            rst = float(num1) * float(num2)
        if operator == "/":
            rst = float(num1) / float(num2)
        # “=”不用显示在屏幕上，所以用op
        if op == "=":
            # 输出结果，控制显示的数值位数，最多为10位
            sv.set(str(rst)[:10])
            # 将上一步的计算结果赋值给num1，清除num2和operator的
            num1 = str(rst)
            num2 = ''
            operator = ''


# 定义加减乘除四则运算,与等于按钮
b_plus = Button(frame_bord, text='+', width=5, height=2, \
             command=lambda: operation('+')).grid(row=1, column=3)
b_minus = Button(frame_bord, text='-', width=5, height=2, \
             command=lambda: operation('-')).grid(row=2, column=3)
b_times = Button(frame_bord, text='x', width=5, height=2, \
             command=lambda: operation('x')).grid(row=3, column=3)
b_divide = Button(frame_bord, text='/', width=5, height=2, \
             command=lambda: operation('/')).grid(row=4, column=3)
b_equal = Button(frame_bord, text='=', width=5, height=2, \
             command=lambda: operation('=')).grid(row=4, column=2)

# 定义数字改变函数
def change(num):
    '''
    按下一个数字需要考虑两种情况：
    1. 数字属于第一个操作数
    2. 数字属于第二个操作数
    3. 判断是否属于第一个操作数，可以通过operator判断
    '''
    # 加入操作数是None，表明肯定是第一个操作数
    global num1, num2, operator
    # None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False, not Flase即为True
    if not operator:
        num1 = num1 + num
        # 如果是第一个操作数，则只显示第一个操作数
        sv.set(num1)
    else:
        num2 = num2 + num
        # 如果是第二个操作数 ，则应该显示完整的计算式子
        sv.set(num1 + operator + num2)

# 计算器数字区域，形态分布与小键盘数字类似
b_0 = Button(frame_bord, text='0', width=5, height=2, \
             command=lambda: change("0")).grid(row=4, column=0)
b_1 = Button(frame_bord, text='1', width=5, height=2, \
             command=lambda: change("1")).grid(row=3, column=0)
b_2 = Button(frame_bord, text='2', width=5, height=2, \
             command=lambda: change("2")).grid(row=3, column=1)
b_3 = Button(frame_bord, text='3', width=5, height=2, \
             command=lambda: change("3")).grid(row=3, column=2)
b_4 = Button(frame_bord, text='4', width=5, height=2, \
             command=lambda: change("4")).grid(row=2, column=0)
b_5 = Button(frame_bord, text='5', width=5, height=2, \
             command=lambda: change("5")).grid(row=2, column=1)
b_6 = Button(frame_bord, text='6', width=5, height=2, \
             command=lambda: change("6")).grid(row=2, column=2)
b_7 = Button(frame_bord, text='7', width=5, height=2, \
             command=lambda: change("7")).grid(row=1, column=0)
b_8 = Button(frame_bord, text='8', width=5, height=2, \
             command=lambda: change("8")).grid(row=1, column=1)
b_9 = Button(frame_bord, text='9', width=5, height=2, \
             command=lambda: change("9")).grid(row=1, column=2)
b_d = Button(frame_bord, text='.', width=5, height=2, \
             command=lambda: change(".")).grid(row=4, column=1)


frame_bord.pack(padx=10, pady=10)

root.mainloop()