"""
Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book, page  is always on the right side:

image

When she flips page , she sees pages  and . Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is  pages long, and she wants to turn to page , what is the minimum number of pages she will turn? She can start at the beginning or the end of the book.

Given  and , find and print the minimum number of pages Brie must turn in order to arrive at page .

Function Description

Complete the pageCount function in the editor below. It should return the minimum number of pages Brie must turn.

pageCount has the following parameter(s):

n: the number of pages in the book
p: the page number to turn to
Input Format

The first line contains an integer , the number of pages in the book.
The second line contains an integer, , the page that Brie's teacher wants her to turn to.

Constraints

Output Format

Print an integer denoting the minimum number of pages Brie must turn to get to page .

Sample Input 0

6
2
Sample Output 0

1
Explanation 0

If Brie starts turning from page , she only needs to turn  page:

Untitled Diagram(6).png

If Brie starts turning from page , she needs to turn  pages:

Untitled Diagram(3).png

Because we want to print the minumum number of page turns, we print  as our answer.

Sample Input 1

5
4
Sample Output 1

0
Explanation 1

If Brie starts turning from page , she needs to turn  pages:

Untitled Diagram(4).png

If Brie starts turning from page , she doesn't need to turn any pages:

Untitled Diagram(5).png

Because we want to print the minimum number of page turns, we print  as our answer.
"""

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    page = []
    first = 0
    last = 0
    if p == n or (n%2 == 1 and n-1 == p) :
        return 0
    for i  in range(0,n+1,2):
        page.append((i,i+1))
    for j in range(len(page)):
        if p in page[j]:
            first = j # 앞쪽에서부터 루프가 돌기 때문에 j는 반드시 앞에서 해당 페이지로 갈 수 있는 인덱스를 지목한다.
        else:
            last = len(page) -1 - first #끝에서 서칭하려면 전체 page 길이에서 인덱스 번호를 찾아가야하기 때문에 -1을 하고,
            # 끝자리에서 앞자리 값을 차감하면 끝에서 찾는 인덱스 번호가 완성된다.
    if first>last:
        return last
    else:
        return first 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
