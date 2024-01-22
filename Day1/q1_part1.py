with open('input.txt', 'r') as file:
    ip = file.readlines()
    
total = 0

for s in ip:
    for i in range(len(s)):
        if s[i].isdigit():
            break
    rev = s[::-1]
    for j in range(len(s)):
        if rev[j].isdigit():
            break
    first = int(s[i]) #find first occuring digit in each line
    last = int(rev[j]) #find last occuring digit in each line
    
    total += int(str(first)+str(last))
    
print(total)
