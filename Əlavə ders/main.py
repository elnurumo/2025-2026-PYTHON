# 11 Hedef
# 9 - cu
# 


# 10 kaspi
# 

# # 30

# s = input()
# s = s.split()
# s = '#'.join(s)
# s = s+'#'
# print(s)

# 30 --Mehdi
# 14 -- Mehemmed

# n = int(input())
# n = str(n)
# s = 0
# c = 0
# for i in n:
#     i = int(i)
#     if i%2!=0:
#         s = s + i
#         c = c + 1
# print(s,c)

# # 30

# s = input().split()
# # ['salam','necesen','sagol','yaxshiyam']
# s = '# '.join(s)
# s = s +'#'
# print(s)


# s = 0
# for i in range(1,91):
#     s = s + i
# print(s)

# sinaq 4



# # 29

# n = int(input())
# k = n%10
# f = 0
# while n>0:
#     q = n%10
#     if q != k:
#         f = 1
#     n = n//10
# if f == 1:
#     print('beraber deyil')
# else:
#     print('Beraberdir')

# 30

# s =input()
# f = s.split()
# for i in f:
#     print(len(i))

# 29

# n = int(input())
# s = 0
# c = 0
# while n>0:
#     q = n%10
#     if q%2!=0:
#         s = s + q
#         c = c + 1
#     n = n//10
# print(s,c)

# 30

# s = input().split() #'salam necesen sagol'
# s = '# '.join(s)
# s = s + '#'
# print(s

# n = int(input(),base=16)
# print(n)

# 25-30
# 


# 29

# n = int(input()) # 2222, 2232
# n = str(n)
# a = n[0]
# s = 0
# for i in n:
#     if a == i:
#         s = s + 1
# if s == len(n):
#     print('yes')
# else:
#     print('no')

# n = int(input())
# n =str(n)
# a = n[0]
# if n.count(a) == len(n):
#     print('Yes')
# else:
#     print('No')

# 30

# s = input().split() # 'salam necesen' ----> ['salam','necesen']
# for i in s:
#     print(len(i))


# sinaq 5
# 14


# # sinaq 4
# # 30
# s = input().split() #---> ['salam','necesen']
# for i in s:
#     print(len(i))

# 16




# 28,30,25,


# def f(x):
#     if x==1:
#         return 1
#     return x - f(x-1)

# print(f(5))


# sinaq 10-cu sinif guven




# # Sinaq 4
# # 28,30,29
# # Sinaq 2
# # 29,30


# # 29

# n = int(input())
# a = n%10
# f = 0
# while n>0:
#     q = n%10
#     if q!=a:
#         f = 1
#     n = n//10
# if f == 1:
#     print('Eyni deyil')
# else:
#     print('Eyni')


# n = int(input())
# n = str(n)
# if n.count(n[0]) == len(n):
#     print('Eyni')
# else:
#     print('Eyni deyil')


# # 30

# s = input().split() # 'salam necesen'
# # ['salam','necesen']
# for i in s:
#     print(len(i))

# 28

# # 29

# m = []
# for i in range(100,1000):
#     a = i//100
#     b = i%10
#     c = i//10%10
#     if a+b+c == 19:
#         m.append(i)
# print(m)


# # 30
# n = int(input())
# n = abs(n)
# c = 0
# h = 1
# while n>0:
#     q = n%10
#     c = c + q
#     h = h*q
#     n = n//10
# print(c+h)


# Sınaq 3
# 

# # 29

# n = int(input()) # 256
# n = str(n) # '256'
# m = max(n) # '6'
# s = 0 
# for i in n:
#     if i!=m:
#         s = s + int(i)
# print(s)



# # 30

# for i in range(111,1000,2):
#     a = i%10
#     b = i//10%10
#     c = i//100
#     if a%2==1 and b%2==1 and c%2==1:
#         print(i)


# n = int(input()) # 110 # 2-likden onluqa
# n = str(n)
# l = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + int(i)*2**l
#     l = l - 1
# print(onluq)



# n = int(input())
# n = str(n)
# n = '1'.join(n)
# n = int(n)
# print(n**2)


# a = [8,4,5,8,15,68,19,15,19]
# b = [8,19,15,5,2,367]
# s = []
# for i in a:
#     if b.count(i)>0 and s.count(i)==0:
#         s.append(i)
# print(len(s))

# n = input().split() # ['salam','necesen','sagol']
# b = []
# for i in n:
#     if i.count('a')>0:
#         b.append(i)
# b = ','.join(b)
# print(b)


# n = input().split() # ['salam' ,'necesen']
# b = []
# for i in n:
#     s = len(i)
#     b.append(s)
# print(min(b))

# 5

