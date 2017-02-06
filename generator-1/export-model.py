# -*- coding: utf-8 -*-

import grt
import json
import pprint
import sys
tables = {}

schema = grt.root.wb.doc.physicalModels[0].catalog.schemata[0]
str=""""""
for table in schema.tables:
    tt = {'cols':[], 'fkeys':[]}
    cols = []
    for column in table.columns:
        #print column.name, column.formattedType, column.comment
        col = {}
        col['name'] = column.name
        col['type'] = column.formattedType
        col['comment'] = column.comment
        cols.append(col)
    tt['cols'] = cols
    cols = []
    for column in table.foreignKeys:
        col = {}
        fk_keys=[]
        for cc in column.referencedColumns:
            fk_keys.append(cc.name)
        col['fk_name'] = fk_keys
        col['fk_table'] = column.referencedTable.name
        cols.append(col)
    tt['fkeys'] = cols
    tables[table.name] = tt

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(tables)
trt = json.dumps(tables)

path = '/home/djordje/data/git/handbooks/generator-1/tables.txt'
f1=open(path, 'w+')
f1.write(trt)
f1.close()

