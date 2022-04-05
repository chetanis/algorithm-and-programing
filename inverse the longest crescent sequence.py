T1=[2,3,4,15,16,17,0,0,-4,5,6,7,8,9,10,1,2]

def inversLong(T):
    max=0;index=0;m=0
    for i in range(len(T)-1):
        if T[i]<T[i+1]:m+=1
        else:
            if m>max:
                max=m
                index=i-max
                m=0
    max=index+max
    while index<max:
        T[index],T[max]=T[max],T[index]
        index+=1;max-=1

inversLong(T1)
print(T1)


