#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#나이순 정렬
list1 = []
for i in range(int(input())):
    x, y = map(str, input().split())
    list1.append([x, y])

for i in range(len(list1)):
    list1[i][0] = int(list1[i][0])
        
list1.sort(key = lambda x: x[0])

for i in range(len(list1)):
    print(list1[i][0], list1[i][1], end= ' ')
    print()


# In[ ]:


#좌표 압축(시간 초과)
import sys

n = int(input())
point = list(map(int, sys.stdin.readline().split()))

point2 = list(set(point))
num = 0
result = []

for i in range(n):
    for j in range(len(point2)):
        if point[i] > point2[j]:
            num += 1
    result.append(num)
    num = 0

for i in range(len(result)):
    print(result[i], end=' ')


# In[ ]:


#좌표 압축
import sys

n = int(input())
point = list(map(int, sys.stdin.readline().split()))

point2 = sorted(list(set(point)))

dic = {point2[i]: i for i in range(len(point2))}

for i in point:
    print(dic[i], end = ' ')


# In[ ]:


#팩토리얼
def fact(n: int):
    if n == 0:
        return 1
    else:
        multi = fact(n-1)
        result = n * multi
        return result
    
if __name__ == "__main__":
    n = int(input())
    print(fact(n))
    


# In[ ]:


#피보나치 수 5
def pivo(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = pivo(n-1) + pivo(n-2)
        return result
    
if __name__=="__main__":
    n = int(input())
    print(pivo(n))


# In[ ]:


#재귀의 귀재
def recursion(s, l, r):
    global cnt
    cnt += 1
    
    if l >= r:
        return 1
    elif s[l] != s[r]: 
        return 0
    else:
        return recursion(s, l+1, r-1)  

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

if __name__=="__main__":
    for i in range(int(input())):
        cnt = 0
        x = str(input())
        print(isPalindrome(x), cnt)


# In[ ]:


#숫자 카드(시간 초과) -> 입력을 set으로 해주면 시간 초과 방지할 수 있음
# import sys 

# n = int(input())
# n_card = list(map(int, sys.stdin.readline().split()))

# m = int(input())
# m_card = list(map(int, sys.stdin.readline().split()))


# cnt = 0
# result = []
# for i in range(m):
#     for j in range(n):
#         if m_card[i] == n_card[j]:
#             cnt += 1
#     result.append(cnt)
#     cnt = 0
    
# for k in range(len(result)):
#     if result[k] > 0:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

import sys 

n = int(input())
n_card = set(map(int, sys.stdin.readline().split()))

m = int(input())
m_card = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    if m_card[i] in n_card:
        print(1, end=' ')
    else:
        print(0, end=' ')


# In[ ]:


#문자열 집합
n, m = map(int, input().split())
n_list = []
m_list = []
result = 0

for i in range(n):
    n_list.append(str(input()))
for j in range(m):
    m_list.append(str(input()))
for k in range(m):
    if m_list[k] in n_list:
        result += 1
print(result)


# In[ ]:


#나는야 포켓몬 마스터 이다솜
import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
pocket_books = {}
pocket_books2 = {}

for i in range(1, n+1):
    name = input().strip()
    pocket_books[name] = i # 'dsf' : 1
    pocket_books2[str(i)] = name # '1' : 'dsf'
    
for j in range(m):
    result = input().strip()
    if result.isdigit():
        print(pocket_books2[result])
    else:
        print(pocket_books[result])


# In[ ]:


#숫자카드2
import sys 
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

dic = dict()

for i in n_list:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in m_list:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')


# In[ ]:


#꼬마 정민
a,b,c = map(int,input().split())
print(a+b+c)


# In[ ]:


#듣보잡
n, m = map(int, input().split())
dic = dict()
for i in range(n+m):
    a = str(input())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

result_list = []
for key, value in dic.items():
    if value == 2:
        result_list.append(key)
result_list.sort()
print(len(result_list))
for j in range(len(result_list)):
    print(result_list[j])
        


# In[ ]:


#대칭 차집합
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
a_dic = dict()
b_dic = dict()
result = []

for i in a_list:
    a_dic[i] = 1
for j in b_list:
    b_dic[j] = 1
    
for k in a_list:
    if k in b_dic:
        b_dic[k] = 0
for n in b_list:
    if n in a_dic:
        a_dic[n] = 0

for key, value in b_dic.items():
    if value > 0:
        result.append(key)
for key, value in a_dic.items():
    if value > 0:
        result.append(key)
print(len(result))


# In[5]:


#서로 다른 부분 문자열의 개수
s = str(input())

s_list = []

for i in range(len(s)):
    for j in range(len(s)):
        s_list.append(s[i:i+j])
print(len(set(s_list)))


# In[ ]:




