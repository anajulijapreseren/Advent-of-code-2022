f = open("day1.txt", "r")
sums=[]
cur_sum=0
for line in f:
    if line=="\n":
        sums.append(cur_sum)
        cur_sum=0
    else:
        cur_sum+=float(line)

#1. del
print("max kalorije {}".format(max(sums)))

#2. del
sums.sort(reverse=True)
vsota3=sum(sums[:3])
print("vsota kalorij prvih treh je {}".format(vsota3))

