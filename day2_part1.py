#naredim slovarcek: igra:rezultat zame
dic={}

pari=[("A","X"),("A","Y"),("A","Z"),("B","X"),("B","Y"),("B","Z"),("C","X"),("C","Y"),("C","Z")]

#za vsak možen par v igri izračunam dobljene točke zame
for i in pari:
    if i[1]=="X":
        izbira=1 #koliko točk dobiš za izbiro X
        if i[0]=="A":
            rez=3   #koliko točk dobiš za poraz/remi/zmago
        elif i[0]=="B":
            rez=0
        else: #nasprotnik izbere skarje
            rez=6
    elif i[1]=="Y":
        izbira=2
        if i[0]=="A":
            rez=6
        elif i[0]=="B":
            rez=3
        else:
            rez=0
    else:#izbrali smo Z (skarje)
        izbira=3
        if i[0]=="A":
            rez=0
        elif i[0]=="B":
            rez=6
        else:
            rez=3
    dic[i]=izbira+rez

stetje={i:0 for i in pari}

#preštejemo koliko posameznih parov imamo
f = open("day2.txt", "r")
for line in f:
    tup=(line[0],line[2])
    stetje[tup]+=1

koncnirez=0
for i in stetje: #keys
    koncnirez+=stetje[i]*dic[i] 
    
print("part1 rezultat: {}".format(koncnirez))