from math import *

f_t3 = 11.602801650829043  # KN
f_r3 = 4.362911336817603   # KN
f_a3 = 3.0105102533205064   # KN

[b, h, l, t] = [18, 11, 50, 4.4]  # 键联接尺寸

a = 46.7  # mm
l = ((54/2)+24+22)-a  # mm
lb = (82/2)+20+a  # mm
d = 179.32677150688227  # 大轮分度圆直径
print(f"L = {l}")
print(f"lb = {lb}")
print(f"d = {d}")
print(f"a = {a}")
print(f"AD = {l+l+lb}")

# H面支座反力
# -F_t3*L+F_rh1*2L=0
# -F_t3+F_rh1+F_rh2=0
f_rh1 = (f_t3*l)/(2*l)
f_rh2 = f_t3-f_rh1

# V面支座反力
# F_r3-F_rv2-F_rv1=0
# F_r3*L-F_rv1*2L=0
m_a3 = f_a3*(d/2)
f_rv1 = (m_a3+f_r3*l)/(2*l)
f_rv2 = f_r3-f_rv1

print(f"m_a3 = {m_a3};")
print(f"f_rh1 = {f_rh1};\t f_rh2 = {f_rh2}")
print(f"f_rv1 = {f_rv1};\t f_rv2 = {f_rv2}")

f_r1 = sqrt(f_rv1*f_rv1+f_rh1*f_rh1)
f_r2 = sqrt(f_rv2*f_rv2+f_rh2*f_rh2)

print(f"f_r1 = {f_r1};\t f_r2 = {f_r2}")

M_H_B = f_rh1*l
M_V_B_L = f_rv2*l
M_V_B_R = f_rv1*(2*l-l)

M_A = 0
M_B_L = sqrt(pow(M_V_B_L, 2)+pow(M_H_B, 2))
M_B_R = sqrt(pow(M_V_B_R, 2)+pow(M_H_B, 2))
M_C = 0

print(f"M_H_B = {M_H_B}")
print(f"M_V_B_L = {M_V_B_L}")
print(f"M_V_B_R = {M_V_B_R}")
print(f"\n总弯矩:")
print(f"M_A = {M_A}")
print(f"M_B_L = {M_B_L}")
print(f"M_B_R = {M_B_R}")
print(f"M_C = {M_C}")

# 输出轴转矩
m_t3 = f_t3*(d/2)
print(f"m_t3 = {m_t3}")

# B截面抗弯截面系数
alpha = 0.6
w_b = (pi*pow(d, 3))/32-(b*t*pow(d-t, 2))/(d)
Sigma_ca = sqrt(pow(M_B_R*1E3, 2)+pow(alpha*m_t3*1E3, 2))/w_b
print(f"w_b = {w_b}")
print(f"Sigma_ca = {Sigma_ca}")
