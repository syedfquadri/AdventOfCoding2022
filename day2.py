f = open("day2.txt",'r')
s = {'X':-1,'Y':0,'Z':1}
o = {'A':1,'B':2,'C':3}
e = 0
j = 0

######PART 1###################
# for i in f:
#     print(i)
#     e += s[i[2]]
#     if o[i[0]] == s[i[2]]: #draw
#         j += 3
#     elif  (i[0]=='A' and i[2]=='Z'):
#         j += 0
#     elif (i[0]=='C' and i[2]=='X') or o[i[0]]<s[i[2]]: #win
#         j += 6
#     else: #loose
#         j += 0
# print(f'e: {e}, j:{j} and sum is : {e+j}')

############## PART 2 #############
for i in f:
    if i[2] == 'X':
        j += 0
        if i[0] != 'A':
            e += o[i[0]]-1
        else:
            e += 3
    elif i[2] == 'Y':
        j += 3
        e += o[i[0]]
    else:
        j+=6
        if i[0] != 'C':
            e += o[i[0]]+1
        else:
            e += 1
print(e+j)