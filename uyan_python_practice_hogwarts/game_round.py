'''
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
'''

#定义函数，函数名为fight
def fight():
    #定义四个变量，存储我和对方的血量和攻击力
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200
    #对打多轮，谁的血量先为0，那么谁就输了

    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        #谁的血量先为0，谁救输了
        if my_hp <= 0:
            print(f"我的血量为：{my_hp}")
            print(f"你的血量为：{enemy_hp}")
            print("我输了。")
            #跳出循环
            break
        elif enemy_hp <= 0:
            print(f"我的血量为：{my_hp}")
            print(f"你的血量为：{enemy_hp}")
            print("你输了。")
            break


#调用函数，函数名为fight
fight()


