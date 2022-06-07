import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np


set1 = []
set2 = []
set3 = []
set4 = []

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

print(len(set1) + len(set2) + len(set3) + len(set4))
print(min(min(set1), min(set2)))
print(max(max(set1), max(set2)))
print(min(min(set3), min(set4)))
print(max(max(set3), max(set4)))

print(statistics.mean(set1))
print(statistics.stdev(set1))
print()

print(statistics.mean(set2))
print(statistics.stdev(set2))
print()

print(statistics.mean(set3))
print(statistics.stdev(set3))
print()

print(statistics.mean(set4))
print(statistics.stdev(set4))
print()


plt.hist(set1, bins=30, density=True)
x1 = np.linspace(min(set1), max(set1), 30, endpoint=True)
gaussian_y = (1.0 / (statistics.stdev(set1) * np.sqrt(2 * np.pi))) * \
    np.exp(-((x1 - statistics.mean(set1)) * 2) /
           (2 * statistics.stdev(set1) * 2))
plt.plot(x1, gaussian_y)
plt.show()


plt.hist(set2, bins=30, density=True)
x1 = np.linspace(min(set2), max(set2), 30, endpoint=True)
gaussian_y = (1.0 / (statistics.stdev(set2) * np.sqrt(2 * np.pi))) * \
    np.exp(-((x1 - statistics.mean(set2)) * 2) /
           (2 * statistics.stdev(set2) * 2))
plt.plot(x1, gaussian_y)
plt.show()

plt.hist(set3, bins=30, density=True)
x1 = np.linspace(min(set3), max(set3), 30, endpoint=True)
gaussian_y = (1.0 / (statistics.stdev(set3) * np.sqrt(2 * np.pi))) * \
    np.exp(-((x1 - statistics.mean(set3)) * 2) /
           (2 * statistics.stdev(set3) * 2))
plt.plot(x1, gaussian_y)
plt.show()

plt.hist(set4, bins=30, density=True)
x1 = np.linspace(min(set4), max(set4), 30, endpoint=True)
gaussian_y = (1.0 / (statistics.stdev(set4) * np.sqrt(2 * np.pi))) * \
    np.exp(-((x1 - statistics.mean(set4)) * 2) /
           (2 * statistics.stdev(set4) * 2))
plt.plot(x1, gaussian_y)
plt.show()


# np.linspace for gaussian line
# gaussian_y = (1.0 / (std * np.sqrt(2 * np.pi))) * np.exp(-((gaussian_x - mean) * 2) / (2 * std * 2))


# print("Mean: % s" %(statistics.mean(set1))
# print("Standard Deviation: % s" %(statistics.stdev(set1)))
# print()
#
# print("Mean: " statistics.mean(set2))
# print("Standard Deviation: " statistics.stdev(set2))
# print()
#
# print("Mean: " statistics.mean(set3))
# print("Standard Deviation: " statistics.stdev(set3))
# print()
#
# print("Mean: " statistics.mean(set4))
# print("Standard Deviation: " statistics.stdev(set4))
# print()
