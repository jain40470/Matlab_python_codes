import matplotlib.pyplot as plt
import math


def funci(x):

    return (math.pow(2, x)-5*x+2)


def deri_funci(x):

    return (math.log(2)*(math.pow(2, x))-5)


def main():

    toler = 0.0001

    a = 0
    b = 1

    c = (b-a)/2

    count = 0

    while (abs(funci(c)) > toler and count < 100):

        c = c - funci(c)/deri_funci(c)
        count = count + 1

    print(c)


main()
