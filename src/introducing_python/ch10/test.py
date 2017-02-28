#! /usr/bin/env python3
# coding = utf-8
# test.py - some statement run test.

import os
from datetime import datetime
from datetime import date
import time
import locale

print(os.getcwd())

some_day = datetime(2014, 1, 2, 3, 4, 5, 6)

print(some_day.isoformat())

now = time.time()

print(time.ctime(now))
print(time.localtime(now))
print(time.gmtime(now))

halloween = date(2014, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'zh_cn']:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))



