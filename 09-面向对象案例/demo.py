import rand_math
import rand_zimu

print('请选择游戏(输入1或2)\n1.数字游戏\n2.字母游戏')
game = input('输入1或2：')
if game == '1':
    game_num = rand_math.GameNum()
    game_num.num(0,0)
elif game == '2':
    game_zimu = rand_zimu.GameZiMu()
    game_zimu.a()
else:
    print('输入错误')










