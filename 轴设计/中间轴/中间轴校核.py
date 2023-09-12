from math import *
from os import system
system("cls")

f_t1 = 3606.555661747266  # N
f_r1 = 1356.1450981433054  # N
f_a1 = 935.7716459873701  # N

f_t2 = 11602.801650829044  # N
f_r2 = 4362.911336817603  # N
f_a2 = 3010.5102533205068  # N

[b, h, l, t] = [18, 11, 50, 4.4]  # 键联接尺寸

a = 42
L1 = 36
Lc = 192.5
L2 = 36.5
d1 = 179.326771506882  # 大齿轮分度圆直径
d2 = 54.1072155408696  # 小齿轮分度圆直径

# H面支座反力
f_rh1 = (-f_t1*L1+f_t2*(L1+Lc))/(L1+Lc+L2)
f_rh2 = f_rh1-f_t2+f_t1

print(f"\nH面支座反力")
print(f"f_rh1 = {f_rh1}N")
print(f"f_rh2 = {f_rh2}N")

# H面弯矩方程
print(f"\nH面弯矩分布")
M_H_A = f_rh2*0
M_H_B_L = f_rh2*L1
M_H_B_R = f_rh2*L1-f_t1*(L1-L1)
M_H_C_L = f_rh2*(L1+Lc)-f_t1*((L1+Lc)-L1)
M_H_C_R = -f_rh1*((L1+Lc+L2)-(L1+Lc))
M_H_D = -f_rh1*((L1+Lc+L2)-(L1+Lc+L2))

print(f"M_H_A = {M_H_A}N*mm")
print(f"M_H_B_L = {M_H_B_L}N*mm")
print(f"M_H_B_R = {M_H_B_R}N*mm")
print(f"M_H_C_L = {M_H_C_L}N*mm")
print(f"M_H_C_R = {M_H_C_R}N*mm")
print(f"M_H_D = {M_H_D}N*mm")

# V面支座反力
m_a1 = f_a1*(d1/2)
m_a2 = f_a2*(d2/2)
f_rv1 = (f_r1*L1+m_a1-m_a2+f_r2*(L1+Lc))/(L1+Lc+L2)
f_rv2 = f_r1+f_r2-f_rv1

print(f"\nV面支座反力")
print(f"f_rv1 = {f_rv1}N")
print(f"f_rv2 = {f_rv2}N")

print(f"\nV面弯矩分布")
M_V_A = f_rv2*0
M_V_B_L = f_rv2*L1
M_V_B_R = f_rv2*L1-f_r1*(L1-L1)+m_a1
M_V_C_L = f_rv2*(L1+Lc)-f_r1*((L1+Lc)-L1)+m_a1
M_V_C_R = f_rv1*((L1+Lc+L2)-(L1+Lc))
M_V_D = f_rv1*((L1+Lc+L2)-(L1+Lc+L2))

print(f"M_V_A = {M_V_A}N*mm")
print(f"M_V_B_L = {M_V_B_L}N*mm")
print(f"M_V_B_R = {M_V_B_R}N*mm")
print(f"M_V_C_L = {M_V_C_L}N*mm")
print(f"M_V_C_R = {M_V_C_R}N*mm")
print(f"M_V_D = {M_V_D}N*mm")


print(f"\n总支座反力")
f_r1 = sqrt(pow(f_rv1, 2)+pow(f_rh1, 2))
f_r2 = sqrt(pow(f_rv2, 2)+pow(f_rh2, 2))
print(f"f_r1 = {f_r1}N")
print(f"f_r2 = {f_r2}N")

print(f"\n总弯矩分布")
M_A = sqrt(pow(M_H_A, 2)+pow(M_V_A, 2))
M_B_L = sqrt(pow(M_H_B_L, 2)+pow(M_V_B_L, 2))
M_B_R = sqrt(pow(M_H_B_R, 2)+pow(M_V_B_R, 2))
M_C_L = sqrt(pow(M_H_C_L, 2)+pow(M_V_C_L, 2))
M_C_R = sqrt(pow(M_H_C_R, 2)+pow(M_V_C_R, 2))
M_D = sqrt(pow(M_H_D, 2)+pow(M_V_D, 2))

print(f"M_A = {M_A}N*mm")
print(f"M_B_L = {M_B_L}N*mm")
print(f"M_B_R = {M_B_R}N*mm")
print(f"M_C_L = {M_C_L}N*mm")
print(f"M_C_R = {M_C_R}N*mm")
print(f"M_D = {M_D}N*mm")

# 扭矩为
print(f"\n扭矩分布")
T = f_t2*(d2/2)
print(f"T = {T}N*mm")

# 第三强度理论校核
# 抗弯截面系数
C_d = 48.75
W_C = (pi*pow(C_d, 3))/32
print(f"W_C = {W_C}mm^3")

alpha = 0.6
Sigma_ca = sqrt(pow(M_C_L, 2)+pow(alpha*T, 2))/W_C
print(f"Sigma_ca = {Sigma_ca}MPa")
