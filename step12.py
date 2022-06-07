import matplotlib.pyplot as plt
import numpy as np
import csv

x = np.array([])
y = np.array([])


with open('data.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        x = np.insert(x, len(x), float(row[0]))
        y = np.insert(y, len(y), float(row[1]))

line_x = np.linspace(np.min(x), np.max(x), 10)
line_y = 1.85 * line_x - 0.5
plt.scatter(x, y, color="red")
plt.plot(line_x, line_y)
plt.show()


# y = 1.85x - 0.5 -----> 0.5 - 1.85x + y = 0


class1_x = np.array([])
class1_y = np.array([])
class2_x = np.array([])
class2_y = np.array([])


for x1 in range(20, 60, 2):
    for x2 in range(20, 100, 2):
        if x2 > 1.85 * x1 - 0.5:
            class1_x = np.insert(class1_x, len(class1_x), x1)
            class1_y = np.insert(class1_y, len(class1_y), x2)
        else:
            class2_x = np.insert(class2_x, len(class2_x), x1)
            class2_y = np.insert(class2_y, len(class2_y), x2)

line_x = np.linspace(20, 60, 2)
line_y = 1.85 * line_x - 0.5

plt.scatter(class1_x, class1_y, color="orange")
plt.scatter(class2_x, class2_y, color="green")
plt.plot(line_x, line_y)
plt.show()


# with open( 'data.csv' , newline='' ) as csvfile :
#     myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
#     for row in myreader :
#         cur_x = float(row[0])
#         cur_y = float(row[1])
#
#         if cur_y > 1.85 * cur_x - 0.5:
#             class1_x = np.insert(class1_x, len(class1_x), cur_x)
#             class1_y = np.insert(class1_y, len(class1_y), cur_y)
#         else:
#             class2_x = np.insert(class2_x, len(class2_x), cur_x)
#             class2_y = np.insert(class2_y, len(class2_y), cur_y)
#
# plt.scatter(class1_x, class1_y, color = "orange")
# plt.scatter(class2_x, class2_y, color = "green")
# plt.plot(line_x, line_y)
# plt.show()
