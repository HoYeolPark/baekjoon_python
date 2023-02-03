#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#터렛
import sys
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())

    d = ((x2-x1)**2 + (y2-y1)**2)*0.5
    add = r1+r2
    sub = r1-r2
    if sub < 0:
        sub = r2-r1
    
    if (d == 0) and (sub == 0):
        print(-1)
    elif (d==add) or (d==sub):
        print(1)
    elif (d<add) and (d>sub):
        print(2)
    else:
        print(0)
    


# In[ ]:


#??!
a = str(input())

print('%s??!'%(a))


# In[ ]:


#chess
chess = [1, 1, 2, 2, 2, 8]
real = list(map(int, input().split()))

for i in range(len(chess)):
    print(chess[i]-real[i],end=" ")
    


# In[ ]:


# 나머지
a, b, c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)


# In[ ]:


#곱셈
a = int(input())
b = int(input())
print(a * (b%10))
print(a * ((b//10)%10))
print(a * (b//100))
print(a * b)


# In[ ]:


#개
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")


# In[ ]:


#두 수 비교하기
a, b = map(int, input().split())

if a > b:
    print('>')
else:
    if a < b:
        print('<')
    else:
        print('==')


# In[ ]:


test = int(input())

if 90 <= test <= 100:
    print('A')
elif 80 <= test < 90:
    print('B')
elif 70 <= test < 80:
    print('C')
elif 60 <= test < 70:
    print('D')
else:
    print('F')


# In[ ]:


#윤년
a = int(input())
if (a%4 == 0) and ((a%100 != 0) or (a%400 == 0)):
    print(1)
else:
    print(0)
                   


# In[ ]:


#사분면 고르기
x = int(input())
y = int(input())

if (x > 0) and (y > 0):
    print(1)
elif (x > 0) and (y < 0):
    print(4)
elif (x < 0) and (y > 0):
    print(2)
else:
    print(3)


# In[ ]:


#알람시계
h, m = map(int, input().split())
if (1<= h < 24) and (0 <= m <= 44):
    print(h-1,m+15)
elif (1<= h < 24) and (m > 44):
    print(h, m-45)
elif(h==0) and (0 <= m <= 44):
    print(23, m+15)
elif(h==0) and (m > 44):
    print(0, m-45)


# In[ ]:


#오븐 시계
a, b = map(int, input().split())
c = int(input())
d = b+c

if d >= 60:
    a += d//60
    d = d%60
if a >= 24:
    a = a%24
print(a, d)
        


# In[ ]:


#주사위 세개
a, b, c = map(int, input().split())
if a==b==c:
    print(10000 + a*1000)
elif a==b!=c or a==c!=b:
    print(1000 + a*100)
elif b==c!=a:
    print(1000 + b*100)
else:
    if a>b:
        if a>c:
            print(a*100)
        else:
            print(c*100)
    else:
        if b>c:
            print(b*100)
        else:
            print(c*100)


# In[ ]:


#구구단
n = int(input())

for i in range(1,10):
    print(f"{n} * {i} =", end = " ")
    print(n*i)


# In[ ]:


#A+B
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b)


# In[ ]:


#합
n = int(input())
a = 0
for i in range(n+1):
    a += i
print(a)


# In[ ]:


X = int(input())
N = int(input())
result = 0
for i in range(N):
    a, b = map(int, input().split())
    result += (a*b)
if X == result:
    print("Yes")
else:
    print("No")


# In[ ]:


#빠른 A+B
import sys

T = int(input())
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


# In[ ]:


#A+B -7
import sys

T = int(input())
for i in range(1,T+1):
    a, b = map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {a+b}')
    


# In[ ]:


#A+B -8
import sys

T = int(input())
for i in range(1,T+1):
    a, b = map(int,sys.stdin.readline().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')    


# In[ ]:


#별 찍기 - 1
n = int(input())
for i in range(1,n+1):
    print('*'*i)


# In[ ]:


#별 찍기 - 2
n = int(input())
for i in range(1, n+1):
    print(' '*(n-i),end='')
    print('*'*i)


# In[ ]:


#A+B -5
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0: 
        break
    else:
        print(a+b)


# In[ ]:


#A+B -4
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
        


# In[ ]:


N = int(input())
result = N
count = 0
a = 0
b = 0
c = 0
while True:
    a = N//10 
    b = N%10
    c = a + b
    N = b*10 + c%10
    count += 1
    if result == N:
        break
    else:
        continue
print(count)


# In[ ]:


#개수 세기
import sys

n = int(input())
num = list(map(int, input().split()))
b = int(input())

cnt = 0
for i in range(len(num)):
    if num[i] == b:
        cnt += 1
print(cnt)


# In[ ]:


#X보다 작은 수
N, X = map(int, input().split())
num2 = list(map(int, input().split()))

for i in range(N):
    if num2[i] < X:
        print(num2[i], end=' ')

    


# In[ ]:


#최소, 최대
N = int(input())
num = list(map(int, input().split()))

print(min(num), max(num))


# In[ ]:


#최댓값
num10 = []
for i in range(9):
    num10.append(int(input()))

maximum = max(num10)                 
for i in range(9):
    if maximum == num10[i]:
        print(maximum, i+1)
    


# In[ ]:


#과제 안내신분...?
num = []
for i in range(28):
    num.append(int(input()))

count = 30 
result = []
for i in range(1,31):
    for j in range(28):
        
    result.append

