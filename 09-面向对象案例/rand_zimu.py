
class GameZiMu():
    #rand_zimu.py

    # 打印字母A
    # 控制行
    def a(self):
        for i in range(1,6):
            #判断开始输入的位置
            for k in range(6-i):
                print(' ',end='')
            # 控制列
            for j in range(1,i+1):
                if i==1 or i==3 or j==1 or j==i:
                    print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

    #打印字母b
    #控制行
    def b(self):
        for i in range(1,4):
            #判断开始输入的位置
            for j in range(1,4):
                if i==1 or i==4 or j==1:
                    if j<3:
                        print('*',end=' ')
                elif j==3:
                    if i==2 or i==3:
                        print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()
        for i in range(1,5):
            #判断开始输入的位置
            for j in range(1,4):
                if i==1 or i==4 or j==1:
                    if j<3:
                        print('*',end=' ')
                elif j==3:
                    if i==2 or i==3:
                        print('*',end=' ')
                else:
                    print(' ',end=' ')

    def d(self):
        for i in range(1,5):
            #判断开始输入的位置
            for j in range(1,4):
                if i==1 or i==4 or j==1:
                    if j<3:
                        print('*',end=' ')
                elif j==3:
                    if i==2 or i==3:
                        print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

    #打印字母C
    def c(self):
        for i in range(1,5):
            #判断开始输入的位置
            for j in range(1,4):
                if j==1:
                    if i==2 or i==3:
                        print('*',end=' ')
                elif i==1 or i==4:
                    if j==1:
                        print(' ',end=' ')
                    else:
                        print('*',end=' ')
                else:
                    print(' ',end=' ')
            print()

