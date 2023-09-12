
#输出轴与齿轮
T = 1040.346480238948  # N*m
[b, h, l, t] = [18, 11, 50, 4.4]
work_l = 1.5*l  # mm
d = 62  # mm

sigma_bs = (4000*T)/(h*work_l*d)

print(sigma_bs)

#输出轴与联轴器
Tl = 1040.346480238948  # N*m
[b, h, l] = [14, 9, 70]
work_l = 1.5*(l-b)  # mm
d = 50  # mm

sigma_bs = (4000*T)/(h*work_l*d)

print(sigma_bs)
