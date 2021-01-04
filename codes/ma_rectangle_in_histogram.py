
def max_area(l,n):
    area = []
    area.append(l[0])
    h=l[0]
    w = 1
    weight = 0
    maximun_area = l[0]
    for i in range(1, n):
        if l[i]< h:
            weight = h*(w+1)-(h-l[i])*(w+1)
        else:
            weight= area[i-1]+h
        prev = area[i-1]
        curr = l[i]
        prev_next = weight
        a = max(prev,curr,prev_next)
        if a==prev_next:
            area.append(a)
            h=min(h,l[i])
            w=w+1
        elif a==prev or a==curr:
            area.append(curr)
            h=curr
            w=1
        if area[i]> maximun_area:
            maximun_area = area[i]

    return maximun_area


test_num=int(input())
for i in range(test_num):
    n=int(input())
    heights=list(map(int,input().split()))
    res=max_area(heights,n)
    print(res)


