
# 线性插值(需插值的x坐标, 两端基点坐标)将输出x对应的y坐标
def Linear_interpolation(x,  x0,  y0,  x1, y1):
    return (y0 + ((((x - x0) * y1) - ((x - x0) * y0)) / (x1 - x0)))


print(Linear_interpolation(69.812, 40, 1.219, 80, 1.228))
