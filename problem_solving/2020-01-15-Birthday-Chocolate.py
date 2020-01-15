"""
Lily has a chocolate bar that she wants to share it with Ron for his birthday. Each of the squares has an integer on it. She decides to share a contiguous segment of the bar selected such that the length of the segment matches Ron's birth month and the sum of the integers on the squares is equal to his birth day. You must determine how many ways she can divide the chocolate.

Consider the chocolate bar as an array of squares, . She wants to find segments summing to Ron's birth day,  with a length equalling his birth month, . In this case, there are two segments meeting her criteria:  and .

Function Description

Complete the birthday function in the editor below. It should return an integer denoting the number of ways Lily can divide the chocolate bar.

birthday has the following parameter(s):

s: an array of integers, the numbers on each of the squares of chocolate
d: an integer, Ron's birth day
m: an integer, Ron's birth month
Input Format

The first line contains an integer , the number of squares in the chocolate bar.
The second line contains  space-separated integers , the numbers on the chocolate squares where .
The third line contains two space-separated integers,  and , Ron's birth day and his birth month.

Constraints

, where ()
Output Format

Print an integer denoting the total number of ways that Lily can portion her chocolate bar to share with Ron.

Sample Input 0

5
1 2 1 3 2
3 2
Sample Output 0

2
Explanation 0

Lily wants to give Ron  squares summing to . The following two segments meet the criteria:

image

Sample Input 1

6
1 1 1 1 1 1
3 2
Sample Output 1

0
Explanation 1

Lily only wants to give Ron  consecutive squares of chocolate whose integers sum to . There are no possible pieces satisfying these constraints:

image

Thus, we print  as our answer.

Sample Input 2

1
4
4 1
Sample Output 2

1
Explanation 2

Lily only wants to give Ron  square of chocolate with an integer value of . Because the only square of chocolate in the bar satisfies this constraint, we print  as our answer.
"""
import math
import os
import random
import re
import sys
from itertools import combinations
# Complete the birthday function below.
def birthday(s, d, m):
    # res = []
    # comb_list = []
    # comb_list = set(combinations(s,m))
    # for i in comb_list:
    #     if sum(i) == d:
    #         res.append(sum(i))
    # print(len(res))
    count = 0
    queue = s[:m-1] # 여기서 m-1이 의미하는 바가 무엇인가? queue는 여기서 단순 variables다.
                    # 이렇게 되면, s[m]번째 배열이 빠지지 않나? 안빠지네?
                    # m=3이라 하면, queue = s[:2], ele는 s[2:] 순회한다.
                    # 아, 여기서 바보짓했네 ㅋㅋㅋㅋㅋㅋㅋㅋ
                    # m=3이면 배열 내에서 3개까지 더해진다.
    for ele in s[m-1:]:
        queue.append(ele)
        if (sum(queue) == d):
            count += 1
        queue.pop(0)
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
