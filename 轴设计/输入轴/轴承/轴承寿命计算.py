from os import system
from math import *

system("cls")


f_r1 = 2.134*1E3  # N
f_r2 = 4.249*1E3  # N
f_a0 = 935.7716459873701  # N

C = 46.2*1E3  # N
C0 = 30.5*1E3  # N
 # 总轴向力
rel_C = f_a0/C0  # 相对轴向载荷

print(f"fa = {f_a0}")
print(f"相对轴向载荷 fa/C0 = {f_a0/C0}")


# 线性插值(需插值的x坐标, 两端基点坐标)将输出x对应的y坐标
def Linear_interpolation(x,  x0,  y0,  x1, y1):
    return (y0 + ((((x - x0) * y1) - ((x - x0) * y0)) / (x1 - x0)))

e = Linear_interpolation(rel_C, 0.029, 0.40, 0.058, 0.43)
print(f"e = {e}")

# 求派生轴向力
f_d1 = e*f_r1
f_d2 = e*f_r2

print("\n派生轴向力:")
print(f"f_d1 = {f_d1}N")
print(f"f_d2 = {f_d2}N")

# 求轴承轴向力

print("\n轴向力为:")
f_a1 = f_a0+f_d2
f_a2 = f_d2
print(f"f_a1 = {f_a1}\nf_a2 = {f_a2}\n")

# 求径向动载系数
print(f"f_a1/f_r1 = {f_a1/f_r1}")
print(f"f_a2/f_r2 = {f_a2/f_r2}")

fd = 1.1
X1 = 0.44
Y1 = Linear_interpolation(rel_C, 0.029, 1.40, 0.058, 1.30)  # Y1线性插值
X2 = 1
Y2 = 0
print(f"Y1 = {Y1}")

# 求动载荷P
print("\n动载荷P为:")
p1 = fd*(X1*f_r1+Y1*f_a1)
p2 = fd*(X2*f_r2+Y2*f_a2)
print(f"p1 = {p1}N\np2 = {p2}N")

n = 480  # r/min
Lh = (1E6/(60*n))*pow((C/p1), 3)
print(f"Lh = {Lh}")
