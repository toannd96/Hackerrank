"""
Sami's spaceship crashed on Mars! She sends a series of SOS messages to Earth for help.

NASA_Mars_Rover.jpg

Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of Sami's SOS have been changed by radiation.

For example, Earth receives SOSTOT. Sami's original message was SOSSOS. Two of the message characters were changed in transit.

Function Description

Complete the marsExploration function in the editor below. It should return an integer representing the number of letters changed during transmission.

marsExploration has the following parameter(s):

s: the string as received on Earth
Input Format

There is one line of input: a single string, .

Note: As the original message is just SOS repeated  times, 's length will be a multiple of .

Constraints

 will contain only uppercase English letters, ascii[A-Z].
Output Format

Print the number of letters in Sami's message that were altered by cosmic radiation.

Sample Input 0

SOSSPSSQSSOR
Sample Output 0

3
Explanation 0

 = SOSSPSSQSSOR, and signal length . Sami sent  SOS messages (i.e.: ).

Expected signal: SOSSOSSOSSOS
Recieved signal: SOSSPSSQSSOR
Difference:          X  X   X
We print the number of changed letters.

Sample Input 1

SOSSOT
Sample Output 1

1
Explanation 1

 = SOSSOT, and signal length . Sami sent  SOS messages (i.e.: ).

Expected Signal: SOSSOS     
Received Signal: SOSSOT
Difference:           X
We print the number of changed letters, which is .

Sample Input 2

SOSSOSSOS
Sample Output 2

0
Explanation 2

Since no character is altered, we print 0.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.


def marsExploration(s):
    """
    해당 문제에서 SOS의 각 문자열 내의 값과 일치하지 않는 값을 카운트해서 return 해주면 되는 건데... 흠
    이 코드는 정말 깔끔하게 잘 작성된 예시다. 지금 내 코드는 파이썬을 파이썬스럽게 사용하지 못하고 있다.
    """
    # 누군가의 모범답안
    # return sum(s[i] != "SOS"[i%3] for i in range(len(s)))

    # 아마 내 답안은 이런 형태였을 것이다.
    res = 0
    sos = "SOS"
    for i in range(len(s)):
        if s[i] != sos[i % 3]:
            res += 1
        else:
            res += 0
    return res

    # 내 코드가 누군가가 봤을 때 이해하기는 더 편하겠지만, 간결한 코드라고하는 할 수 없다.
    # 특히 내가 떠올리지 못했던 부분은 sos[i%3]으로 사용하는 부분이다.
    # 아직 한~~참 멀었다.
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
