import math
import numpy as np

n = 1000000000
A = []
sum = 0
max = 0
k = 0
division = 0
for i in range(n, 0, -1):
    if math.sqrt(i) == int(math.sqrt(i)):
        edge = int(math.sqrt(i))
        break

for i in range(edge, 0, -1):
    A.append(i * i)

if(n in A):
    print(1)
while(sum < n):
    for i in range(0, len(A)):
        if(A[i] * 2 == n or A[i] * 2 == n - 1):
            max = A[i]
        elif(max < A[i] and A[i] <= (n - sum)):
            max = A[i]
    print(max)
    division = int((n - sum) / max)
    for i in range(0, division):
        sum += max
        k += 1
    if((n - sum) <= 3):
        k += n - sum
        sum += n - sum
    max = 0

print(A)
print(sum, k)
