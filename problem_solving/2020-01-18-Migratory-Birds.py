"""
You have been asked to help study the population of birds migrating across the continent. Each type of bird you are interested in will be identified by an integer value. Each time a particular kind of bird is spotted, its id number will be added to your array of sightings. You would like to be able to find out which type of bird is most common given a list of sightings. Your task is to print the type number of that bird and if two or more types of birds are equally common, choose the type with the smallest ID number.

For example, assume your bird sightings are of types . There are two each of types  and , and one sighting of type . Pick the lower of the two types seen twice: type .

Function Description

Complete the migratoryBirds function in the editor below. It should return the lowest type number of the most frequently sighted bird.

migratoryBirds has the following parameter(s):

arr: an array of integers representing types of birds sighted
Input Format

The first line contains an integer denoting , the number of birds sighted and reported in the array .
The second line describes  as  space-separated integers representing the type numbers of each bird sighted.

Constraints

It is guaranteed that each type is 1, 2, 3, 4, or 5.
Output Format

Print the type number of the most common bird; if two or more types of birds are equally common, choose the type with the smallest ID number.

Sample Input 0

6
1 4 4 4 5 3
Sample Output 0

4
Explanation 0

The different types of birds occur in the following frequencies:

Type 1: 1 bird
Type 2: 0 birds
Type 3: 1 bird
Type 4: 3 birds
Type 5: 1 bird
The type number that occurs at the highest frequency is type , so we print  as our answer.

Sample Input 1

11
1 2 3 4 5 4 3 2 1 3 4
Sample Output 1

3
Explanation 1

The different types of birds occur in the following frequencies:

Type 1: 2
Type 2: 2
Type 3: 3
Type 4: 3
Type 5: 1
Two types have a frequency of , and the lower of those is type .
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    res = {1:0, 2:0, 3:0, 4:0, 5:0}
    for i in arr:
        if i in res:
            res[i] +=1
    return max(res, key=res.get) 
    # 이렇게 처리하면 값이 2개가 중복되었을 때, key값이 작은 값을 우선 출력하는 일을 어떻게 처리하는 거지?
    # 기존의 코드
    # res = {}
    # for i in arr:
    # if i in res:
    #   res[i] +=1
    # else:
    #   res[i] = 1
    # return max(res, key=res.get)
    # 이 코드로 실행 시, 테스트 케이스에서 10만 개를 돌렸을 때, failed가 발생한다.
    # 왜 틀린지 모르겠다.
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
