#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# knn.py - k-近邻算法

from numpy import *
import operator


def create_dataset():
    group = array([[1.0, 1.1],
                   [1.0, 1.0],
                   [0, 0],
                   [0, 0.1]
                   ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(in_x, date_set, labels, k):
    "k-近邻算法"
    # 计算距离
    data_set_size = date_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - date_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    # 选择距离最小的k个点
    sorted_dist_indcies = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_lable = labels[sorted_dist_indcies[i]]
        class_count[vote_i_lable] = class_count.get(vote_i_lable, 0) + 1
    sored_class_count = sorted(
        class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sored_class_count[0][0]


def file2matrix(filename):
    with open(filename) as fr:
        array_of_lines = fr.readlines()
    number_of_lines = len(array_of_lines)
    mat = zeros((number_of_lines, 3))
    class_label_vertor = []
    index = 0
    for line in array_of_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        mat[index, :] = list_from_line[0:3]
        class_label_vertor.append(int(list_from_line[-1]))
    return mat, class_label_vertor


def main():
    group, labels = create_dataset()
    print(classify0([0, 0], group, labels, 3))

if __name__ == '__main__':
    main()
