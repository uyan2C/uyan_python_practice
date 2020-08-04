from tonglao import TongLao
from xuzhu import XuZhu


#创建Tonglao类的实例
#实例化的同时，给构造函数传参
# 使用关键字传参
tl = TongLao(hp=1000, power=100)
xz = XuZhu(hp=2000, power=200)

#调用方法
tl.see_people("WYZ")
tl.see_people("李秋水")
tl.see_people("丁春秋")
tl.fight_zms(enemy_hp=700, enemy_power=300)
xz.fight_zms(enemy_hp=2600, enemy_power=300)


