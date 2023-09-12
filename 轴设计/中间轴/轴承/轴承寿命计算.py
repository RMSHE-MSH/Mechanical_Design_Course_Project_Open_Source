from os import system
from math import *

system("cls")

#7309B

#支座反力
f_r1 = 9652.112797169628  # N
f_r2 = 2088.60582956413  # N
#齿轮轴向力
f_a1 = 935.7716459873701  # N
f_a2 = 3010.5102533205068  # N

C = 59.5*1E3  # N
C0 = 39.8*1E3  # N

fa = f_a2-f_a1  # 总轴向力(方向为-x)
rel_C = fa/C0  # 相对轴向载荷

print(f"fa = {fa}")
print(f"相对轴向载荷 fa/C0 = {fa/C0}")


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
print(f"\nf_d2-fa = {f_d2-fa}")
print(f"f_d1+fa = {f_d1+fa}")

print("\n轴向力为:")
f_a1 = f_d1
f_a2 = f_d1+fa
print(f"f_a1 = {f_a1}\nf_a2 = {f_a2}\n")

# 求径向动载系数
print(f"f_a1/f_r1 = {f_a1/f_r1}")
print(f"f_a2/f_r2 = {f_a2/f_r2}")

fd = 1.1
X1 = 1
Y1 = 0
X2 = 0.44
Y2 = Linear_interpolation(rel_C, 0.029, 1.40, 0.058, 1.30)  # Y2线性插值
print(f"Y2 = {Y2}")

# 求动载荷P
print("\n动载荷P为:")
p1 = fd*(X1*f_r1+Y1*f_a1)
p2 = fd*(X2*f_r2+Y2*f_a2)
print(f"p1 = {p1}N\np2 = {p2}N")

n = 144.7545684221058  # r/min
Lh = (1E6/(60*n))*pow((C/p1), 3)
print(f"Lh = {Lh}")
