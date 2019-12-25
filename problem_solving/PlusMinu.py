"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Constraints



Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1         
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .


"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = [] #리스트 내 양의 정수 값을 받아올 리스트 변수 지정
    zero = [] # 리스트 내 값이 0인 요소 값을 받아올 리스트 변수 지정
    negative = [] #리스트 내 값이 음의 정수인 값을 받아올 리스트 변수 지정
    for i in range(len(arr)): #전체 리스트 순회를 위한 루프 설정
        if arr[i] > 0: # 리스트 내 요소 값이 양의 정수라면
            positive.append(arr[i]) #양의 정수 변수에 요소 추가
        elif arr[i] == 0 : # 0이라면
            zero.append(arr[i]) #0을 받는 리스트에 변수 지정
        else:
            negative.append(arr[i]) #그 외에 음수는 모두 음의 정수 변수에 추가
    print(round(len(positive)/len(arr),6), "\n", round(len(negative)/len(arr),6), "\n", round(len(zero)/len(arr),6))
    #여기서 새로 배운 사실은 파이썬 내에 round 라는 함수가 있다는 것이다. 이 함수는
    #round(<소수점 값이 있는 수>, <소수점 반올림 자릿수 지정>) 형태로 사용 가능하다는 것이다.
    #예를 들어 round(0.333333333333,4) 라는 값을 입력하면,
    #출력되는 값은 0.3333까지 자동 반올림되어 소수점 뒤 4번째자리까지 출력된다는 점이다.
    #새로 배운 사실 TMI...
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)