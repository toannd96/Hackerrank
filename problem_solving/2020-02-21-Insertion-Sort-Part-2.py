"""
In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?

Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.

In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.

For example, there are  elements in . Working from left to right, we get the following output:

3 4 7 5 6 2 1
3 4 7 5 6 2 1
3 4 5 7 6 2 1
3 4 5 6 7 2 1
2 3 4 5 6 7 1
1 2 3 4 5 6 7
Function Description

Complete the insertionSort2 function in the editor below. At each iteration, it should print the array as space-separated integers on a separate line.

insertionSort2 has the following parameter(s):

n: an integer representing the length of the array 
arr: an array of integers
Input Format

The first line contains an integer, , the size of .
The next line contains  space-separated integers .

Constraints



Output Format

On each line, output the entire array at every iteration.

Sample Input

6
1 4 3 5 6 2
Sample Output

1 4 3 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 3 4 5 6 2 
1 2 3 4 5 6 
Explanation

Skip testing  against itself at position . It is sorted.
Test position  against position : , no more to check, no change.
Print 
Test position  against positions  and :

, new position may be . Keep checking.
, so insert  at position  and move others to the right.
Print 
Test position  against positions  (as necessary): no change.
Print 
Test position  against positions : no change.
Print 
Test position  against positions , insert  at position  and move others to the right.
Print 
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.


def insertionSort2(n, arr):
    # 여기서 왜 insertion sort를 진행할 때, 1부터 시작을 하는가?
    # insertion sort의 시작 시, 대전제는 arr[0]은 정렬 되었다 보는 것이다.
    # for loop가 돌아가는 곳을 outer loop
    # while loop가 돌아가는 곳은 inner loop라 보는 것이다.
    # 예를 들어, arr = [7,8,5,4,2,6]이라는 배열이 있다 보자
    # arr[0]은 정렬되어 있다 보는 것이니, arr[0] = 7을 건너 뛰고 시작!
    # 그럼 for loop에서 정렬이 시작되는 부분은 1부터다.
    # j는 정렬된 값 중에 가장 큰 값을 가리킨다.
    # 정렬된 것이 없는 처음 시작 단계에선 j는 첫번째 값을 가리킨다.
    for i in range(1, n):
        key = arr[i]  # 정렬의 대상이 되는 비교할 값
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1  # 정렬된 값들의 제일 오른쪽 값
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]  # 여기서 값을 덮어 씌우지만, key에서 안전하게 보관하고 있다.
            j -= 1  # j를 감소시키는 이유는 이전에 정렬된 값들하고 비교하기 위해서다.
        arr[j+1] = key
        print(*arr)  # *arr은 받는 인자들을 순서대로 print하라는 뜻이다.


"""
for i in range(1,n):
    key = arr[i]
    j = i - 1
    while j>=0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key
"""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
