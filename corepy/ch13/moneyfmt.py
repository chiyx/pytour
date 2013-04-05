#! /usr/bin/env python

class MoneyFmt(object):
    "a money fomat tool class"

    def __init__(self, value, sign="$"):
        if (not isinstance(value, float)):
            raise TypeError, 'value must be a float value'
        self.__value = value
        self.__sign = sign

    def __nonzere__(self):
        return (self.__value == 0.0)

    def __repr__(self):
        return str(self.__value)

    def __str__(self):
        return self.dollarize()

    def update(self, new_val):
        if (not isinstance(new_val, float)):
            raise TypeError, 'value must be a float value'
        self.__value=new_val

    def dollarize(self):
        int_value = int(self.__value * 100)
        vturpe = divmod(int_value, 100000)
        lv = vturpe[0]
        rv = vturpe[1]
        temarr = []
        while lv !=0:
            temarr.append(str(lv % 1000))
            lv /= 1000
        temarr.reverse()
        lvstr = ','.join(temarr)
        if len(lvstr):
            lvstr += ','
        rvstr = '%06.2f' % (rv / 100.0)
        return self.__sign + lvstr + rvstr

