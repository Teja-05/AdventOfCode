with open('lagoon.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

d = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
digplan = []

for line in l:
    direction, steps, color = line.split(' ')
    digplan.append([direction, int(steps)]) #take only direction and steps to dig

r, c = 0, 0
area, perimeter = 0, 0

for direction, steps in digplan:
    perimeter += steps
    dc, dr = d[direction]
    nc = c + dc*steps
    nr = r + dr*steps

    area += (r-nr)*(c+nc) #area covered by moving steps in the direction
    r, c = nr, nc

total = area//2 + perimeter//2 + 1

print(total)
