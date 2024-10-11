import math
def calculating_Join():
    Y2 = float(input("enter coordinate of Y2:"))
    Y1 = float(input("enter coordinate of Y1:"))
    DY = Y2 - Y1
    print(DY)
    X2 = float(input("enter coodinate of X2:"))
    X1 = float(input("enter coodinate of X1:"))
    DX = X2 - X1
    print(DX)
    Distance =(math.sqrt((DY ** 2) + (DX ** 2)))# distance in metres
    print(Distance)
    Direction = math.degrees(math.tanh(DY / DX))# Direction in degrees minutes and seconds
    print(Direction)
    if DY > 0 and DX > 0:
        print(Direction)
    elif DY < 0 and DX < 0:
        print(Direction + 180.0)
    if DY > 0 and DX < 0:
        print(180.0 - Direction)
    else:
        print(Direction + 360.0)
calculating_Join()
