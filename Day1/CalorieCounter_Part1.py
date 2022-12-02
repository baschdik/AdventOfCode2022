from pydoc import doc
from telnetlib import theNULL


f= open('input.txt','r')

input = f.readlines()

f.close

curMax = 0
curCalories = 0
for line in input:
    if line == '\n':
        if curMax < curCalories:
            curMax = curCalories
        curCalories = 0
    else:

        curCalories += int(line)

print(curMax)