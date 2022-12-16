f = open("inputs/day3.txt",'r')

##### PART 1 ######
# summ = 0
# for i in f:
#     i = i.strip('\n')
#     l = len(i)//2
#     a = list(i[0:l])
#     b = list(i[l:])
#     j = [k for k in a if k in b]
#     if ord(j[0]) >= ord('A') and ord(j[0]) <= ord('Z'):
#         summ += ord(j[0])-64+26
#     else:
#         summ += ord(j[0])-96
# print(summ)

##### PART 2 ######
summ = 0
lst = []
d = {0:[],1:[],2:[]}
for idx,i in enumerate(f):
    i = i.strip('\n')
    if idx ==299:
        print(idx)
        d[idx%3]=list(i)
    if (idx%3 ==0 and idx!=0) or idx==299:
        c_1_2 = [k for k in d[0] if k in d[1]]
        c_2_3 = [k for k in d[1] if k in d[2]]
        z = [l for l in c_1_2 if l in c_2_3]
        if ord(z[0]) >= ord('A') and ord(z[0]) <= ord('Z'):
            summ += ord(z[0])-64+26
            lst.append(ord(z[0])-64+26)
        else:
            summ += ord(z[0])-96
            lst.append(ord(z[0])-96)
        d = {0:[],1:[],2:[]}
    d[idx%3]=list(i)
print(summ)