l=[1,2,0,3,0,0,9]
zeros=[]
digit=[]
for i in l:
    if i==0:
        zeros.append(i)
    else:
        digit.append(i)
print(digit+zeros)        
