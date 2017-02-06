#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import pprint

from model.users import User

path = './tables.txt'

f1 = open(path, 'r') 
trt1 = f1.read() 

tables = json.loads(trt1)
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(tables)

for table in tables:
    print table
    print '------------------------------'
    tt = tables[table]
    cols = tt['cols']
    for field in cols:
        print field['name'], field['type'], field['comment']
    cols = tt['fkeys']
    for field in cols:
        print field['fk_name'], field['fk_table']
    usr = User(table)
    usr.generate()

