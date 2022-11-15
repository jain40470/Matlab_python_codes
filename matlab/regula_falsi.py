import matplotlib.pyplot as plt
import math


def funci(x):

    a = (math.pow(2, x)-5*x+2)
    return a


def main():

    toler = 0.0001

    a = 0
    b = 1

    count = 0

    while ((abs(funci(a)) > toler and abs(funci(b)) > toler) and count < 100):

        f_a = funci(a)
        f_b = funci(b)

        c = a - ((b-a)*(f_a))/(f_b-f_a)

        f_c = funci(c)

        if (f_a*f_c < 0):
            b = c
        else:
            a = c

        count = count + 1
    print(b)


main()
