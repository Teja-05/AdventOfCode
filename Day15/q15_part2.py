with open('hashalgo.txt', 'r') as f:
    ip = f.read()

l = ip.split(',')

d = [{} for i in range(256)]
totalpower = 0

#to compute hashvalue of each label
def findhash(st):
    hashval, temp = 0, 0 #to store hashvalue of each string in input sequence
    for c in st:
        temp += ord(c)
        temp *= 17
        temp %= 256
    hashval += temp
    return hashval

for line in l:
    if '=' in line:
        label, foclength = line.split('=')
        boxid = findhash(label)
        d[boxid][label] = int(foclength) #add lens with the given label or replace accordingly
    else:
        label = line[:-1]
        boxid = findhash(label)
        if label in d[boxid]:
            del d[boxid][label] #remove lens if present in the box already

for bid, boxno in enumerate(d,1):
    for slotno, lens in enumerate(boxno.items(),1):
        totalpower += bid*slotno*lens[1] #find focusing power of each lens

print(totalpower)
