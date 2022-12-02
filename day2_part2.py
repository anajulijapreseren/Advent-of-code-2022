#ista fora kot 1.del, le druge vrednosti v prvem slovarju
dic={}

pari=[("A","X"),("A","Y"),("A","Z"),("B","X"),("B","Y"),("B","Z"),("C","X"),("C","Y"),("C","Z")]

#za vsak možen par v igri izračunam dobljene točke zame
for i in pari:
    if i[1]=="X": #lose
        rez=0 #koliko točk dobim za poraz
        if i[0]=="A": #nasprotnik izbere kamen, jaz moram škarje->3 tocke za izbiro
            izbira=3   #koliko točk dobiš za poraz/remi/zmago
        elif i[0]=="B":
            izbira=1  
        else: #nasprotnik izbere skarje
            izbira=2  
    elif i[1]=="Y": #draw
        rez=3
        if i[0]=="A":
            izbira=1  
        elif i[0]=="B":
            izbira= 2 
        else:
            izbira=3  
    else: #win
        rez=6
        if i[0]=="A":
            izbira=2  
        elif i[0]=="B":
            izbira=3  
        else:
            izbira= 1 
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
     
print("part2 rezultat: {}".format(koncnirez))