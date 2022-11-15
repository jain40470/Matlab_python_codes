import matplotlib.pyplot as plt
import math


def funci(x, y):
    return (10.0-(10.0)*y)


def func_org(x):

    a = (1.0-math.exp(-10*x))
    return a

# Rk2 method
#  dy/dx = f(x,y)
#  k1 = hf(x,y)
#  k2 = hf(x+h,y+k)
#  y(n+1) = y(n) + (k1+k2)/2


def main():

    y_org = []
    y_cal = []
    x_cal = []

    a = 0
    b = 0.5

    h = 0.01
    # n = (b-a)/h

    x_cal.append(0.0)
    y_cal.append(0.0)
    y_org.append(0.0)

    i = h

    count = 0

    while (i <= b):

        x_cal.append(i)
        y_org.append(func_org(i))

        op = len(y_cal)

        k1 = h*funci(i, y_org[op-1])
        k2 = h*funci(i+h/2, y_org[op-1]+k1/2)
        k3 = h*funci(i+h/2, y_org[op-1]+k2/2)
        k4 = h*funci(i+h, y_org[op-1]+k3)

        y_cal.append(y_cal[op-1]+(k1+2*k2+2*k3+k4)/6)
        i = i + h

        count = count + 1

    print(count)
    plt.plot(x_cal, y_cal, 'r', label="Calculated-RK-4")
    plt.legend()
    plt.plot(x_cal, y_org, 'b', label="EXACT")
    plt.legend()
    plt.show()

    # for i in range(0, len(y_org), 1):

    #     print(y_org[i])


main()
