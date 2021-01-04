def sub_sum(L,n,Sum):
    index_0=0
    index_n=0
    term=L[index_0]
    while(index_n<=n-1):
        while term <= Sum:
            if term == Sum:
                return (index_0,index_n)
            index_n=index_n+1
            if index_n == n:
                return (-1,-1)
            term=term+L[index_n]
        term=term-L[index_0]
        index_0=index_0+1
    return (-1,-1)


# L=[1,2,3]
# a,b=sub_sum(L,3,12)
# print(a,b)

n=int(input())
for i in range(n):
    num,sum=map(int,input().split(' '))
    L=list(map(int,input().split()))
    a,b=sub_sum(L,num,sum)
    if a==-1:
        print(a)
    else:
        print(a,b)


