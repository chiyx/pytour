#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from utils import resourcesLoader

csv_file = resourcesLoader.getRealPath('catlogo.png')


print(csv_file)
