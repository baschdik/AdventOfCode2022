def MatchPoints(Strategy):
    return {
        'A X\n':3,
        'A Y\n':4,
        'A Z\n':8,
        'B X\n':1,
        'B Y\n':5,
        'B Z\n':9,
        'C X\n':2,
        'C Y\n':6,
        'C Z\n':7

    }[Strategy]


f= open('input.txt','r')

input = f.readlines()

f.close

curPoints = 0
for line in input:
    curPoints += int(MatchPoints(line))
    

     

print(curPoints)

