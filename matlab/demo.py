import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 6, 8], 'r', label="plottt")
plt.legend()
plt.plot([1, 2, 3, 4], [1, 4, 20, 10], 'b', label="hiii")
plt.legend()

# plt.ylabel('y-numbers')
# plt.xlabel('x-numbers')


def abc(i):
    return int(1/2)


print("hi")
my_List = []
for i in range(0, 100, 1):
    my_List.append(abc(i))
# plt.plot(my_List)
plt.show()
