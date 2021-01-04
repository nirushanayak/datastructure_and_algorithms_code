from itertools import permutations
n = int(input())
m = int(input())
global count
count = 0

def isValid(p):
    for i in range(1,n+1):
        if abs(p[i-1]-i) == m:
            return False
    global count
    count = count+1
    return True


a=[isValid(list(p)) for p in list(permutations(range(1,n+1)))]
print(count)

