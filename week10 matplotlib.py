import matplotlib.pyplot as plt
import numpy as np


def power2(n):
    return n**2

array_size = int(input())
plot_style = input()
array_list = [i for i in range(array_size-1)]

xpoints = np.array([array_list])
ypoints = [i**2 for i in array_list]

if plot_style == "scatter":
    plt.scatter(xpoints, ypoints)
elif plot_style == "bar":
    catergories = input("categories").split()
    val = input("values: ").split()
    plt.bar(catergories, val)
else:
    plt.plot(xpoints, ypoints)
plt.show()
