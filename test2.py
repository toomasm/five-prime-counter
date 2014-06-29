import pybedtools
from pybedtools import BedTool
from collections import Counter


# The chosen input file is a random test file I got from the Internet and modified for testing my code
tool1 = BedTool("test2.bed")


# Finds the start positions of all reads and stores these to a list calles "Storage"
storage = []
for x in range(0, 100):
    feature = tool1[x]
    if feature.strand == '+':
        start_pos = (feature.start)
        storage.append(start_pos)
    elif feature.strand == '-':
        start_pos = (feature.stop)
        storage.append(start_pos)

# Counts the occurrences of a start position and stores the position and the number of occurrences in a dictionary 
result = {} 
for x in storage:
    count = storage.count(x)
    result[x] = count
    while count > 1:
        storage.remove(x)
        count = count - 1 
        
for x in result:
    print x, result[x]