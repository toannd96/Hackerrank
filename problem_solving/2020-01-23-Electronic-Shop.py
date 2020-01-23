"""
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica wants to spend as much as possible for the  items, given her budget.

Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.

For example, suppose she has  to spend. Three types of keyboards cost . Two USB drives cost . She could purchase a , or a . She chooses the latter. She can't buy more than  items so she can't spend exactly .

Function Description

Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget, or  if she cannot afford both items.

getMoneySpent has the following parameter(s):

keyboards: an array of integers representing keyboard prices
drives: an array of integers representing drive prices
b: the units of currency in Monica's budget
Input Format

The first line contains three space-separated integers , , and , her budget, the number of keyboard models and the number of USB drive models.
The second line contains  space-separated integers , the prices of each keyboard model.
The third line contains  space-separated integers , the prices of the USB drives.

Constraints

The price of each item is in the inclusive range .
Output Format

Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

Sample Input 0

10 2 3
3 1
5 2 8
Sample Output 0

9
Explanation 0

She can buy the  keyboard and the  USB drive for a total cost of .

Sample Input 1

5 1 1
4
5
Sample Output 1

-1
Explanation 1

There is no way to buy one keyboard and one USB drive because , so we print .
"""

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    # 내 코드는 테스트 케이스 절반이 정답으로 출력되지 않는다.
    # 왜 여기서 이중 for loop를 사용하는가?
    # 내 코드에 확신이 있었는데 어디서 틀렸는지 이해를 못하겠다.
    
    # res = []
    # for i in range(len(keyboards)):
    #     if i == n-1:
    #         res.append(keyboards[n-1])
    # for j in range(len(drives)):
    #     if j == m-1:
    #         res.append(drives[m-1])
    # if sum(res) <= b:
    #     return sum(res)
    # else:
    #     return -1

    keyboards.sort(reverse=True)
    drives.sort()
    res = -1
    for k in keyboards:
        for d in drives:
            if k+d > b:
                break
            if k+d > res:
                res = k+d
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
