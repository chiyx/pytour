#! /usr/bin/env python3
# coding = utf-8

import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()

curs.execute(
    '''
    CREATE TABLE if not exists zoo(
        critter varchar(20) primary key,
        count int,
        damages float
    )
    '''
)
# insert data
ins = 'insert into zoo (critter, count, damages) values (?, ?, ?)'
curs.execute(ins, ('wease1', 1, 2000.0))
curs.execute(ins, ('duck', 5, 0.0))
curs.execute(ins, ('bear', 2, 1000.0))
# query
curs.execute('select * from zoo')
rows = curs.fetchall()
print(rows)
# order
curs.execute('select * from zoo order by count')
rows = curs.fetchall()
print(rows)
curs.close()
conn.close()
