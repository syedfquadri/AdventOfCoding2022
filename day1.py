f = open("day1.txt",'r')
sum = []
x =0
for i in f:
    if len(i) == 1:
        sum.append(x)
        x =0
    else:
        x += int(i)
ssum = sorted(sum)
print(ssum)