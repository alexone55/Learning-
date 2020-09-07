import re
import pandas as pd

inFile = open('./Files/babynames/baby1990.html', 'r', encoding='utf8')

str = inFile.read()
match = re.findall(r'<td>(.*?)</td>', str)
name_list = []

for i in range(0, len(match), 3):
    name_list.append(tuple(match[i:i+3]))
print(name_list)
