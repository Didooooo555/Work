'''text = input().strip()

# Разбиваем строку на слова
words = text.split()

# Словарь для подсчета
freq = {}

# Подсчёт слов
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Находим слово с максимальной частотой
most_common = max(freq, key=freq.get)

print(most_common)'''




'''data = {"a": 1, "b": 2, "c": 3}

# Меняем местами ключ и значение
swapped = {value: key for key, value in data.items()}

print(swapped)'''



'''word = input().strip()

if word == word[::-1]:
    print("YES")
else:
    print("NO")'''





"""text = input().strip()
word = text.split()
n = int(input())
for i in word:
    if len(i) >= n:
        print(i)"""

#print(*(i**2 for i in range(10+1)))

"""a = int(input())
s = 0
b = 0
while s < a:
    s += 1
    b += s
    print(b)"""

#a = int(input())
#print('Even' if a%2==0 else 'Odd')

#a, b ,c = map(int,input().split())
#print(min(a, b, c))

'''a = input()
print(sum(map(int, a)))'''

#a = input()
#print('Yes' if a[::-1]==a else 'No')

'''a = input()
w = "aeiouAEIOU"
for i in w:
    a = a.replace(i, '*')
print(a)'''

#print(''.join(i for i in input() if i.lower() not in 'aeiou'))
#print(*('yes' if int(i)%2==0 else 'no' for i in input().split()))

'''a = input().split()
print(max(a,key=len))'''

'''n = int(input())
a, b = 1, 1
for i in range(n-2):
    a, b = b, a+b
    print(a)
    print(b)
print(b)'''

'''a = list(map(int,input().split()))
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(*a)'''

'''a, b = map(int,input().split())
s = 0
for i in range(a, b+1):
    s += i
print(s)'''

#a, b = map(int,input().split())
#print(sum(range(a,b+1)))

'''a = input().split()
a.reverse()
print(*a)'''

'''n = int(input())
a = list(map(int,input().split()))
print(sum(1 for i in a if i % 2 ==0))'''
'''a = (input())
print(int(a[::-1]))'''

'''a = int(input())
b = a//1000
c = a%1000
v = b%10+b//100+(b%100)//10
n = c%10+c//100+(c%100)//10
print("YES" if v == n else "NO")'''

#a, b, c = map(int,input().split())
#print("YES" if a+b > c and a+c > b and b+c > a else "NO")

#a = int(input())
#print("YES" if len(set(str(a))) == 4 else "NO")

'''a, b, c = input().split()

win = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

if a == b == c:
    print(0)
elif win[a] == b:
    print(1)
elif win[c] == a:
    print(3)
else:
    print(2)'''

'''from random import randint
s=0
n = int(input())
a = [0]* n
for i in range(n):
    a[i] = randint(-50,50)
    print(a[i], end=' ')
    if a[i]>0:
        s+=1
print(s, end='\n')'''

'''n = input()
print('yes' if sum(map(int, n))%3==0 else 'no')'''

'''from array import array
a = array('i', map(int,input().split()))
for i in range(len(a)):
    print(a[i],end=' ')'''

'''a = int(input())
b = a//6
c = (b+b)*2
print(b,c,b)'''

'''v = int(input())
t = int(input())
print((v*t)%109)'''

'''a = list(map(int,input().split()))
n=a.index(max(a))
m=a.index(min(a))
a[n], a[m] = a[m], a[n]
print(*a)'''

'''from array import array
from random import randint
n = int(input())
a = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j]=randint(0,1)
        print(a[i][j], end=' ')
    print()
s = 0
for i in range(n):
    for j in range(n):
        if i == j:
            s+=a[i][j]
print(s)'''

'''n = int(input())
if n%3==0 and n%5==0:
    print('lets go')
elif n%3==0:
    print('lets')
elif n%5==0:
    print('go')
else:
    print(n)'''

'''a = int(input())
s=0
for i in range(1,a+1):
    s+=1
    for j in range(1,s+1):
        print(j,end=' ')
    print()'''

'''a = int(input())
print(len(set(str(a))))'''

#print(int(input())+int(input()))


'''s = 0
a = int(input())
while a>0:
    a//=2
    s+=1
print(s)'''

'''a = int(input())
b = int(input())
if a > b:
    if a%2==0:
        print(a)
    else:
        print(b)
else:
    print('The end')'''

'''a = 10
s = 0
for i in range(a):
    s+=i
print(s)'''

'''a=0
while a<10:
    a+=1
    print(a)'''

'''from math import gcd
from math import lcm

a, b = 12, 18
print("gcd =", gcd(a, b))    # 6  EYOB
print("lcm =", lcm(a, b))    # 36 EKOE
print('lcm =', (a*b)//gcd(a, b)) #EKOE 2'''

'''a = int(input())
print(((10*a)-5)**2)'''


'''s = input().strip()

max_zeros = 0
current = 0

for char in s:
    if char == '0':
        current += 1
        if current > max_zeros:
            max_zeros = current
    else:
        current = 0

print(max_zeros)'''

'''a,b,c = map(int,input().split())
print(max(a,b,c)-min(a,b,c))'''


'''a = int(input())
s = 0
for i in range(a+1):
    s+=i
print(s)'''

'''a = int(input())
print(sum(i for i in range(1,a+1)))'''

#print(sum(i for i in range(1,int(input())+1)))

#print(pow(int(input()),2))

'''n = int(input())
a = list(map(int,input().split()))
b = []
v = []
for i in range(n):
    if i % 2 == 0:
        b.append(i) 
    else:
        v.append(i)
print(b)
print(v)
print('Yes' if len(b)>len(v) else 'No')'''


'''t = input()
print(len(set(t)))'''

