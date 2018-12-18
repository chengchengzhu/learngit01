from tkinter import * #导入tkinter库
root =Tk() #给窗体
root.title('calculator') #设置窗体名字
frm=Frame(root,bg='pink') #新建框架
frm.pack(expand = YES,fill = BOTH) #放置框架
display=StringVar()
e=Entry(frm,textvariable=display) #添加输入框
e.grid(row=0,column=0,sticky=N,columnspan=4,rowspan=2) #放置输入框位置

def print_jia():
    e.insert(INSERT,'+')
def print_jian():
    e.insert(INSERT,'-')
def print_cheng():
    e.insert(INSERT,'*')
def print_chu():
    e.insert(INSERT,'/')
def print_dengyu():
    e.insert(INSERT,'=')


Button(frm,text='1',width=3,bg='yellow',command= lambda :e.insert(INSERT,'1')).grid(row=2,column=0,sticky=W) #设置按钮，lambda为匿名函数
Button(frm,text='2',width=3,bg='yellow',command= lambda :e.insert(INSERT,'2')).grid(row=2,column=1)
Button(frm,text='3',width=3,bg='yellow',command= lambda :e.insert(INSERT,'3')).grid(row=2,column=2)
Button(frm,text='4',width=3,bg='yellow',command= lambda :e.insert(INSERT,'4')).grid(row=3,column=0,sticky=W)
Button(frm,text='5',width=3,bg='yellow',command= lambda :e.insert(INSERT,'5')).grid(row=3,column=1)
Button(frm,text='6',width=3,bg='yellow',command= lambda :e.insert(INSERT,'6')).grid(row=3,column=2)
Button(frm,text='7',width=3,bg='yellow',command= lambda :e.insert(INSERT,'7')).grid(row=4,column=0,sticky=W,rowspan=2)
Button(frm,text='8',width=3,bg='yellow',command= lambda :e.insert(INSERT,'8')).grid(row=4,column=1,rowspan=2)
Button(frm,text='9',width=3,bg='yellow',command= lambda :e.insert(INSERT,'9')).grid(row=4,column=2,rowspan=2)
Button(frm,text='/',width=4,bg='white',command=print_chu).grid(row=5,column=3,sticky=E)
Button(frm,text='*',width=4,bg='white',command=print_cheng).grid(row=4,column=3,sticky=E)
Button(frm,text='-',width=4,bg='white',command=print_jian).grid(row=3,column=3,sticky=E)
Button(frm,text='+',width=4,bg='white',command=print_jia).grid(row=2,column=3,sticky=E)
Button(frm,text='=',width=4,bg='white',command= lambda :cal(display)).grid(row=6,column=3,sticky=E)
Button(frm,text='clear',width=3,bg='red',command= lambda :display.set('')).grid(row=6,column=0,sticky=W)
Button(frm,text='0',width=3,bg='red',command= lambda :e.insert(INSERT,'0')).grid(row=6,column=2)
Button(frm,text='.',width=3,bg='red',command= lambda :e.insert(INSERT,'.')).grid(row=6,column=1)

def cal(display): #eval函数将字符串转化为表达式
    display.set(eval(display.get()))

print('OK')
root.mainloop() #让程序一直循环