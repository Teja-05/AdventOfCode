with open('games.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0

for line in l:
    game, trials = line.split(':')
    gameid = game.split(' ')[-1]
    trial = trials.split(';') #get each trial for each game

    arr = []
    rmax, gmax, bmax = -1, -1, -1

    #find the maximum number of cubes for each color in a game across all trials
    for t in trial:
        curr = {'red':0, 'green':0, 'blue':0}
        cubeset = t.split(',')
        for cube in cubeset:
            cube = cube.lstrip(' ')
            qty, color = cube.split(' ')
            curr[color] += int(qty)

        for color, qty in curr.items(): #update max values
            if color=='red' and qty>rmax:
                rmax = qty
            if color=='green' and qty>gmax:
                gmax = qty
            if color=='blue' and qty>bmax:
                bmax = qty

    power = rmax*gmax*bmax
    total += power

print(total)
