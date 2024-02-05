with open('map.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

total = 0
instructions = l[0]
mappings = l[2:]
d = {}

for line in mappings:
    source, dest = line.split(' = ')
    d[source] = dest[1:-1].split(', ') #to create a map for each node

#print(d)
    
i=0 #traverse the instruction string
currpoint = 'AAA'

while(1):
    total += 1
    if instructions[i]=='L':
        currpoint = d[currpoint][0] #update with left element
    elif instructions[i]=='R':
        currpoint = d[currpoint][1]  #update with right element

    if currpoint=='ZZZ':
        break
    
    i += 1
    if i==len(instructions): #to repeat the instructions further
        i = 0

print(total)
