from math import *


class work:
    D = 350/1000  # (m)
    linear_v = 0.8  # (m/s)
    T = 950  # (N*m)
    efficiency = 0.96

    angular_v = linear_v / (D*0.5)  # (rad/s)
    P = (T * angular_v)/1000  # (KW)
    n = (60*angular_v)/(2*pi)  # (r/min)


class coupling:
    efficiency = 0.98  # 联轴器效率


class bearing:
    # 角接触球轴承
    Num = 3  # 轴承对数
    efficiency = 0.99  # 一对轴承的效率


class gear:
    Num = 2  # 齿轮对数
    efficiency = 0.98  # 圆柱齿轮副效率
    i = None  # 传动比


class Vbelt:
    efficiency = 0.925  # V带传动效率
    i = 2  # 传动比


# 传动总效率
Total_Efficiency = work.efficiency*coupling.efficiency*pow(bearing.efficiency, bearing.Num)*pow(gear.efficiency, gear.Num)*Vbelt.efficiency


class motor:
    # 同步转速1000r/min, 6级
    name = "Y132M2-6"
    P0 = 5.5  # 额定功率(kw)
    Pr = work.P/Total_Efficiency  # 工作机所需的电动机功率(kw)
    n = 960  # (r/min)
    T0 = (9550*Pr)/n  # (N*m)


# 理论总传动比
Total_i = motor.n/work.n
gear.i = sqrt(Total_i/Vbelt.i)


print(f"work.angular_v = {work.angular_v} rad/s")
print(f"work.P = {work.P} kw")
print(f"work.n = {work.n} r/min")
print(f"Total_Efficiency = {Total_Efficiency}")
print(f"motor.Pr = {motor.Pr} kw")
print(f"理论总传动比 Total_i = {Total_i}")
print(f"Vbelt.i = {Vbelt.i}")
print(f"gear.i = {gear.i}")


# 计算传动装置的运动和动力参数
class iAxis:
    efficiency = Vbelt.efficiency*bearing.efficiency
    n = motor.n/Vbelt.i  # 轴转速
    P = motor.Pr*efficiency  # 轴功率
    T = motor.T0*Vbelt.i*efficiency  # 轴扭矩


class cAxis:
    efficiency = gear.efficiency*bearing.efficiency
    n = iAxis.n/gear.i  # 轴转速
    P = iAxis.P*efficiency  # 轴功率
    T = iAxis.T*gear.i*efficiency  # 轴扭矩


class oAxis:
    efficiency = gear.efficiency*bearing.efficiency*coupling.efficiency*work.efficiency
    n = cAxis.n/gear.i  # 轴转速
    P = cAxis.P*efficiency  # 轴功率
    T = cAxis.T*gear.i*efficiency  # 轴扭矩


print(f"\niAxis.n = {iAxis.n} r/min")
print(f"iAxis.P = {iAxis.P} kw")
print(f"iAxis.T = {iAxis.T} N*m")
print(f"cAxis.n = {cAxis.n} r/min")
print(f"cAxis.P = {cAxis.P} kw")
print(f"cAxis.T = {cAxis.T} N*m")
print(f"oAxis.n = {oAxis.n} r/min")
print(f"oAxis.P = {oAxis.P} kw")
print(f"oAxis.T = {oAxis.T} N*m")
