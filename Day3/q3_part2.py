import re
from collections import defaultdict

with open('engine.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0
r, c = len(l), len(l[0])
pattern = re.compile(r'\d+') #to find digits
directions = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1],[-1,-1]]
arr = defaultdict(list)

def dfs(row,col):
    if (0<=row<r and 0<=col<c and l[row][col]=='*'):
        return 1
    return 0

for idx, line in enumerate(l):
    numidx = re.finditer(pattern,line) #find the positions where numbers appear in each row
    
    for i in numidx: #for each group of numbers find its start and end point
        start = i.start()
        end = i.end()-1
        #print(start,end)

        check = []
        for dr, dc in directions:
            nr = idx+dr

            #find all part numbers of a *
            if dfs(nr,start+dc):
                arr[(nr,start+dc)].append(i.group())
                break
            if dfs(nr,end+dc):
                arr[(nr,end+dc)].append(i.group())
                break

for gears in arr.values():
    if len(gears)==2: #check for gears
        total += int(gears[0])*int(gears[1]) #add gear ratios of induvidual gears

print(total)
