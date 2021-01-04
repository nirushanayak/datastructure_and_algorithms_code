def rev_list_in_gropus(num,arr,k):
    i0 = 0
    rev = []
    while i0 < num:
        i1 = i0+k
        if i1 <= num:
            s = arr[i0:i1]
            s = s[::-1]
            rev = rev+s
            i0 = i1
        else:
            s = arr[i0:]
            s = s[::-1]
            rev = rev+s
            i0 = i1
    return rev

n=int(input())
for i in range(n):
    num,k=map(int,input().split())
    arr=list(map(int,input().split()))
    res=rev_list_in_gropus(num,arr,k)
    print(*res)

