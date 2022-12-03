import string

alpha_low = list(string.ascii_lowercase)
alpha_up = list(string.ascii_uppercase)
alpha=alpha_low+alpha_up
st=list(range(1,52+1))

values={alpha[i]:st[i] for i in range(len(alpha))}
#---------------part 2------------------------------
from itertools import islice

vsota=0
x=0
with open("day3.txt") as file:
    while True:
        next_3_lines = list(islice(file, 3))
        if not next_3_lines:
            break
        brezn=[]
        for i in next_3_lines:
            ibrez=i.replace('\n','')
            brezn.append(ibrez)
        common_letters=list(set(brezn[0])&set(brezn[1])&set(brezn[2]))
        for j in common_letters:
            vsota+=values[j]
        

print("Resitev part2 je:{}".format(vsota))