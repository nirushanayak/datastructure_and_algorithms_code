def poisonousPlants(A):
    count =0
    while(True):
        s=[]
        s.append(A[0])
        for i in range(1,len(A)):
            if(A[i]<= A[i-1]):
                s.append(A[i])
        if s==A:
            return count
        else:
            A=s
            s=[]
            count=count+1


c=poisonousPlants([1,1,1,1,1])
print(c)
