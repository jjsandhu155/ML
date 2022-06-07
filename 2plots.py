import csv
import statistics
import numpy as np
import matplotlib.pyplot as plt
import math

# read in data to array of tv and sales values
with open('Advertising.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in myreader:
        break
    tv_vals = []
    sales_vals = []
    for row in myreader:
        tv_vals.append(float(row[1]))
        sales_vals.append(float(row[4]))

n = len(tv_vals)

# compute mean of tv and sales
tv_mean = statistics.mean(tv_vals)
sales_mean = statistics.mean(sales_vals)

# compute beta1 and beta0
beta1_num = 0.0
for count, tv_val in enumerate(tv_vals):
    beta1_num += (tv_val - tv_mean) * (sales_vals[count] - sales_mean)
beta1_denom = 0.0
for count, tv_val in enumerate(tv_vals):
    beta1_denom += (tv_val - tv_mean)**2
beta1 = beta1_num/beta1_denom
beta0 = sales_mean - (beta1 * tv_mean)

# calculate rss for each beta0 and beta1 in xp and yp (for contour and surface plot)

# series of beta0 and beta1 values respectively
# xp = np . arange( 5.0 , 9.0 , 4.0 / 100 )
# yp = np . arange( .03 , .07 , .04 / 100 )

xp = np . arange(6.0, 8.0, 2.0 / 100)
yp = np . arange(.04, .06, .02 / 100)

rss_matrix = []
for y_val in yp:
    l = []
    for x_val in xp:
        cur_rss = 0
        for count, tv_val in enumerate(tv_vals):
            cur_rss += (sales_vals[count]-x_val-(y_val*tv_val))**2
        l.append(cur_rss)
    rss_matrix.append(l)

# generate contour plot
plt.contour(yp, xp, np.array(rss_matrix).transpose())
plt.scatter(beta0, beta1, color='#ff0000', marker='.')
plt.xlabel('beta0')
plt.ylabel('beta1')
plt.show()

# generate surface plot
xp, yp = np.meshgrid(xp, yp)
zp = np.array(rss_matrix)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(xp, yp, zp)
ax.scatter(7.0325935491277, 0.04753664, 2102.53, color='#FF0000')
plt.show()
