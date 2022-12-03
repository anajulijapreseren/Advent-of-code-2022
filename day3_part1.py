import string

f = open("day3.txt", "r")

alpha_low = list(string.ascii_lowercase)
alpha_up = list(string.ascii_uppercase)
alpha=alpha_low+alpha_up
st=list(range(1,52+1))

values={alpha[i]:st[i] for i in range(len(alpha))}

#------part 1-------------------------------------------
vsota=0

for i in f:
    i=i.replace('\n','')
    firstcom, secondcom = i[:len(i)//2], i[len(i)//2:]
    common_letters=list(set(firstcom)&set(secondcom))
    for j in common_letters:
        vsota+=values[j]
print("Resitev part1 je:{}".format(vsota))

