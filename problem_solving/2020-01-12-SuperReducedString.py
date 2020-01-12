"""
Steve has a string of lowercase characters in range ascii[‘a’..’z’]. He wants to reduce the string to its shortest length by doing a series of operations. In each operation he selects a pair of adjacent lowercase letters that match, and he deletes them. For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. If the final string is empty, print Empty String

Function Description

Complete the superReducedString function in the editor below. It should return the super reduced string or Empty String if the final string is empty.

superReducedString has the following parameter(s):

s: a string to reduce
Input Format

A single string, .

Constraints

Output Format

If the final string is empty, print Empty String; otherwise, print the final non-reducible string.

Sample Input 0

aaabccddd
Sample Output 0

abd
Explanation 0

Steve performs the following sequence of operations to get the final string:

aaabccddd → abccddd → abddd → abd
Sample Input 1

aa
Sample Output 1

Empty String
Explanation 1

aa → Empty String
Sample Input 2

baab
Sample Output 2

Empty String
Explanation 2

baab → bb → Empty String
"""

# 인접한 행렬을 어떻게 처리할 것인가에 대한 물음

# 내가 접근했던 풀이법

"""
    res = []
    dic = {}
    for i in range(len(s)):
        if s[i] in dic:
            dic[s[i]] +=1
        else:
            dic[s[i]] = 1

    for j in dic:
        if dic[j] % 2 != 0:
            res.append(j)
        else:
            res.append('')
            
    if ''.join(res) == '':
        return 'Empty String'
    else:
        return ''.join(res)
    # 이 경우, 행렬의 순서가 지켜지지 않는 문제가 발생한다.
    # 갯수 세는 부분이 포인트는 아니다.
    # 중요한 건 인접한 중복된 문자를 어떻게 삭제하는 코드를 작성할 것인지가 관건이다.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):

    res = [] # stack
    for c in s:
        # 여기가 제일 이해되지 않는 대목이다.
        if res and res[len(res)-1] == c: # peek what's on top
        # 이런 느낌인가보다
            res.pop()
        else:
            res.append(c)    
    res = ''.join(res)
    return res or 'Empty String'

'''
예를 들어, res = [a,b]인데, 이 경우 s의 다음 값이 b라면 인접한 값이 같기 때문에 배열에 포함된 값을 제거해야된다
'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
