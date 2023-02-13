#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#단어 공부
word = input().upper()
word_list = list(set(word))
count_list = []

for i in word_list:
    count_list.append(word.count(i))

if count_list.count(max(count_list)) > 1:
    print('?')

else:
    print(word_list[(count_list.index(max(count_list)))])


# In[ ]:


#단어의 개수
word = list(map(str,input().split()))

print(len(word))


# In[ ]:


#상수
a, b = map(str, input().split())

reverse_a = a[::-1]
reverse_b = b[::-1]

if int(reverse_a) > int(reverse_b):
    print(int(reverse_a))
else:
    print(int(reverse_b))        


# In[ ]:


#다이얼
word = input()
number = 0

for i in range(len(word)):
    if word[i] == 'A' or word[i] == 'B' or word[i] == 'C':
        number += 3
    elif word[i] == 'D' or word[i] == 'E' or word[i] == 'F':
        number += 4
    elif word[i] == 'G' or word[i] == 'H' or word[i] == 'I':
        number += 5
    elif word[i] == 'J' or word[i] == 'K' or word[i] == 'L':
        number += 6
    elif word[i] == 'M' or word[i] == 'N' or word[i] == 'O':
        number += 7
    elif word[i] == 'P' or word[i] == 'Q' or word[i] == 'R' or word[i] == 'S':
        number += 8
    elif word[i] == 'T' or word[i] == 'U' or word[i] == 'V':
        number += 9
    elif word[i] == 'W' or word[i] == 'X' or word[i] == 'Y' or word[i] == 'Z':
        number += 10
print(number)

#다른 사람 풀이
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)



# In[ ]:


#크로아티아 알파벳
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']


# In[ ]:


#그룹 단어 체커
n = int(input())


# In[ ]:


#손익분기점
a,b,c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)


# In[ ]:


#벌집
n = int(input())
cir = 1
cnt = 1

if n == 1:
    print(1)
else:
    while cir < n:
        cir += (cnt*6)
        cnt += 1
    print(cnt)


# In[ ]:


#달팽이는 올라가고 싶다.
a, b, v = map(int,input().split())

result = 0
cnt = 0
while True:
    result += a
    cnt += 1
    if result >= v:
        break
    else:
        result -= b
print(cnt)

#시간 초과나서 다시 도전
a, b, v = map(int,input().split())

if (v-b) % (a-b) == 0:
    print((v-b) // (a-b))
else:
    print((v-b) // (a-b) + 1)


# In[23]:


#ACM 호텔
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    ho = n // h
    
    if n % h == 0:
        floor = h
    else:
        ho += 1
    if ho < 10:
        print(f'{floor}0{ho}')
    else:
        print(f'{floor}{ho}')



# In[ ]:




