"""
There are N cars (numbered 1 through N) on a circular track with length N. For each i (2≤i≤N), the i-th of them is at a distance i−1 clockwise from car 1, i.e. car 1 needs to travel a distance i−1 clockwise to reach car i.

For each valid i, you can fill the i-th car's tank with up to fi litres of gasoline, with cost ci coins per litre.

After that, you choose some car, sit in this car and start driving in the clockwise direction. To move one unit of distance in this direction, you need to spend 1 litre of gasoline. When you pass another car (even if you'd run out of gasoline exactly at that point), you steal all its gasoline. You cannot move if you do not have any gasoline left.

Your goal is to fill the cars in such a way that you are able to choose an optimal car, travel the clockwise distance N and return to the place where you were initially. Under this constraint, you want to pay the least possible number of coins.

Find the smallest number of coins you need to pay. It is guaranteed that there is a way to travel the distance N. It can be proved that in such a case, the smallest number of coins is always an integer.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers f1,f2,…,fN.
The third line contains N space-separated integers c1,c2,…,cN.
Output
For each test case, print a single line containing one integer ― the smallest possible number of coins you need to pay.

Constraints
1≤T≤10
1≤N≤200,000
0≤fi≤109 for each valid i
0≤ci≤109 for each valid i
Subtasks
Subtask #1 (10 points): N≤2,000
Subtask #2 (90 points): original constraints

Example Input
3
3
1 1 1
1 1 1
3
3 0 0
10 0 0
3
3 3 3
3 2 1
Example Output
3
30
3

"""


def coins(total, cars, val):
    arr = list(zip(cars, val))
    arr.sort(key=lambda x: x[1])
    i = 0
    distance = 0
    coins = 0
    while (distance != total):
        if (total - distance < arr[i][0]):
            coins = coins + (total - distance) * arr[i][1]
            distance = total
        else:
            distance = distance + arr[i][0]
            coins = coins + arr[i][0] * arr[i][1]
            i = i + 1
    return coins


num = int(input())
for i in range(num):
    total = int(input())
    cars = list(map(int, input().split()))
    val = list(map(int, input().split()))
    print(coins(total, cars, val))
