def twoStacks(x, a, b):
    sum = 0
    count = 0
    while (sum <= x):
        count = count + 1
        res = which_stack(a, b)
        if res == 'a':
            sum = sum + a.pop(0)
        elif res == 'b':
            sum = sum + b.pop(0)
        else:
            return count-1
    return count-1

def which_stack(s1, s2):
    if (len(s1) == 0 and len(s2) == 0):
        return 'c'
    if (len(s1) == 0):
        return 'b'
    if (len(s2) == 0):
        return 'a'
    if (s1[0] < s2[0]):
        return 'a'
    elif s1[0] > s2[0]:
        return 'b'
    else:
        s1.pop(0)
        s2.pop(0)
        which_stack(s1, s2)



c=twoStacks(62,[7 ,15, 12, 0, 5, 18,17,2,10,15,4, 2, 9, 15, 13, 12, 16],
            [12 ,16, 6, 8, 16, 15, 18, 3, 11, 0, 17, 7, 6, 11, 14, 13, 15, 6, 18, 6, 16, 12, 16, 11, 16, 11])
print(c)
