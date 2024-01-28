with open('scratchcard.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0
n = len(l)
arr = []
matches = []

for i in range(n):
    arr.append([i+1,1])

for line in l:
    temp = line.split(':')
    winningnums, havingnums = temp[1].split('|')
    
    l1 = winningnums.split(' ')
    l1 = [int(x) for x in l1 if x!='']
    l2 = havingnums.split(' ')
    l2 = [int(x) for x in l2 if x!='']

    match = len(set(l1).intersection(set(l2))) #find the count of common numbers
    matches.append(match) #add matching number count of each card

for i in range(n):
    m = matches[i]
    for j in range(m):
        arr[i+j+1][1] += arr[i][1] #copy the cards based on matching number count
        
for i in range(n):
    total += arr[i][1] #find sum of card instances

print(total)
