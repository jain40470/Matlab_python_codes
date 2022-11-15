import matplotlib.pyplot as plt
# original function

# (x-y)^4 + 2*x^2 + y*y - x + 2*y

import math


def funci_x(x, y):

    a = (4*pow(x-y, 3)-1+4*x)

    return a


def funci_y(x, y):
    a = (-4*pow(x-y, 3)+2*y+2)
    return a


def main():

    iter = 100
    tol = 1

    i = 0

    x = [1]
    y = [1]

    while (i < iter and tol > 0.001):

        temp_x = x[len(x)-1]
        temp_y = y[len(y)-1]

        a1 = x[len(x)-1] - 0.05*funci_x(temp_x, temp_y)
        b1 = y[len(y)-1] - 0.05*funci_y(temp_x, temp_y)

        x.append(a1)
        y.append(b1)

        tol = min(abs(funci_x(temp_x, temp_y)), abs(funci_y(temp_x, temp_y)))
        i = i + 1

    plt.plot(x, y, 'r')
    plt.show()


main()
