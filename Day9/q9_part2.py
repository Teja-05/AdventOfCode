with open('report.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

total = 0
histories = []

def func(arr):
    diff = []
    if arr.count(0)==len(arr): #if all are zeroes
        return 0
    for i in range(len(arr)-1):
        diff.append(arr[i+1]-arr[i]) #find difference until all are zeroes
    return arr[-1] + func(diff)

for line in l:
    histories.append([int(x) for x in line.split(' ')])

for h in histories:
    hrev = h[::-1] #reverse to extrapolate first value
    nextval = func(hrev) #next value for each history in report
    total += nextval

print(total)
