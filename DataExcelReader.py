# Python Data Excel Reader
# Max Base
# https://github.com/BaseMax/PythonDataExcelReader
# 2020-11-06

import json

def readExel(fileTxt):
    reader = open(fileTxt)
    try:
        context=reader.read()
        context=context.strip()
        # print(context)
        rows=context.split('\n')
        # print(rows)
        for i in range(len(rows)):
            rows[i]=rows[i].split('\t')
            # print(rows[i])
        return rows
    finally:
        reader.close()
    return []

rows=readExel('input.txt')
print(rows)
output = open("output.json", "w")
output.write( json.dumps(rows))
output.close()
