def MatchPoints(Strategy):
    return {
        'A X\n':4,
        'A Y\n':8,
        'A Z\n':3,
        'B X\n':1,
        'B Y\n':5,
        'B Z\n':9,
        'C X\n':7,
        'C Y\n':2,
        'C Z\n':6

    }[Strategy]


f= open('input.txt','r')

input = f.readlines()

f.close

curPoints = 0
for line in input:
    curPoints += int(MatchPoints(line))
    

     

print(curPoints)

