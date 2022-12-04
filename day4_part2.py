with open("day4.txt") as f:
    counter=0
    for line in f:
        line=line.replace('\n','')
        w=line.split(',')
        prvi=w[0].split('-')
        drugi=w[1].split('-')
        prvi=[int(i) for i in prvi]
        drugi=[int(i) for i in drugi]
    
        if prvi[1]>=drugi[0] and prvi[0]<=drugi[1]: 
            counter+=1
        elif prvi[0]<=drugi[1] and prvi[1]>=drugi[0]: 
            counter+=1
print(counter)