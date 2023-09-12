from math import *


A0 = 103

iAxis_P = 4.904059088175153
iAxis_n = 480

cAxis_P = 4.757918127347533
cAxis_n = 144.7545684221058

oAxis_P = 4.342857142857143
oAxis_n = 43.65392724806272

iAxis_d_min = A0*pow(iAxis_P/iAxis_n, 1.0/3.0)
iAxis_d_min = iAxis_d_min + 0.07*iAxis_d_min

cAxis_d_min = A0*pow(cAxis_P/cAxis_n, 1.0/3.0)
cAxis_d_min = cAxis_d_min + 0.07*cAxis_d_min

oAxis_d_min = A0*pow(oAxis_P/oAxis_n, 1.0/3.0)
oAxis_d_min = oAxis_d_min + 0.05*oAxis_d_min

print(f"iAxis_d_min = {iAxis_d_min} mm")
print(f"cAxis_d_min = {cAxis_d_min} mm")
print(f"oAxis_d_min = {oAxis_d_min} mm")
