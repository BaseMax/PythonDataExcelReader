# Max Base
# 
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
