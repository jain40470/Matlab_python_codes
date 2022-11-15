import matplotlib.pyplot as plt
import math


def funci(x):

    return (x*x-6*x-16)


def main():

    a = 0
    b = 10

    x = [a, b]
    y = [funci(a), funci(b)]

    n = 25
    i = 1

    while n > i:

        d = (0.618)*(x[1]-x[0])

        x_0 = x[0] + d
        x_1 = x[1] - d

        y[0] = funci(x_0)
        y[1] = funci(x_1)

        if y[0] < y[1]:

            x[0] = x_1

        else:

            x[1] = x_0

        i = i + 1

    plt.plot(y, x, 'r')
    plt.show()
    # plt.legend()


main()
