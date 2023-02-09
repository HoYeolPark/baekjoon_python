#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#과제 안내신분..?
num = []
for i in range(1,31):
    num.append(i)

for i in range(28):
    num.remove(int(input()))
print(min(num))
print(max(num))


# In[ ]:


#나머지
a = []
for i in range(10):
    a.append(int(input())%42)
a = set(a) #set함수는 리스트 안에 있는 중복된 숫자를 제거해줌
print(len(a))


# In[ ]:


#평균
n = int(input())
subject = list(map(int, input().split()))
result = []

for i in range(n):
    result.append((subject[i]/max(subject))*100)
print(sum(result)/len(result))


# In[ ]:


#OX퀴즈
n = int(input())

for i in range(n):
    OX = str(input())
    result = 0
    cnt = 0
    for i in range(len(OX)):
        if OX[i] == 'O':
            cnt += 1
        else:
            cnt = 0
        result += cnt
    print(result)      


# In[ ]:


#평균은 넘겠지
c = int(input())

for i in range(c):
    point = list(map(int, input().split()))
    result = []
    average = sum(point[1:])/point[0]
    for j in range(1,len(point)):
        if point[j] > average:
            result.append(point[j])
    last = format((len(result)/point[0])*100, ".3f")
    print(f'{last}%')
        


# In[ ]:


#정수 N개의 합
def solve(a: list) -> int:
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans        

if __name__ == "__main__":
    n = list(map(int,input().split()))
    print(solve(n))


# In[ ]:


#아스키 코드
print(ord(str(input())))


# In[ ]:


#숫자의 합
n = int(input())
real = str(input())
sum1 = 0
for i in range(n):
    sum1 += int(real[i])
print(sum1)


# In[ ]:


#알파벳 찾기
a = str(input())
for i in range(97,123):
    print(a.find(chr(i)), end = ' ')


# In[2]:


#문자열 반복
n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    for j in range(len(b)):
        print(int(a)*b[j], end='')
    print()


# In[ ]:




