#!/bin/env python
#-*- coding: utf-8 -*-


from subprocess import *
from xlsxwriter import *

cmd = "vmstat 1 5 | awk '{now=strftime(\"%Y-%m-%d %T \"); print now $0}'"
p = Popen(cmd, shell=True, stdout=PIPE)
(ret, err) = p.communicate()
print(ret)
workbook = Workbook('vmstat.xlsx')
worksheet = workbook.add_worksheet()

# 데이터를 줄 단위로 만듭니다.
retdecode=ret.decode('utf-8')
rows = retdecode.split("\n")

for row_idx, row in enumerate(rows) :
    columns = row.split()
    for col_idx, col in enumerate(columns) :
        worksheet.write(row_idx, col_idx, col)

workbook.close()