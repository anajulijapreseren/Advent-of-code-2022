s1=['B','P','N','Q','H','D','R','T']
s2=['W','G','B','J','T','V']
s3=['N','R','H','D','S','V','M','Q']
s4=['P','Z','N','M','C']
s5=['D','Z','B']
s6=['V','C','W','Z']
s7=['G','Z','N','C','V','Q','L','S']
s8=['L','G','J','M','D','N','V']
s9=['T','P','M','F','Z','C','G']
s=[s1,s2,s3,s4,s5,s6,s7,s8,s9]


with open('day5.txt') as f:
    for line in f:
        bes=line.split(' ')
        amount=int(bes[1])
        od=int(bes[3])-1
        do=int(bes[5])-1
        for i in range(amount):
            s[do].append(s[od][-1])
            s[od].pop()

zgoraj=[]
for i in s:
    if i!=[]:
        zgoraj.append(i[-1])
print(''.join(zgoraj))