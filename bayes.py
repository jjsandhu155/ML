
import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt


set1 = []
set2 = []
set3 = []
set4 = []
n0 = 0
n1 = 0

with open('SocialNetworkAds.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        break
    for row in myreader:
        if row[2] == '0':
            set1.append(int(row[0]))
        if row[2] == '1':
            set2.append(int(row[0]))
        if row[2] == '0':
            set3.append(int(row[1]))
        if row[2] == '1':
            set4.append(int(row[1]))

        if row[2] == '0':
            n0 += 1
        if row[2] == '1':
            n1 += 1

arr1x = np.array([])
arr1y = np.array([])
arr2x = np.array([])
arr2y = np.array([])

P_output0 = n0/(n0+n1)
P_output1 = n1/(n0+n1)

for x1 in range(20, 60, 2):
    for x2 in range(15000, 150000, 5000):
        P_x1_output0 = (1.0 / (statistics.stdev(set1) * np.sqrt(2 * np.pi))) * \
            np.exp(-((x1 - statistics.mean(set1)) * 2) /
                   (2 * statistics.stdev(set1) * 2))
        P_x2_output0 = (1.0 / (statistics.stdev(set3) * np.sqrt(2 * np.pi))) * \
            np.exp(-((x2 - statistics.mean(set3)) * 2) /
                   (2 * statistics.stdev(set3) * 2))
        P_x1_output1 = (1.0 / (statistics.stdev(set2) * np.sqrt(2 * np.pi))) * \
            np.exp(-((x1 - statistics.mean(set2)) * 2) /
                   (2 * statistics.stdev(set2) * 2))
        P_x2_output1 = (1.0 / (statistics.stdev(set4) * np.sqrt(2 * np.pi))) * \
            np.exp(-((x2 - statistics.mean(set4)) * 2) /
                   (2 * statistics.stdev(set4) * 2))

        T0 = P_output0 * P_x1_output0 * P_x2_output0
        T1 = P_output1 * P_x1_output1 * P_x2_output1

        P_first = T0/(T0 + T1)
        P_second = T1/(T0 + T1)

        if P_first > P_second:
            arr1x = np.insert(arr1x, len(arr1x), x1)
            arr1y = np.insert(arr1y, len(arr1y), x2)
        else:
            arr2x = np.insert(arr2x, len(arr2x), x1)
            arr2y = np.insert(arr2y, len(arr2y), x2)
plt.scatter(arr1x, arr1y, color="red", label='Not Purchased')
plt.scatter(arr2x, arr2y, color="green", label='Purchased')
plt.legend(['Not Purchased', 'Purchased'])
plt.show()
