# 定义TongLao类
class TongLao:
    # 定义构造函数,类实例化时即调用
    def __init__(self, hp, power):
        # 定义实例属性，以”self.变量名“的方式定义
        # 不加self.为普通属性，是方法内的局部变量，只在当前的方法内有用
        # 要使其他方法也可以用，前面必须加self.
        self.hp = hp
        self.power = power

    # 定义类方法，调用类方法，必须先实例化
    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        self.power = self.power * 10
        self.hp = self.hp / 2

        # 一回合对打
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        # 比较双方血量
        if self.hp > enemy_hp:
            print(f"我的血量为{self.hp}，我的攻击力为{self.power}")
            print(f"敌人的血量为{enemy_hp}，敌人的攻击力为{enemy_power}")
            print("我赢了")
        elif self.hp < enemy_hp:
            print(f"我的血量为{self.hp}，我的攻击力为{self.power}")
            print(f"敌人的血量为{enemy_hp}，敌人的攻击力为{enemy_power}")
            print("我输了")
        else:
            print(f"我的血量为{self.hp}，我的攻击力为{self.power}")
            print(f"敌人的血量为{enemy_hp}，敌人的攻击力为{enemy_power}")
            print("平局")




