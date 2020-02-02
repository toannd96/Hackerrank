"""
You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

Append a lowercase English alphabetic letter to the end of the string.
Delete the last character in the string. Performing this operation on an empty string results in an empty string.
Given an integer, , and two strings,  and , determine whether or not you can convert  to  by performing exactly  of the above operations on . If it's possible, print Yes. Otherwise, print No.

For example, strings  and . Our number of moves, . To convert  to , we first delete all of the characters in  moves. Next we add each of the characters of  in order. On the  move, you will have the matching string. If there had been more moves available, they could have been eliminated by performing multiple deletions on an empty string. If there were fewer than  moves, we would not have succeeded in creating the new string.

Function Description

Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

appendAndDelete has the following parameter(s):

s: the initial string
t: the desired string
k: an integer that represents the number of operations
Input Format

The first line contains a string , the initial string.
The second line contains a string , the desired final string.
The third line contains an integer , the number of operations.

Constraints

 and  consist of lowercase English alphabetic letters, .
Output Format

Print Yes if you can obtain string  by performing exactly  operations on . Otherwise, print No.

Sample Input 0

hackerhappy
hackerrank
9
Sample Output 0

Yes
Explanation 0

We perform  delete operations to reduce string  to hacker. Next, we perform  append operations (i.e., r, a, n, and k), to get hackerrank. Because we were able to convert  to  by performing exactly  operations, we print Yes.

Sample Input 1

aba
aba
7
Sample Output 1

Yes
Explanation 1

We perform  delete operations to reduce string  to the empty string (recall that, though the string will be empty after  deletions, we can still perform a delete operation on an empty string to get the empty string). Next, we perform  append operations (i.e., a, b, and a). Because we were able to convert  to  by performing exactly  operations, we print Yes.

Sample Input 2

ashley
ash
2
Sample Output 2

No
Explanation 2

To convert ashley to ash a minimum of  steps are needed. Hence we print No as answer.
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.


def appendAndDelete(s, t, k):
    s_length = len(s)  # 문자열 s의 전체 길이
    t_length = len(t)  # 문자열 t의 전체 길이

    if s_length + t_length < k:
        return 'Yes'  # k의 값이 s와 t의 합보다 작으면 당연히 YES

    same = 0
    for s_l, t_l in zip(s, t):  # Zip함수는 동일환 개수로 이뤄진 자료형을 묶어주는 역할을 하는 함수다.
        if s_l == t_l:
            same += 1  # 자료형 갯수가 같은 것이 나올 때마다 same이 한 개씩 추가된다.
        else:
            break  # 다른 값이 출력되면 멈춘다.

    extra_s = s_length - same  # 문자열이 서로 다른 값의 수
    extra_t = t_length - same  # 문자열이 서로 다른 값의 수
    difference = extra_s + extra_t

    if difference <= k and difference % 2 == k % 2:  # 여기가 이해가 안되네
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
