def window_max(n,arr,w):
    res=[]
    for i in range(n):
        j=i
        print(arr[i])
        res.append(arr[i])
        count=1
        while(count<3 and j+1<n):
            if(res[i]<arr[j+1]):
                res[i]=arr[j+1]
            j=j+1
            count=count+1
    return res


res=window_max(7,[1,3,-3,5,3,6,7],3)
print(res)
