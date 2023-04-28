#!/usr/bin/env python3

import sys
import re

inputlist = list()
compare_list = list()

for file in sys.argv[1:]:
    f = open(file, 'r')
    for string in f:
        string = re.sub('[^A-Za-z]+', '\n', string)
        words = string.split()
        for word in words:
            word = word.strip()
            word = word.lower()
            if word not in inputlist:
                inputlist.append(word)
    f.close()

g = open('/usr/share/dict/words')
for word in g:
    word = word.strip()
    compare_list.append(word)
g.close()

for word in inputlist:
    if word not in compare_list:
        print(word)
