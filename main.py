import random
import time
import matplotlib.pyplot as plt


def divide(array):
    if len(array) == 1:
        return array
    left = divide(array[:len(array) // 2])
    right = divide(array[len(array) // 2:])
    return conquer(left, right)


def conquer(left, right):
    new_arr = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_arr.append(left[i])
            i += 1
        else:
            new_arr.append(right[j])
            j += 1
    if i < len(left):
        while i < len(left):
            new_arr.append(left[i])
            i += 1
    if j < len(right):
        while j < len(right):
            new_arr.append(right[j])
            j += 1
    return new_arr


x_coordinate = []
y_coordinate = []
for n in range(1, 900, 100):
    arr = [random.randint(0, 100000) for i in range(n * 100)]
    start = time.time()
    print(divide(arr))
    print("Time taken: ", round(time.time() - start, 6))
    x_coordinate.append(n * 100)
    y_coordinate.append(round(time.time() - start, 6))

plt.plot(x_coordinate, y_coordinate, marker="o")
plt.xlabel("Size")
plt.ylabel("Time")
plt.show()

