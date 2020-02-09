"""
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.

For example, there are  sticks of lengths . The shortest stick length is , so we cut that length from the longer two and discard the pieces of length . Now our lengths are . Again, the shortest stick is of length , so we cut that amount from the longer stick and discard those pieces. There is only one stick left, , so we discard that stick. Our lengths are .

Function Description

Complete the cutTheSticks function in the editor below. It should return an array of integers representing the number of sticks before each cut operation is performed.

cutTheSticks has the following parameter(s):

arr: an array of integers representing the length of each stick
Input Format

The first line contains a single integer , the size of .
The next line contains  space-separated integers, each an  where each value represents the length of the  stick.

Output Format

For each operation, print the number of sticks that are present before the operation on separate lines.

Constraints

Sample Input 0

6
5 4 4 2 2 8
Sample Output 0

6
4
2
1
Explanation 0

sticks-length        length-of-cut   sticks-cut
5 4 4 2 2 8             2               6
3 2 2 _ _ 6             2               4
1 _ _ _ _ 4             1               2
_ _ _ _ _ 3             3               1
_ _ _ _ _ _           DONE            DONE
Sample Input 1

8
1 2 3 4 3 3 2 1
Sample Output 1

8
6
4
1
Explanation 1

sticks-length         length-of-cut   sticks-cut
1 2 3 4 3 3 2 1         1               8
_ 1 2 3 2 2 1 _         1               6
_ _ 1 2 1 1 _ _         1               4
_ _ _ 1 _ _ _ _         1               1
_ _ _ _ _ _ _ _       DONE            DONE

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):
    arr.sort()
    result = []
    i = 0
    while(i < n):
        result.append(n-i)
        i += arr.count(arr[i])  # 똑같은 값이 중복되면 그 값의 index는 제외하고 진행이 되어야한다.
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))  # 이 곳에서
    fptr.write('\n')

    fptr.close()