# s = 0
# for i in range(1000,10000):
#     a = i%10
#     b = i//10%10
#     c = i//100%10
#     d = i//1000
#     if a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
#         s = s + i
# print(s)

# n = int(input())
# k=n
# k = list(str(k))
# k.sort()
# k = "".join(k)
# k= int(k)
# if k==n:
#     print("yes")
# else:
#     print("no")

# n= input() #dsds21
# reqemler = "0123456789"
# for i in n:
#     if reqemler.count(i)==1:
#         n=n.replace(i,"a")
# print(n)


# n = int(input())
# s = 0
# for i in range(1,n+1):
#     if i%2==1 and n%i==0:   
#         s = s + i
# print(s)

# # 90

# n = input().split()
# s = 0
# for i in range(len(n)):
#     k = n[i]
#     if k[0] == '3' and k[len(k)-1] == '6':
#         s = s + i
# print(s)



# 29,30

# 29

# x = int(input())
# n = int(input())
# f = 1
# s = 1
# for i in range(1,n+1):
#     f = f * i
#     if i%2==0:
#         s = s + x**i/f
# print(s)


# # 30

# def simpleOrCompound(x):
#     f=0
#     for i in range(2,x//2+1):
#         if x%i==0:
#             f = 1
#     return f

# a = int(input())
# b = int(input())
# if 2<=a<b:
#     for i in range(a,b+1):
#         if simpleOrCompound(i) == 0:
#             print(i)



# # 112 toplu

# n = int(input())
# s = 0
# while n%10==0:
#     s = s + 1
#     n = n//10
# print(s)

# # 113
# n = int(input())
# f = 0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             f = 1
#     if f == 1:
#         print('Mürəkkəb ədəddir')
#     else:
#         print('Sadə ədəddir')

# 120

# x = int(input())
# n = int(input())
# s = 1
# f = 1
# for i in range(1,n+1):
#     f = f * i
#     if i%2==0:
#         s = s + x**i/f
# print(s)


# # 121

# s = 0
# for i in range(1,201):
#     if i%5==0 and i%3!=0:
#         s = s + 1
# print(s)


# n = int(input())
# if n>0:
#     f = 1
#     if n%2==0:
#         for i in range(1,n+1):
#             f = f * i
#     else:
#         f = n*n*2
#     print(f)

# # 123

# s = 0
# for i in range(100,1000):
#     a = i%10
#     b = i//10%10
#     c = i//100
#     if a+b+c>=12 and i%2==0 and i%5==0:
#         s = s + 1
# print(s)

# 124

# n = int(input())
# if n>0:
#     s = 0
#     k = -1
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#         s = s + k*(1/f**i)
#         k = -k
#     print(s)

# # # 128

# n = int(input()) # 240135
# b = []
# n = str(n)
# for i in n:
#     i = int(i)
#     if i%2!=0:
#         b.append(i)
# if len(b) == 0:
#     print('Ədəddə tək rəqəm yoxdur')
# else:
#     print(min(b))


# 129

# n = int(input(),base=16)
# print(n)


# n = input() # AA
# #             01
# rqmlr = '0123456789ABCDEF'
# #        0123456789101112131415
# onluq = 0
# L = len(n)-1
# for i in n:
#     onluq = onluq + rqmlr.find(i)*16**L
#     L = L-1
# print(onluq)


# # 29

# x = int(input())
# n = int(input())
# s = 1
# f = 1
# for i in range(2,n+1):
#     f = f * i
#     if i%2==0:
#         s = s + x**2/f
# print(s)


# 30

# def simpleOrCompound(x):
#     f = 0
#     for i in range(2,x//2+1):
#         if x%i==0:
#             f = 1
#     return f


# a = int(input())
# b = int(input())
# c = []
# if 2<=a<b:
#     for i in range(a,b+1):
#         if simpleOrCompound(i) == 0:
#             c.append(i)
# print(c)


# # 30

# def simpleOrCompound(x):
#     f = 0
#     for i in range(2,x//2+1):
#         if x%i == 0:
#             f = 1
#     return f


# a = int(input('a= ')) # 10 
# b = int(input('b= ')) # 20
# if 2<=a<b:
#     for i in range(a,b+1):
#         if simpleOrCompound(i) == 0:
#             print(i)


# 29,30


# 29

# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print('I rubdedir')
# elif x<0 and y>0:
#     print('II rubdedir')
# elif x<0 and y<0:
#     print('III rubdedir')
# elif x>0 and y<0:
#     print('IV rubdedir')
# else:
#     print('Kordinat bashlanghicindadir')



# # 30

# n = input()
# s = ''
# for i in range(0,len(n)):
#     if '0'<=n[i]<='9':
#         s = s + n[i]
#     else:
#         s = s + str(i)
# print(s)


