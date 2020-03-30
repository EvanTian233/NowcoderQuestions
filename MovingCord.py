


inval = input().split(';')
print(0)
initx = 0
inity = 0

for i in inval:
    if i[0] == 'A':
        initx -= int(i[1:])
    if i[0] == 'D':
        initx += int(i[1:])
    if i[0] == 'W':
        inity += int(i[1:])
    if i[0] == 'S':
        inity -= int(i[1:])
    else:
        continue


print(str(initx) + ',' + str(inity))

