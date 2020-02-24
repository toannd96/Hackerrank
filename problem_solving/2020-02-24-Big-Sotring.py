"""
Consider an array of numeric strings where each string is a positive number with anywhere from  to  digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and print each element of the sorted array on a new line.

Function Description

Complete the bigSorting function in the editor below. It should return the sorted string array.

bigSorting has the following parameter(s):

unsorted: an unsorted array of integers as strings
Input Format

The first line contains an integer, , denoting the number of strings in .
Each of the  subsequent lines contains an integer string .

Constraints

Each string is guaranteed to represent a positive integer without leading zeros.
The total number of digits across all strings in  is between  and  (inclusive).
Output Format

Print each element of the sorted array on a new line.

Sample Input 0

6
31415926535897932384626433832795
1
3
10
3
5
Sample Output 0

1
3
3
5
10
31415926535897932384626433832795
Explanation 0

The initial array of strings is . When we order each string by the real-world integer value it represents, we get:

We then print each value on a new line, from smallest to largest.

Sample Input 1

8
1
2
100
12303479849857341718340192371
3084193741082937
3084193741082938
111
200
Sample Output 1

1
2
100
111
200
3084193741082937
3084193741082938
12303479849857341718340192371
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    # for i in sorted(unsorted, key=int):
        #sorted (value, key, reverse) 형태로 입력 가능
    #     i = int(i)
    #     print(i)
    # 내가 작성한 답도 print 하면 맞는데, 왜 답이 틀리다고 나올까?
    # 이걸 어떻게 return 형태로 답을 내어줄 수 있을까?
    return sorted(unsorted, key=lambda x: (len(x),x)) #lamda 뭔지도 모르는데, 일단 답을 맞추느라 타인의 답을 기용해서 작성했다.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
