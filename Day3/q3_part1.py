import string
import re

with open('engine.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0
r, c = len(l), len(l[0])
pattern = re.compile(r'\d+') #to find digits
directions = [[-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1],[-1,-1]]

punctuations = string.punctuation
allowed = punctuations.replace('.','')
symbols = list(allowed)

def dfs(row,col):
    if (0<=row<r and 0<=col<c and l[row][col] in symbols): #check for partno
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

            #check if either side of number is surrounded by a symbol
            check.append(dfs(nr,start+dc))
            check.append(dfs(nr,end+dc))

        if(any(check)):
            partno = int(i.group())
            total += partno

print(total)