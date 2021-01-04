def tap_rain_water(num,arr):
    left=[0 for i in range(num)]
    right=[0 for i in range(num)]
    left[0]=0
    water_filled=0
    right[num-1]=0
    for i in range(1,num):
        left[i]=max(left[i-1],arr[i-1])
    for i in range(num-2,-1,-1):
        right[i]=max(right[i+1],arr[i+1])
    for i in range(num):
        a=(min(left[i],right[i])-arr[i])
        if a>0:
            water_filled=water_filled+a
    return water_filled





tap_rain_water(5,[1,2,3,4,5])
