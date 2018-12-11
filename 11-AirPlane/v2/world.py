import tkinter
import time
import random as rd

'''
蜜蜂从上向下运动
可以通过键盘左右控制
'''

step = (0,10)
direction = (1,1)

x = 0
y = 10

def set_right(e):
    global x
    x += 20

def set_left(e):
    global x
    x -= 20

root_window = tkinter.Tk()
root_window.title('bjtlxy')

root_window.bind('<Key-Left>',set_left)
root_window.bind('<Key-Right>',set_right)
root_window.resizable(width=False,height=False)

#创建画布
window_canvas = tkinter.Canvas(root_window,
                               width=480,
                               height=600)

def main():
    # 创建开始界面



root_window.mainloop()



