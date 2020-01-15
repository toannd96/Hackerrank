"""
You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .

For example,  and . Our three pairs meeting the criteria are  and .

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

n: the integer length of array 
ar: an array of integers
k: the integer to divide the pair sum by
Input Format

The first line contains  space-separated integers,  and .
The second line contains  space-separated integers describing the values of .

Constraints

Output Format

Print the number of  pairs where  and  +  is evenly divisible by .

Sample Input

6 3
1 3 2 6 1 2
Sample Output

 5
Explanation

Here are the  valid pairs when :

(0,2) -> ar[0] + ar[2] = 1+2 = 3
(0,5) -> ar[0] + ar[5] = 1+2 = 3
(1,3) -> ar[1] + ar[3] = 3+6 = 9
(2,4) -> ar[2] + ar[4] = 2+1 = 3
(4,5) -> ar[4] + ar[5] = 1+2 = 3
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations 
# 여기서 어쩔 수 없이 내장 함수의 힘을 빌리긴 했는데, 내장 함수 없이 구현하려면 순열과 조합을 어떻게 구현할 수 있을까?
# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    sum_list = []
    res = []
    comb_list = []
    comb_list = combinations(ar, 2)
    for i in comb_list:
        sum_list.append(i[0] + i[1])
    for j in sum_list:
        if j % k ==0 :
            res.append(j)
    return len(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
