from sklearn import decomposition
import numpy as np
import matplotlib.pyplot as plt
# import numpy as np
import statistics
import csv

# x = np.array([])
# y = np.array([])
#
# with open( 'data.csv' , newline='' ) as csvfile :
#     myreader = csv.reader( csvfile , delimiter=',' , quotechar='"' )
#     for row in myreader :
#         x = np.insert(x, len(x), float(row[0]))
#         y = np.insert(y, len(y), float(row[1]))

x = []
y = []

with open('data.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        x.append(float(row[0]))
        y.append(float(row[1]))


x_mean = statistics.mean(x)
x_std = statistics.stdev(x)
y_mean = statistics.mean(y)
y_std = statistics.stdev(y)

x_norm = []
y_norm = []

normalized_data = []

for elem in x:
    x_norm.append((elem - x_mean)/x_std)

for elem in y:
    y_norm.append((elem - y_mean)/y_std)

for index in range(len(x_norm)):
    cur_list = []
    cur_list.append(x_norm[index])
    cur_list.append(y_norm[index])
    normalized_data.append(cur_list)


#
#
#
X = np . array(normalized_data)
#
pca = decomposition . PCA(n_components=2)
#
pca . fit(X)
#
print(pca . components_)
print(pca . explained_variance_)
print(pca . explained_variance_ratio_)
#


# print(pca.components_[0])
# print(X[:, 0])
# print(X[:, 1])
#
#
# plt.scatter(X[:, 0], X[:, 1])
# plt.axis('equal')
#
# line_x = np.linspace(-2, 2, 50)
# line_y = -1 * line_x
# plt.plot(line_x, line_y)
#
# line_x = np.linspace(-2, 2, 50)
# line_y = line_x
# plt.plot(line_x, line_y)
#
#
# plt.show()


first_scores = []
second_scores = []

for index in range(len(X[:, 0])):
    cur_x = X[:, 0][index]
    cur_y = X[:, 1][index]
    first_scores.append(
        np.dot([cur_x, cur_y], [pca.components_[0][0], pca.components_[0][1]]))
    second_scores.append(
        np.dot([cur_x, cur_y], [pca.components_[1][0], pca.components_[1][1]]))

plt.scatter(x, first_scores)
plt.show()

plt.scatter(x, second_scores)
plt.show()

plt.scatter(y, first_scores)
plt.show()

plt.scatter(y, second_scores)
plt.show()


# for elem in x:
#     x_norm = np.insert(x_norm, len(x_norm), (elem - x_mean)/x_std)
#
# for elem in y:
#     y_norm = np.insert(y_norm, len(y_norm), (elem - y_mean)/y_std)
