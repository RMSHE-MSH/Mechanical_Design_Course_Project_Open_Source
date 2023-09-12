from math import *

d0 = d2 = 54.1072155408696  # mm
iAxis_T = 97.57034227515148*1E3  # N*mm
cAxis_T = 313.89764489968235*1E3  # N*mm
beta = 14.5454507692722  # °


def gear_force(d, T, beta, alpha=20):
    alpha = alpha*(pi/180)
    beta = beta*(pi/180)

    Ft = (2*T)/d
    Fr = (Ft*tan(alpha))/cos(beta)
    Fa = Ft*tan(beta)
    Fn = Ft/(cos(alpha)*cos(beta))

    return Ft, Fr, Fa, Fn


print("Gear_force = (Ft, Fr, Fa, Fn)")
print(f"Gear0_force = {gear_force(d0,iAxis_T,beta)}")
print(f"Gear2_force = {gear_force(d2,cAxis_T,beta)}")
