with open("day4.txt") as f:
    counter=0
    for line in f:
        line=line.replace('\n','')
        w=line.split(',')
        prvi=w[0].split('-')
        drugi=w[1].split('-')
        #You need to change string to int, otherwise comparison is not correct:
        #'52'<'8' = True #primerja unicode
        #52<8 = False
        prvi=[int(i) for i in prvi]
        drugi=[int(i) for i in drugi]
    
        if (prvi[0]<=drugi[0] and prvi[1]>=drugi[1]): #drugi vsebovan v prvem
            counter+=1
        elif (prvi[0]>=drugi[0] and prvi[1]<=drugi[1]): #prvi vsebovan v drugem
            counter+=1
print(counter)