'''n = int(input())
a = list(map(int,input().split()))
if sorted(a) == a:
    print(0)
else:
    print(sorted(a))'''

'''a = list(map(int,input().split()))
print('yes' if (max(a)-min(a))%2==0 else 'no')'''

'''a = list(map(int,input().split()))
b = []
for i in range(len(a)):
    if a[i]%2==0:
        continue
    b.append(a[i])
print(*b)
b_max = 0
m = 0
for j in range(len(b)-1):
    b_max = b[j]+b[j+1]
    if b_max%2==0:
        m+=1
print(m)'''

'''a = list(map(int,input().split()))
m = a.index(min(a))
print(m)
a[0], a[m] = a[m], a[0]
print(*a)'''


'''a = 2.7182818284590452353602875
b = str(a)
m = int(input())
if m == 0:
    print(round(a))
else:
    print(b[:2]+b[2:m+1])'''


'''a = list(map(int,input().split()))
for i in range(len(a)-1):
    if a[i]*a[i+1]<0:
        print('yes')
    else:
        print('no')'''

'''n = int(input())
a = list(map(int,input().split()))
d = True 
for i in range(1,n):
    if a[i]%2 == a[i-1]%2:
        d = False
        break
if d:
    print('yes')
else:
    print('no')'''

'''n = int(input())
a = list(map(int,input().split()))
m = False 
for i in range(1,n-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        m = True
        break
if m:
    print('yes')
else:
    print('no')'''


'''n = int(input())
a = list(map(int,input().split()))
k = True
s = 0
for i in range(1,n):
    if a[i]<=a[i-1]:
        s+=1
if s>1:
    print('no')
else:
    print('yes')'''


'''n = int(input())
a = list(map(int,input().split()))
f = False
t = sum(a)
k = 0
for i in range(n):
    r = t - k - a[i]
    if k == r:
        f = True
        break
    k += a[i]
if f:
    print('yes')
else:
    print('no')'''


'''n, k = map(int,input().split())
a = list(map(int,input().split()))
b = []
for i in range(n-1):
    print(a[i]+a[i+1])
    b.append(a[i]+a[i+1])
print(*b)
print(max(b)-min(b))'''


'''a = list(map(int,input().split()))
print(sum(set(a)))'''


'''a = [4,2,5,7,1,3]
a.sort(reverse=True)
print(a)'''


'''from math import gcd
a, b = map(int,input().split())
print((a*b)//gcd(a,b))'''



'''n = int(input())
arr = list(map(int, input().split()))

l = 0
r = len(arr) - 1
take_left = True  # флаг: True — слева, False — справа

b1 = []
b2 = []

for i in range (n):
    while l <= r:
        if take_left:
            b1.append(arr[l])
            l += 1      # "удалили" слева
        else:
            b2.append(arr[r])
            r -= 1      # "удалили" справа

        take_left = not take_left  # меняем сторону

if b1>b2:
    print(2)
elif b2>b1:
    print(1)
else:
    print(0)'''

    
'''a = list(map(int,input().split()))
l = 0
r = len(a)-1
t = True
while l<=r:
    if t:
        print('left:',a[l])
        l+=1#delete
    else:
        print('right:',a[r])
        r-=1#delete 
    t = not t'''
    
    
'''n = int(input())
s = 0
for i in range(1,n+1):
    if n%i==0:
        s+=i
print(s)'''

    
'''a = input()
print(a.count('0'))'''


'''a = input()
print('yes' if len(a) == len(set(a)) else 'no')'''

'''t = ''.join(input().split())
b = t.lower()
print('yes' if b[::-1]==b else 'no')'''

'''n = int(input())
a = list(map(int, input().split()))

m = max(a)                      # максимальный элемент
a = [i for i in a if i != m]    # удаляем все максимумы

print(max(a))                   # второй по величине'''


'''a = list(map(int,input().split()))
b = max(a)
a = [i for i in a if i!=b]
print(max(a))'''


'''a = input()
print(sum(map(int,a)))'''

'''a = list(map(int,input().split()))
l = 0
r = len(a)-1
t = True
while l<=r:
    if t:
        print('l:',a[l])
        l+=1
    else:
        print('r:',a[r])
        r-=1
    t = not t'''

'''a = list(map(int, input().split()))
a.sort(reverse=True)
print(*a)'''

'''a = int(input())-1
print(a//20+1)
print(a%20//4+1)'''
# a<b ; a%b=a
# a<b ; a//b=0

'''a = input()
if a.isdigit():
    a = int(a)
print(type(a))'''

'''a = input()
if a.isdigit():
    a = int(a)
else:
    print('error')
print(type(a))'''

'''print("my name {}, my old {}".format("Didar", "38"))'''

'''price = 2.34556
print("price: {:.2f}".format(price))'''


'''#изменяемые типы (mutable): list, dict, set
my_list = [3, 4, 5]
my_list.append(9)
print(my_list)

my_dict = {'a' : 3}
my_dict['b'] = 6
print(my_dict)

my_set = {4, 5, 6}
my_set.add(9)
print(my_set)
#неизменяемые типы (immutable): int, float, tuple, str'''


'''#List/dict comprehension

#List Comprehension (списковые включения): [expr for i in iterable if condition]
s = [x*x for x in range(10) if x%2==0]
print(s)

#dict comprehension (словарные включения): {key: value for i in iterable if condition}
d = {x: x*x for x in range(5)}
print(d)'''

'''name = 'Hello Didar'
name2 = ['Hello', 'Didar']
print(name.endswith('Didar'))
print(name.startswith('Hello'))
print('-'.join(name2))'''

'''def f(a,b):
    while len(a) < b:
        a = "_" + a + "_"
        print(a)
    return a
print(f("hi", 6))'''


a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)

if b > c and b > a:
    print(b)

else:
    print(c)