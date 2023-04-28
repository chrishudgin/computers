#!/usr/bin/env python3

import sys
import re

count = dict()

if len(sys.argv) == 1:
    sys.exit(0)

for file in sys.argv[1:]:
    f = open(file, 'r')
    for string in f:
        string = re.sub('[^a-zA-Z]+', ' ', string)
        words = string.split()
        for word in words:
            word = word.strip()
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    f.close()

count = dict(sorted(count.items()))
for word in count:
    print(f'{count[word]: 4}', word)
