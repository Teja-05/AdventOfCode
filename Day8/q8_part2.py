import math

with open('map.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

res = 0
instructions = l[0]
mappings = l[2:]
d = {}
temp = []

for line in mappings:
    source, dest = line.split(' = ')
    if source.endswith('A'):
        temp.append(source) #take all nodes ending with 'A' as source
    d[source] = dest[1:-1].split(', ') #to create a map for each node
    
i=0 #traverse the instruction string
paths = {}

while(1):
    res += 1

    for j in range(len(temp)): #cover all the source nodes
        if instructions[i]=='L':
            temp[j] = d[temp[j]][0] #update with left element
        elif instructions[i]=='R':
            temp[j] = d[temp[j]][1]  #update with right element
        if temp[j][-1]=='Z' and j not in paths:
            paths[j] = res #steps for each source node

    if len(paths)==len(temp): #when all source nodes are covered
        break
    
    i += 1
    if i==len(instructions): #to repeat the instructions further
        i = 0

#print(paths)
        
dist = list(paths.values())
res = dist[0]
for d in dist[1:]:
    res = math.lcm(res,d) #find total moves
    
print(res)
