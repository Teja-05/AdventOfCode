with open('boatrace.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

total = 1
t, d = l[0], l[1]
l1 = t.split(':')[1].split(' ')
l2 = d.split(':')[1].split(' ')
time = [int(x) for x in l1 if x!='']
distance = [int(x) for x in l2 if x!='']
n = len(time)

for i in range(n):
    currtime = time[i]
    currdist = distance[i]
    ways = 0

    temp = []
    for j in range(1,currtime+1):
        dist = (currtime-j)*j #distance travelled for each timestamp
        temp.append(dist)

    for x in temp:
        if x>currdist:
            ways += 1 #find no of ways to win for each timestamp

    total *= ways

print(total)