#! /usr/bin/env python3
# coding = utf-8

import os

ResourceDirPath = os.path.split(os.path.split(os.path.realpath(__file__))[0])[
    0] + "/resources/"


def getRealPath(filename):
    "get the real path of file in resoures dir"
    return ResourceDirPath + filename
