f = open("inputs/day4.txt",'r')
z = 0
for i in f:
    a,b = i.strip().split(",")
    p_1 = a.split('-')
    p_2 = b.split('-')
    p_1_set = set(range(int(p_1[0]),int(p_1[1])+1))
    p_2_set = set(range(int(p_2[0]),int(p_2[1])+1))
    # if p_1_set.issubset(p_2_set) or p_2_set.issubset(p_1_set): ###### PART 1 #######
    #     z += 1
    if len(p_2_set.intersection(p_1_set))>0: ######## PART 2 ##########
        z += 1
print(z)