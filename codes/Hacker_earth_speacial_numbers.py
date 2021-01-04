from itertools import permutations
from math import gcd as bltin_gcd

# Write your code here
N = input()
String_special = '47474747474747474744444444444'
st1 = len(N)-len(String_special)

if st1>0:
    for i in range(st1):
        String_special=String_special+'47'
s2 = sorted([int(''.join(p)) for p in set(permutations(String_special,len(N)))])
SpecialList=[]
for i in s2:
    if  i <= int(N):
        SpecialList.append(i)
for i in range(1,len(N)):
    s = sorted([int(''.join(p)) for p in set(permutations(String_special,i))])
    SpecialList = SpecialList+s
result=[]
print(SpecialList)
for i in range(len(SpecialList)):
    for j in range(i,len(SpecialList)):
        a=SpecialList[i]
        b=SpecialList[j]
        if bltin_gcd(a, b) == 1 and ((a,b) or(b,a)) not in result :
            result.append((SpecialList[i], SpecialList[j]))

print(len(result))
