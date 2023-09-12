from os import system
from math import sqrt

system("cls")


f_r1 = 9334.87662901257  # N
f_r2 = 6508.515018721893  # N
f_a3 = 3.0105102533205064*1E3  # N

print(f"f_r1 = {f_r1}\nf_r2 = {f_r2}")

e = 1.14
f_d1 = e*f_r1
f_d2 = e*f_r2

print(f"f_d2-f_a3 = {f_d2-f_a3}")
print(f"f_d1+f_a3 = {f_d1+f_a3}")

f_a1 = f_d1
f_a2 = f_d1+f_a3

print(f"f_d1 = {f_d1}\nf_d2 = {f_d2}")
print(f"f_a1 = {f_a1}\nf_a2 = {f_a2}")

print(f_a1/f_r1)
print(f_a2/f_r2)

fd = 1.1
X1 = 1
Y1 = 0
X2 = 0.35
Y2 = 0.57

p1 = fd*(X1*f_r1+Y1*f_a1)
p2 = fd*(X2*f_r2+Y2*f_a2)
print(f"p1 = {p1}\np2 = {p2}")

n = 43.65392724806272 #r/min
C = 56000
Lh = (1E6/(60*n))*pow((C/p2), 3)
print(f"Lh = {Lh}")
