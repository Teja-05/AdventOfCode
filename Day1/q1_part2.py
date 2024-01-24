import re

with open('input.txt', 'r') as file:
    ip = file.read()

l = ip.split('\n')

total = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five': 5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

pattern = re.compile('|'.join(numbers + [r'\d'])) #include both words and digits

for line in l:
    matches = []
    idx = 0

    #find overlapping matches
    while idx<len(line):
        match = pattern.search(line, idx) #search pattern match at each index
        if not match:
            break
        else:
            matches.append(match.group())
        idx += 1
        
    #print(matches)
    first = matches[0] if matches[0].isdigit() else d[matches[0]]
    last = matches[-1] if matches[-1].isdigit() else d[matches[-1]]

    total += int(str(first)+str(last))

print(total)
