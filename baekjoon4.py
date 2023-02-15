#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#부녀회장이 될테야 -> DP
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    floor = [i for i in range(1, n+1)]
    
    for i in range(k):
        for j in range(1, n):
            floor[j] += floor[j-1]
    print(floor[-1])


# In[ ]:


#설탕 배달 -> 그리드
n = int(input())

result = -1

num = n//5
check = n%5

if check == 0:
    result = num
elif check == 1 and num >= 1:
    result = num + 1
elif check == 2 and num >= 2:
    result = num +2
elif check == 3:
    result = num + 1
elif check == 4 and num >= 1:
    result = num + 2
    
print(result)


# In[ ]:


#큰 수 A + B
A, B = map(int,input().split())
print(A + B)


# In[ ]:


#분수 찾기  -> 이건 이해가 잘 안가네
x = int(input())
c = 1
while x > c:
    x -= c
    c += 1
if c % 2 == 0:
    print(f"{x}/{1+c-x}")
else:
    print(f"{1+c-x}/{x}")


# In[ ]:


#행렬 덧셈
import sys
import numpy as np

list1 = []
list2 = []
n, m = map(int, sys.stdin.readline().split())

for i in range(n):
    list1.append(list(map(int,sys.stdin.readline().split())))
for i in range(n):
    list2.append(list(map(int,sys.stdin.readline().split())))
list1 = np.array(list1)
list2 = np.array(list2)
result = list1 + list2
for i in range(n):
    print(result[i])


# In[ ]:


#수 정렬하기
n = int(input())
num = []

for i in range(n):
    num.append(int(input()))
num = sorted(num)

for i in range(n):
    print(num[i], sep='\n')


# In[ ]:


#대표값2
num = []

for i in range(5):
    num.append(int(input()))
num = sorted(num)
aver = int(sum(num)/len(num))
print(aver, sep='\n')
print(num[int((len(num)//2))])


# In[ ]:


#커트라인
n, k = map(int, input().split())
x = list(map(int, input().split()))

x = sorted(x)
print(x[-k])


# In[ ]:


#수 정렬하기2 1방법대로 하면 시간 초과
import sys
n = int(input())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))
num = sorted(num)

for i in range(n):
    print(num[i], sep='\n')


# In[ ]:


#수 정렬하기3 2방법대로 하면 메모리 초과
import sys
n = int(input())
num = [0] * 10001

for i in range(n):
    input_num = (int(sys.stdin.readline()))
    num[input_num] = num[input_num]+1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i, sep='\n')
    


# In[ ]:


#통계학 최빈값에서 Counter.most_common 사용해야함
from collections import Counter
import sys

n = int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))
num = sorted(num)

print(round(sum(num)/n))
print(num[len(num)//2])

mode = Counter(num).most_common()
if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
    
print(max(num)-min(num))


# In[ ]:


#소트인사이드
n = list(input())
n.sort(reverse = True)
n = "".join(n)
print(n)


# In[17]:


#좌표 정렬하기 lambda 사용하기

n = int(input())
list1 = []
for i in range(n):
    x, y = map(int,input().split())    
    list1.append([x, y])
list1.sort(key=lambda x: (x[0], x[1]))
for i in range(n):
    print(list1[i][0], list1[i][1], end=' ')
    print()


# In[ ]:


#좌표 정렬하기 lambda 사용하기

n = int(input())
list1 = []
for i in range(n):
    x, y = map(int,input().split())    
    list1.append([x, y])
list1.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    print(list1[i][0], list1[i][1], end=' ')
    print()


# In[27]:


#단어 정렬
list1 = []
for i in range(int(input())):
    list1.append(str(input()))
    
list2 = list(set(list1))
list2.sort(key=lambda x:(len(x),x))

for i in range(len(list2)):
    print(list2[i])


# In[ ]:




