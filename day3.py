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