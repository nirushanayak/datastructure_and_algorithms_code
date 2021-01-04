"""
For positive integers a and b, we say that a fraction ab is good if it is equal to mm+1 for some positive integer m.

You are given an integer N. Find the number of pairs of integers i,j such that 1≤i,j≤N and the fraction ii+1⋅j+1j is good.

Input
The first and only line of the input contains a single integer N.

Output
Print a single line containing one integer ― the number of pairs of integers i,j (1≤i,j≤N) such that ii+1⋅j+1j is good.

Constraints
1≤N≤1,000,000
Subtasks
Subtask #1 (5 points): 1≤N≤2,000
Subtask #2 (10 points): 1≤N≤100,000
Subtask #3 (85 points): original constraints

Example Input
5
Example Output
8
Explanation
The following eight pairs (i,j) give good fractions: (1,2), (1,3), (2,3), (2,4), (2,5), (3,4), (3,5) and (4,5).


"""
import itertools
from fractions import Fraction

def fractions(s):
    s = [i for i in range(1, s + 1)]
    print(s)
    pairs = list(itertools.combinations(s, 2))
    count = 0
    for pair in pairs:
        if Fraction(pair[0]*(pair[1]+1),(pair[0]+1)*pair[1]).numerator +1 == Fraction(pair[0]*(pair[1]+1),
                                                                                      (pair[0]+1)*pair[1]).denominator:
            count = count+1
    return count



print(fractions(5))
