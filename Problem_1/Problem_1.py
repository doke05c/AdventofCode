f = open("input.txt", "r")
a = f.read()


print(a)

i = 0
countO = 0
while i<len(a):
    if a[i] == '(':
        countO += 1;
    if a[i] == ')':
        countO -= 1;
    i += 1

print(countO)


i=0
countO = 0
while countO>-1:
    if a[i] == '(':
        countO += 1;
    if a[i] == ')':
        countO -= 1;
    i += 1

print(i)



