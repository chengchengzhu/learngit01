
import random
import math

class GameNum():
# 定义字符拼接函数
    def line(self):
        # 定义一个空字符串，用于拼接字符
        str_num = ''
        # 循环前四个随机字母，用ascii码对应的值来随机再转换为字母
        for i in range(4):
            # 随机小写字母的ascii码值
            num = random.randrange(97, 123)
            # 将ascii码值转换成对应的字母
            str_s = chr(num)
            # 依次拼接得到的随机字母
            str_num = str_num + str_s
        # 循环后八个随机数字
        for i in range(8):
            num = random.randrange(0, 10)
            str_num = str_num + str(num)
        # print(str_num)
        return str_num


    def num(self,source,total):
        while 1:
            # input()输入函数，输入的是字符类型，需要强制转换一下
            num = input("请输入一个三位数字，输入-1结束：")
            if num == '-1':
                break
            # if num.isdigit(): #判断是否为纯数字
            #    if 100 <= int(num) <=999:
            #        pass
            # else:
            #    print('请按规定输入')

            '''
            输入一个三位数，与程序随机数比较大小
            1、如果大于程序随机数，分别输出三位数的个位，十位，百位
            2、如果等于程序随机数，提示中奖，记100分
            3、如果小于程序随机数，则将120个字符输入到文本文件中
                （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后八个是数字）
            '''
            # 程序随机数
            random_num = random.randrange(100, 1000)

            if num.isdigit() and 100 <= int(num) <= 999:  # 输入函数返回的是字符类型，不能与整形直接比较，需要强制型转换
                # 判断随机数与输入的数的大小
                num = int(num)
                random_num = int(random_num)
                if num > random_num:
                    # 求百位数字方法是地板除100，或用math.floor()函数
                    bai = num // 100
                    # 求十位数字方法是先把三位数字取100的余数，再地板除10
                    shi = num % 100 // 10
                    # 求个位数字方法是取10的余数
                    ge = num % 10
                    print('输入的数字大于随机数',random_num)
                    print('这个三位数的个位是{}，十位是{}，百位是{}'.format(ge, shi, bai))
                if num == random_num:
                    source += 100
                    print('你中奖了，目前的分数为', source)
                if num < random_num:
                    print('输入的数字小于随机数', random_num)
                    # 由于120个字符每行12个，可知只需存入10行就可以
                    for i in range(10):
                        line = GameNum()
                        str_line = line.line()
                        # print(str_line)
                        # 执行文件存入操作
                        with open("str_num.txt", "a") as f:  # 不需要close，写完自动关闭
                            f.write(str_line + '\n')

            else:
                print('请按规定输入')

if __name__ == '__main__':  # 对于单个py文件内部，main=main，对于其他要import的py文件，main=其文件名
    # 定义一个变量用于存储初始分数
    source = 0
    # 定义一个变量用于累积输入了多少次
    total = 0
    # 实例化类
    num = GameNum()
    num.num(source,total)



