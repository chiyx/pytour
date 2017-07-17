#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from numpy import *

rand_mat = mat(random.rand(4, 4))
inv_rand_mat = rand_mat.I
my_eye = rand_mat * inv_rand_mat
print(my_eye - eye(4))
