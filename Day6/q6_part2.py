with open('boatrace.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

total = 1
str1, str2 = '',''
t, d = l[0], l[1]
l1 = t.split(':')[1].split(' ')
l2 = d.split(':')[1].split(' ')

for x in l1:
    if x!='':
        str1 += x
        
for y in l2:
    if y!='':
        str2 += y

time = int(str1)
distance = int(str2)

temp = []
ways = 0

for i in range(1,time+1): #distance travelled at each millisecond
        dist = (time-i)*i
        temp.append(dist)

for x in temp:
    if x>distance:
        ways += 1 #find no of ways to win

print(ways)