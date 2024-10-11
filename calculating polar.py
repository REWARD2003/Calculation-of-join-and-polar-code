import math
def calculating_polar():
    Y1 = float(input("enter first Y point coordinate:"))
    X1 = float(input("enter first X point coordinate:"))
    d = float(input("enter distance between the points:"))
    q = float(input("enter direction between 2 points:"))
    Y = Y1 + d*math.sin(q)
    X = X1 + d*math.cos(q)
    print(Y)
    print(X)
calculating_polar()
