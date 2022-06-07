import csv
import numpy as np
import matplotlib.pyplot as plt


def read_file(file1):
    non_student_list = []
    student_list = []
    complete_list = []
    with open(file1, newline='') as csvfile:
        myreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in myreader:
            break
        for row in myreader:
            default = 0 if row[0] == "No" else 1
            if row[1] == "No":
                non_student_list.append((row[2], row[3], default))
            elif row[1] == "Yes":
                student_list.append((row[2], row[3], default))
            complete_list.append((row[2], row[3], default))
    return np.array(non_student_list), np.array(student_list), np.array(complete_list)


def sample_array(array, n):
    num_rows = array.shape[0]
    random_indices = np.random.choice(num_rows, n, replace=False)
    return array[random_indices, :]


def split_by_class(array, classes):
    splits = [[] for i in range(classes)]
    for x, y, classification in array:
        splits[int(classification)].append((x, y))
    return [np.array(i).astype(np.float) for i in splits]


def classifier(sample):
    sample_array = np.array(sample).astype(np.float)
    x = sample_array[:, 0]
    y = sample_array[:, 1]
    n = len(sample_array)
    # print(sample_array)
    # print(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_stdv_func = np.vectorize((lambda x: x-x_mean))
    y_stdv_func = np.vectorize((lambda x: x-y_mean))
    b_1 = np.sum(x_stdv_func(x)*y_stdv_func(y))/(np.sum(x_stdv_func(x)**2))
    b_0 = y_mean - b_1 * x_mean
    return x, y, b_0, b_1


non_student_list, student_list, complete_list = read_file(
    '/Users/jjsmac/Desktop/ML/Default.csv')
splits = split_by_class(non_student_list, 2)
splits[0] = sample_array(splits[0], 100)
splits[1] = sample_array(splits[1], 100)
# x,y,b_0,b_1 = classifier(sample)
# plt.plot(x,b_1*x+b_0,'r')
plt.figure("Non-Student List")
plt.scatter(splits[0][:, 0], splits[0][:, 1], marker='.', c='red')
plt.scatter(splits[1][:, 0], splits[1][:, 1], marker='+', c='green')
plt.show()

plt.figure("Student List")
splits = split_by_class(student_list, 2)
splits[0] = sample_array(splits[0], 100)
splits[1] = sample_array(splits[1], 100)
# x,y,b_0,b_1 = classifier(sample)
# plt.plot(x,b_1*x+b_0,'r')
plt.scatter(splits[0][:, 0], splits[0][:, 1], marker='.', c='red')
plt.scatter(splits[1][:, 0], splits[1][:, 1], marker='+',  c='green')
plt.show()

plt.figure("Complete List")
splits = split_by_class(complete_list, 2)
splits[0] = sample_array(splits[0], 100)
splits[1] = sample_array(splits[1], 100)
# x,y,b_0,b_1 = classifier(sample)
# plt.plot(x,b_1*x+b_0,'r')
plt.scatter(splits[0][:, 0], splits[0][:, 1], marker='.', c='red')
plt.scatter(splits[1][:, 0], splits[1][:, 1], marker='+',  c='green')
plt.show()


# def main():
#     non_student_list, student_list, complete_list = read_file('/Users/anirudhbansal/Anirudh/School/12th Grade/ML 2/Default.csv')
#     splits = split_by_class(non_student_list,2)
#     splits[0] = sample_array(splits[0],100)
#     splits[1] = sample_array(splits[1],100)
#     # x,y,b_0,b_1 = classifier(sample)
#     # plt.plot(x,b_1*x+b_0,'r')
#     plt.figure("Non student list")
#     plt.scatter(splits[0][:,0],splits[0][:,1], marker = 'o')
#     plt.scatter(splits[1][:,0],splits[1][:,1], marker = 'x')
#     plt.show()
#
#     plt.figure("Student list")
#     splits = split_by_class(student_list,2)
#     splits[0] = sample_array(splits[0],100)
#     splits[1] = sample_array(splits[1],100)
#     # x,y,b_0,b_1 = classifier(sample)
#     # plt.plot(x,b_1*x+b_0,'r')
#     plt.scatter(splits[0][:,0],splits[0][:,1], marker = 'o')
#     plt.scatter(splits[1][:,0],splits[1][:,1], marker = 'x')
#     plt.show()
#
#     plt.figure("Complete list")
#     splits = split_by_class(complete_list,2)
#     splits[0] = sample_array(splits[0],100)
#     splits[1] = sample_array(splits[1],100)
#     # x,y,b_0,b_1 = classifier(sample)
#     # plt.plot(x,b_1*x+b_0,'r')
#     plt.scatter(splits[0][:,0],splits[0][:,1], marker = 'o')
#     plt.scatter(splits[1][:,0],splits[1][:,1], marker = 'x')
#     plt.show()
#
#
#
# if name == "main":
#     main()
