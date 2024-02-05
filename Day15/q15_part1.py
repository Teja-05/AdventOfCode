with open('hashalgo.txt', 'r') as f:
    ip = f.read()

l = ip.split(',')

currentvalue = 0 #holds sum of all currentvalues

for s in l:
    temp = 0 #to store hashvalue of each string in input sequence
    for c in s:
        temp += ord(c)
        temp *= 17
        temp %= 256
    currentvalue += temp

print(currentvalue)
