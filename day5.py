f = open("inputs/day5.txt",'r')
dct = {1: ["P","D","Q","R","V","B","H","F"],
       2: ["V","W","Q","Z","D","L"],
       3:["C","P","R","G","Q","Z","L","H"],
       4:["B","V","J","F","H","D","R"],
       5:["C","L","W","Z"],
       6:["M","V","G","T","N","P","R","J"],
       7:["S","B","M","V","L","R","J"],
       8:["J","P","D"],
       9:["V","W","N","C","D"]
       }
for i in dct:
    dct[i] = dct[i][::-1]
    
######### PART 1 ############
# for i in f:
#     i = i.strip().split(' ')
#     for j in range(int(i[1])):
#         dct[int(i[-1])].append(dct[int(i[3])][-1])
#         dct[int(i[3])].pop()
# z = ""
# for i in dct:
#     print(dct[i][-1])
#     z += dct[i][-1]
# print(f"z: {z}")