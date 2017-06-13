#! /usr/bin/env python3
# coding = utf-8

import re

# re sub
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
new_text = datepat.sub(r'\3-\1-\2', text)
print('re sub: %s' % (new_text))


# ignorecase
def match_case(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
text = 'UPPER PYTHON, lower python, Mixed Python'
new_text = re.sub('python', match_case('snake'), text, flags=re.IGNORECASE)
print('re sub ignorecase: %s' % (new_text))

# 最短匹配
str_pat = re.compile(r'\"(.*?)\"')
text1 = 'Computer says "no."'
rs = str_pat.findall(text1)
print(rs)
text2 = 'Computer says "no." Phone says "yes."'
rs = str_pat.findall(text2)
print(rs)
