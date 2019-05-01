'''
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock
Input Format

The first line contains an integer , the number of socks represented in . 
The second line contains  space-separated integers describing the colors  of the socks in the pile.
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dic = {}
    ans = 0
    for i in ar:
        if i in dic:
            dic[i] +=1
        else:
            dic[i] = 1
 # Count same values using dictionary.    
    for j in dic:
        if dic[j] % 2 ==0:
            ans += dic[j] // 2
        else:
            ans += (dic[j]-1)//2
    return ans

 # if dicionary's values are odd numbers, we have to count those numbers subtract 1.
 # if the values are even numbers, divide those with 2.
 # (Caution) if you use '/' just one slash, python recognizes float number.
 # the return value is integer number. So, I use double slash.    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()