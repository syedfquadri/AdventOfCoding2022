f = open("inputs/day6.txt",'r')

def sub_Routine(f):
    a = 0
    b = []
    for idx, j in enumerate(f):
        if len(b)==14 and idx!=0:
            if len(set(b))==len(b):
                return idx
            else:
                del b[0]
                b.append(j)
        else:
            b.append(j)
    return idx

# TEST CASES

# 4 PACKET
# print(sub_Routine("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5)
# print(sub_Routine("nppdvjthqldpwncqszvftbrmjlhg") == 6)
# # 14 MESSAGES
# print(sub_Routine("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19)
# print(sub_Routine("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23)


for i in f:
    z = sub_Routine(i)
    print(z)