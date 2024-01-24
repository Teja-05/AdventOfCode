with open('games.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0
d = {'red':12, 'green':13, 'blue':14}

for line in l:
    game, trials = line.split(':')
    gameid = game.split(' ')[-1]
    trial = trials.split(';') #get each trial for each game

    arr = []

    #check for each trial if the count is less than  the limit for all colors
    for t in trial:
        curr = {'red':0, 'green':0, 'blue':0}
        cubeset = t.split(',')
        for cube in cubeset:
            cube = cube.lstrip(' ')
            qty, color = cube.split(' ')
            curr[color] += int(qty)

        check = all((d[color]>=qty for color, qty in curr.items()))
        arr.append(check)

    if sum(arr)==len(arr): #when all trials of a game satisfy the limit
        total += int(gameid)

print(total)
