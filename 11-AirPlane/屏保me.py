import random
import tkinter
import tkinter.messagebox


class RandomBall():
    '''
    单个球定义、运动的类
    '''
    def __init__(self, root_canvas, width, height):
        '''
        参数说明：
        canvas：从ScreenSaver类中传入的画布
        width，height：从SS类中传入的宽高，即屏幕宽高
        '''

        # 将传入变量赋为RB类的属性
        self.canvas = root_canvas
        self.width = width
        self.height = height

        # 随机生成球的中心坐标
        self.xcenter = random.randint(100, width-100)
        self.ycenter = random.randint(100, height-100)
        # 随机生成球的运动速度
        self.xvelocity = random.randint(8,16)
        self.yvelocity = random.randint(8,16)
        # 计算球的半径
        self.radius = random.randint(60, 100)
        # 利用十六进制随机数与lambda表达式生成球的颜色
        # RGB表示法：三个数字，每个数字的值是0-255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，直接用英文单词表示也可以，比如red，green
        color = lambda : random.randint(0,255)
        self.color = '#%02x%02x%02x' % (color(),color(),color())

    # 创建球的函数
    def create_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球
        '''
        # tkinter没有画圆形函数
        # 只有一个画椭圆函数，画椭圆需要定义两个坐标，
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        # 求两个坐标的方法是，已知圆心的坐标，则圆心坐标减去半径能求出
        # 左上角坐标，加上半径能求出右下角坐标(向右x为正，向下y为正)
        xleftup = self.xcenter - self.radius
        yleftup = self.ycenter - self.radius
        xrightdown = self.xcenter + self.radius
        yrightdown = self.ycenter + self.radius
        # 创建球
        self.item = self.canvas.create_oval(xleftup,yleftup,
                                            xrightdown,yrightdown,
                                            fill=self.color,
                                            outline=self.color)

    # 球运动的函数
    def move_ball(self):
        # 计算球移动后的中心点坐标
        self.xcenter += self.xvelocity
        self.ycenter += self.yvelocity
        # 当球与边框发生碰撞时，需要进行回弹操作，即对应方向的速度取负
        if self.xcenter + self.radius >= self.width:
            self.xvelocity = - self.xvelocity
        if self.xcenter - self.radius <= 0:
            self.xvelocity = - self.xvelocity
        if self.ycenter + self.radius >= self.height:
            self.yvelocity = - self.yvelocity
        if self.ycenter - self.radius <= 0:
            self.yvelocity = - self.yvelocity
        # 在canvas上移动球,前提是create_ball已经调用
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)



class ScreenSaver():
    '''
    屏保定义类
    程序启动
    '''
    def __init__(self):
        # 创建球存储列表
        self.balls = []
        # 随机生成球的数量
        self.num = random.randint(10,20)

        # 利用tkinter生成root窗口
        self.root = tkinter.Tk()
        # 获取屏幕宽、高尺寸
        root_w, root_h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # 取消边框
        self.root.overrideredirect(1)
        # 绑定退出函数与相应动作
        self.root.bind('<Motion>', self.myquit)
        self.root.bind('<Key>', self.myquit)
        self.root.bind('<Any-Button>', self.myquit)

        # 创建画布，配置尺寸与颜色属性
        self.canvas = tkinter.Canvas(self.root, width=root_w, height=root_h)
        self.canvas.pack()

        # 利用循环与RandomBall类在画布上画球，并append到列表中
        for i in range(self.num):
            ball = RandomBall(self.canvas, width=root_w, height=root_h)
            ball.create_ball()
            self.balls.append(ball)

        # 调用球运动函数
        self.run_screen_saver()
        # 启用tkinter时间消息循环mainloop
        self.root.mainloop()

    # 球运动函数
    def run_screen_saver(self):
        # 循环实例化的ball调用move_ball函数
        for ball in self.balls:
            ball.move_ball()
        # 使用after实现递归，通过不断调用各球的move_ball函数，实现位置刷新
        self.root.after(50, self.run_screen_saver)

    # 停止运行
    # 此处e只是利用了事件处理机制,际上并不关心事件的类型
    def myquit(self, e):
        # 扩展：
        # 此屏保程序扩展成，一旦捕获事件，则判断屏保不退出
        # 显示一个Button，Button上显示事件类型，点击Button后屏保才退出
        if tkinter.messagebox.askokcancel("彩球碰撞", '确定退出？'):
            self.root.destroy()
        else:
            pass
        #self.root.Button(self.root, )
        #self.root.destroy()

    def end(self):
        self.root.destroy()


if __name__ == '__main__':
    # 启动屏保
    ScreenSaver()