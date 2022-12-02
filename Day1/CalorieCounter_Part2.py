from pydoc import doc
from telnetlib import theNULL


f= open('input.txt','r')

input = f.readlines()

f.close

allElves = []
curCalories = 0
for line in input:
    if line == '\n':
        allElves.append(curCalories)
        curCalories = 0
    else:

        curCalories += int(line)

allElves.sort(reverse=True)
maxCalories = allElves[0] + allElves[1] + allElves[2]
print(maxCalories)