'''
Spiral Matrix I
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
For example,
Given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
For example,
Given n = 3,
You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
import random
class Solution:
    def spairalMatrix(self, M):
        '''
        type ans: list
        type M: list
        '''
        ans = []
        m = len(M)
        n = len(M[0])
        lastRow = m
        lastCol = n
        circul = min(m, n)/2
        for i in range(0, int(circul)+1 ,1):

            for j in range(i, lastCol ,1):
                ans.append(M[i][j])

            for j in range(i+1 , lastRow, 1):
                ans.append(M[j][lastCol-1])
            lastCol -=1

            for j in range(lastCol-1, i-1, -1):
                ans.append(M[lastRow-1][j])
            lastRow -= 1

            for j in range(lastRow-1, i, -1):
                ans.append(M[j][i])


            
        print(ans)
c = Solution()
m = random.randint(1, 10)
n = random.randint(1, 10)
count = 1
M = []
l = []
for i in range(m):
    for j in range(n):
        l.append(count)
        count += 1
    m.append(l)
c.spairalMatrix(M)