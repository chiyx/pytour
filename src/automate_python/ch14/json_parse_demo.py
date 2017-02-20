#! /usr/bin/env python3
# coding = utf-8

import json

stringOfJsonData = '''
{
    "name": "Zophie",
    "isCat": true,
    "miceCaught": 0,
    "felineIO": null
}
'''

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)
