l=[2,3,4,5]
target=7
d={}
for i in range(len(l)):
    diff=target-l[i]
    if diff in d:
        print(d[diff],i)
    d[l[i]]=i
        