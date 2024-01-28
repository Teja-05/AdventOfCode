with open('scratchcard.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0

for line in l:
    temp = line.split(':')
    winningnums, havingnums = temp[1].split('|')
    
    l1 = winningnums.split(' ')
    l1 = [int(x) for x in l1 if x!='']
    l2 = havingnums.split(' ')
    l2 = [int(x) for x in l2 if x!='']

    matches = len(set(l1).intersection(set(l2))) #find the count of common numbers
    
    if matches>0: 
        total += pow(2,matches-1) #add points on each card
        
print(total)