# x =int(input())
# n = int(input())
# f = 1
# s = 1
# for i in range(1,n+1):
#     f = f * i
#     if i%2==0:
#         s = s + x**i/f
# print(s)



# # 89

# n = int(input())
# n = n+1
# while n%2==0 or n%3==0 or n%5==0:
#     n = n+1
# print(n)

# 90

# n = int(input())
# n = str(n)
# s = ''
# for i in n:
#     if i!='4' and i!='7':
#         s = s + i
# print(s)

# n = int(input())
# n = str(n)
# b = []
# for i in range(0,len(n)):
#     if n[i]!='4' and n[i]!='7':
#         b.append(i)
# b = ''.join(b)
# print(b)

# a = 123
# if a>0:
#     a = str(a)
#     print('salam')


# 29,30


# # 29

# a = int(input())
# b = int(input())
# while a!=b:
#     if a>b:
#         a = a - b
#     else:
#         b = b - a
# if a == 1:
#     print('Yes')
# else:
#     print('No')


# # 30

# s = input().split() # ['salam','alma','ananas']
# b = []
# for i in s:
#     c = i.count('a')
#     b.append(c)
# for i in s:
#     if i.count('a') == max(b) and max(b)!=0:
#         print(i)



# # 29

# n = input() # riyaziyyat
# b = []
# for i in n:
#     if b.count(i) == 0:
#         b.append(i)
# print(len(b))


# 30

# n = int(input())
# sade_vuruq = 2
# b = []
# while n>1:
#     if n%sade_vuruq==0:
#         n = n//sade_vuruq
#         if b.count(sade_vuruq) == 0:
#             b.append(sade_vuruq) 
#     else:
#         sade_vuruq = sade_vuruq+1
# print(b)


# 28,29,30




# # 89

# n = int(input()) # 2355
# h = 1
# n = str(n)
# for i in n:
#     i = int(i)
#     if i<5:
#         h=h*i
# print(h)

# # 90

# n = input() # Sdr34fgh5
# s = 0
# rqmlr = '0123456789'
# for i in n:
#     if rqmlr.count(i) == 1:
#         s = s + int(i)**2
# print(s)


# # 30

# n = input() # SalamAjan01
# #             01234567801
# s = ''
# rqml = '0123456789'
# for i in range(0,len(n)):
#     if rqml.count(n[i]) == 0:
#         s = s + str(i)
#     else:
#         s = s + n[i]
# n = s
# print(n)

# # 29

# x = float(input('x: '))
# y = float(input('y: '))
# if x>0 and y>0:
#     print('I rübdə yerləşir')
# elif x<0 and y>0:
#     print('II rübdə yerləşir')
# elif x<0 and y<0:
#     print('III rübdə yerləşir')
# elif x>0 and y<0:
#     print('IV rübdə yerləşir')


# 2024 qebul
# 26,28,29,30


# x = int(input())
# y = int(input())
# if x>0 and y>0:
#     print('I rübdədir')
# elif x<0 and y>0:
#     print('II rübdədir')
# elif x<0 and y<0:
#     print('III rübdədir')
# elif x>0 and y<0:
#     print('IV rübdədir')
# elif x == 0 or y == 0:
#     print('Heç bir rübdə deyil')

# # 30

# n = input() # salam01 --> 0123401
# n = list(n)
# rqmlr = '0123456789'
# for i in range(0,len(n)):
#     if rqmlr.count(n[i]) == 0:
#         n[i] = str(i)
# n = ''.join(n)
# print(n)


# 29

# 83741

# n = int(input())
# n = list(str(n))
# for i in range(len(n)):
#     n[i] = int(n[i])
# c = 0
# d = 0
# for i in range(0,len(n)-1):
#     c = c + n[i]
#     d = d + 1
#     s = (sum(n)-c)/(len(n)-d)
#     if n[i]>s:
#         print(n[i],end=' ')


# ,28,29,30


# # 29

# x = int(input()) # 8
# a = int(input())
# q = 1
# while q<x:
#     q = q*a
# if x == q:
#     print('Yes')
# else:
#     print('No')


# 30

# n = int(input())
# if 99<n<1000:
#     n = list(str(n))
#     n.sort()
#     n.reverse()
#     n = ''.join(n)
#     n = int(n)
#     print(n)

# n = int(input())
# s = ''
# for i in '9876543210':
#     for x in str(n):
#         if x == i:
#             s = s + x
# print(s)


# Sinaq 12

# 30

# def simpleOrCompound(x):
#     f = 'sadə'
#     for i in range(2,x//2+1):
#         if x%i == 0:
#             f = 'mürəkkəb'
#     return f

# a = int(input())
# b = int(input())
# if simpleOrCompound(a)=='sadə'==simpleOrCompound(b):
#     print('YES')
# else:
#     print('NO')


# 