with open('rock.txt') as f:
    ip = f.read()

l = ip.split('\n')

arr = [list(line) for line in l]
total = 0
cols, rows = len(arr[0]), len(arr)

for i in range(cols):
    for j in range(rows):
        if arr[j][i] == 'O':
            while j > 0 and arr[j-1][i] == '.':
                arr[j][i] = '.'
                j -= 1
            arr[j][i] = 'O' #tilting the round rocks

            total += rows - j

print(total) #find the total load
