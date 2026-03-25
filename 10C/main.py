# 2.5
# 55,60,63,
# 37,68,61,58,
# 44,59,71,51,83,84,86,87,88,89,65,
# 69,74



# Alqoritm
# 
# 115,116,120,129,117

# 10.5
# 42,44


# login
# print('Hello world')
# a = 5
# b = 4
# print(a+b) # 9
# print('450'+'12') # ab
# print('a+b') # a+b
# login



# a = ['Ramal','Mehdi','Nihad','Ferid','Fuad','Əlihüseyin','Murad']
# # #     0       1        2       3       4        5          6 index
# for i in range(1,100,2):
#     print(i)


# If else
# 30


# a = input() #5
# b = input() #6
# c = input() #2
# print(c+a+b)  # 256





# a = 2
# b = 'python'
# print(str(a+a)+int(b))

# str str()
# int  int()



# print(5,7,4)

# print(5,end=' ')
# print(6,end=' ')
# print(7)




# a = [20,30,-100,7,8,90,556]
# maximum = a[0]
# for x in a:
#     if maximum<x:
#         maximum = x
# maximum2 = a[0]
# for i in a:
#     if maximum2<i and i!=maximum:
#         maximum2 = i
# print(maximum2)




#    0 1 2 3
#  for , while
# for x in a:
#     print(x)
# b = max(a)
# print(b)


# a = [12,1,23,45]
# min = a[0]
# for i in a:
#     if min>i:
#         min = i
# print(min)

# print(min(a))

# polindrom
# 121, 56, 878,565, 4554, 1221

# while
# # 1-ci üsul
# n = int(input()) # 257
# if 99<n<1000:
#     a = n//100
#     c = n%10
#     if a == c:
#         print('yes')
#     else:
#         print('no')

# a = int(input())
# a = str(a)
# b = a[::-1]
# if a == b:
#     print('Yes')
# else:
#     print('No')


# str, list

# str methods 7
# upper()
# lower()
# capitalize()
# count()
# strip()
# replace()
# find()


# list methods 7
# append()
# insert()
# remove()
# index()
# count()
# sort()
# reverse()

# n = 'salam'
# n = list(n)
# n.reverse()
# print(n)

# a = 'salam'
# c = a.count('a')
# m = max(a)
# print(c)

# n = '        elnur     '
# n = n.strip()
# print(n)

# a= 'Elnur'
# a = a.replace('nur','mir')
# print(a)

# if else
# ortaq
# a = [ 61,62,50,52,70,65,43,51,76,45,22,23,24,81,68,40,85,80,72,90,93,94,56,57,71,77]
# a = a.count()
# print(a)


# def ferid():
#     b = 5


# print(ferid())

# n = int(input())
# a = int(input())
# b= int(input())
# if a<b:
#     if n>b:
#         print('Sağında')
#     elif n<a:
#         print('Solunda')
#     elif a<=n<=b:
#         print('Daxilinde')
# else:
#     print('[a,b] yanlış daxil edilib')



# a = 'salam'
# b = a.find('a',2,len(a))
# print(b)


# For, While 
# a = 'Salam'

# for i in range(1,100,2):
#     print(i,'.',a,sep='')

# for i in a:
#     print(i)
# for i in range(0,len(a)):
#     print(a[i])


# while

# s = 1+2+3+4...+89+90+91

# n = 91
# i = 1
# s=0
# while i<=91:
#     s = s + i
#     i = i + 1
# print(s)

# EBOB
# a = 24
# b = 36
# while a!=b:
#     if a>b:
#         a = a - b
#     else:
#         b = b - a
# print(a)

# # EKOB
# a = 24
# b = 36
# c = a*b
# while a!=b:
#     if a>b:
#         a = a - b
#     else:
#         b = b - a
# print(c//b)

# a = [-2,-30,-20,-10,-4,-5,-15]
# maxi = a[0]
# for i in a:
#     if maxi>i:
#         maxi = i
# print(maxi)

# m = max(a)
# print(m)

# a = ['a','aa','ab','aabc','ac'] # ASCII
# #     0   01   01   0123   01
# print(max(a))

# a = [2,3,4,5,3,4.4]
#    0 1 2 3 4
# a.append()
# a.append(10) # listin sonuna data elave eliyir
# a.remove()
# a.remove(3) # listin içindəki ilk tapdığı 3 -ü siləcək
# a.insert() # luistin daxilində istədiyim indexinə əlavə edir
# a.insert(3,25) # [2,3,4,25,5,3]
# a.sort() # artan sırayla düzür
# a.reverse() # listi tərsinə çevirir
# a = a.count(4) # lsitin daxilindeki 4 ededinin sayin qaytarir
# a = a.index(3) # ilk tapdigi 3 -un indexini qaytarir
# print(a)


# split vs list

# Qessab -- list str---->list
# a = 'salam necesen'
# a = list(a)
# print(a)

# # split ---- str ---> list
# a = 'salam necesen'
# a = a.split(' ')
# for i in range(len(a)):
#     if a[i] == 'salam':
#         a[i] = a[i].split('a')
#         a[i] = ''.join(a[i])
#     else:
#         a[i] = a[i].split('e')
#         a[i] = ''.join(a[i])
# a = ' '.join(a)
# print(a)

# # join list----> str
# a = ['051','391','23','33']
# a = '-'.join(a)
# print(a)


# a = '256' # int
# b = '16.0' # float
# print(a+b)



# Etrafli
# 118,122,124
# 126,121,119,109


# # 103

# n = int(input()) # 5665
# a = n//100
# b = n%100
# if a==b:
#     print('Beraberdir')
# else:
#     print('Beraber deyil')


# # 104

# n = int(input()) # 256
# n = abs(n)
# if 99<n<1000:
#     a = n%10
#     b = n//10%10
#     c = n//100
#     kubc = a**3+b**3+c**3
#     kvadc = a**2+b**2+c**2
#     print(kubc - kvadc)


# # 110
# n = int(input())
# if n%2 == 0 and n>0:
#     print(n-1,n+1,'Tek edelerdir')
# elif n>0 and n%2!=0:
#     print(n-1,n+1,'Cut ededlerdir')

# # 111
# import math
# x = int(input())
# if x<=5:
#     y = abs(x+2)+3*x
# elif 5<x<=7:
#     y = math.sqrt(3*x**4+10)
# else:
#     y = x**3-2
# print(y)

# 113

# # 114

# saat1 = int(input())*3600
# deqiqe1 = int(input())*60
# saniye1 = int(input())
# saat2 = int(input())*3600
# deqiqe2 = int(input())*60
# saniye2 =int(input())
# s1 = saat1+deqiqe1+saniye1
# s2 = saat2+deqiqe2+saniye2
# c = s2 - s1
# print(c)



# # 116

# n = input()
# if len(n)%2 == 0: 
#     print(0)
# else:
#     print(n[len(n)//2])

# # 117
# n = int(input())
# if 0<=n<=30:
#     print(2)
# elif 31<=n<=60:
#     print(3)
# elif 61<=n<=80:
#     print(4)
# elif 81<=n<=100:
#     print(5)


# # 118

# n = input() # aaba
# a = n[0]
# f = 0
# for i in n:
#     if i != a:
#         f = 1
# if f == 1:
#     print('Eyni deyil')
# else:
#     print('Eynidir')

# 119

# #  122---> 212
# n = int(input())
# if 99<n<1000:
#     n = str(n)
#     if n[0] != n[2]:
#         if n.count(n[0]) == 2 or n.count(n[1]) == 2:
#             print('Yes')
#         else:
#             print('No')


# # 120

# pul = float(input()) # 100
# kQiymet = float(input()) # 5
# kSayi = pul//kQiymet
# pQaliq = pul%kQiymet
# print(kSayi,pQaliq)


# # 121

# x = int(input())
# y = int(input())
# if x!=0 and y!=0:
#     if x>0 and y>0:
#         print('I')
#     elif x<0 and y>0:
#         print('II')
#     elif x<0 and y<0:
#         print('III')
#     else:
#         print('IV')

# # 122

# email = 'email@inbox.ru'
# password = '321abc'
# emailUser = input()
# passwordUser = input()
# if email == emailUser and password==passwordUser:
#     print('Xoş gelmisiz')
# else:
#     print('Email ve ya şifre yanlışdır')


# # 123

# n = float(input())
# t = n*10//10
# k = n*10%10/10
# print(t,k)

# print('salam',end=' ')
# print('necesen',end=' ')
# print('Eli',sep='\n')


# # 124

# n = int(input())
# b = int(input())
# s = 0
# if b!=0:
#     for i in range(1,n):
#         if i**2%b == 0:
#             s += 1
#     print('ədədlərin sayı',s)


# # 125

# n = int(input())
# s = 0
# c = 0
# while n>0:
#     q = n%10
#     if q%2!=0:
#         s = s + 1
#         c = c + q
#     n = n//10
# print(c,s)

# 126

# n = int(input()) # 
# n = round(n**(1/3)) # 3.0
# if n == int(n):
#     print('Yes')
# else:
#     print('No')

# n = int(input())
# n = abs(n)
# f = 0
# for i in range(1,n):
#     if i**3 == n:
#         f = 1
# if f == 1:
#     print('Yes')
# else:
#     print('No')

# c = 0
# a = 5
# b = 7
# c = c + b # burda yaradacam yuxarda c = 0.
# c = a + b # burda yaratmağa ehtiyac yoxdur.


# a = input().split() # 25 37 ---> ['25','37']
# s = 1
# for i in range(len(a)): # [0:2)
#     s = s * int(a[i])
# print(s)

# n = int(input())
# f = 1
# for i in range(1,n+1):
#     f = f * i
# print(f)

# a= 256
# b = a%10**2
# a = int(input())
# if a>0:
    

# # 1

# a = int(input())
# b = int(input())
# print(a+b)


# # 2
# a = int(input())**2
# b = int(input())**2
# print(a+b)

# 4

# n = int(input())
# if n>0:
#     a = n%10
#     print(a**2)

# # 5

# n = int(input()) # 25//10= 2 tam hisse
#                  # 25%10 = 5 qaliq hisse
# if 9<n<100:
#     a = n%10
#     b = n//10
#     print(a+b)

# # 6

# n = int(input())
# if 9<n<100:
#     print(n%10*(n//10))
#     # >>>>>>

# # 7

# n = int(input())
# if 99<n<1000:
#     a = n%10
#     b = n//10%10
#     c = n//100
#     print(a*b*c)

# # 8

# n = int(input())
# if 9<n<100 and n%10!=0:
#     a = n%10
#     b = n//10
#     print(a*10+b)


# # 11

# n = input().split() # ['5','7','8']
# s = 0
# for i in range(len(n)):
#     if int(n[i])>0:
#         s = s + int(n[i])
# print(s)


# # 15
# a = int(input()) # 25
# b = int(input()) # 37
# if 9<a<100 and 9<b<100:
#     o = a//10+b//10
#     t = a%10+b%10
#     print(o,t)

# print('a','b','c',sep='@',end=' ') 
# print('d','\ne',end='*')
# print('c,d')

# a@b@c d
# e*c,d


# \n

# print(5,end='')
# print(6)
# print(7)


# print(5)
# print(6,end=' ')
# print('Ramal')

# print(5,end='\n')
# print(7)

# print('salam\necesen')

# # Klaviaturadan 5 rəqəmi göndərilir
# a = float(input()) # 10.0  
# a = str(a)  #  '10.0'
# a = a+'1' # '10.0' + '1' = '10.01'
# a = a*2  # '10.01'*2 = '10.0110.01'
# a = a.split('0') # ['1','.','11','.','1']
# a = '1'+'1'.join(a)  # '1' + '11.1111.11' = '111.1111.11'
# print(a) 

# a = 'salam'
# #    01234
# a = a.find('s',)
# print(a)

# c = 0
# for i in range(10):
#     c = c + 1
# print(c)

# 120,124,131,118,117
# 130


# # 100

# n = int(input()) # 2564
# n = str(n)
# for i in n:
#     print(i)


# # 101

# n = int(input())
# n = n+1
# while n%2==0 or n%3==0 or n%5==0:
#     n = n+1 
# print(n)

# # 103

# n = int(input())
# s = 0
# for i in range(1,n+1,2):
#     s = s + (1/i)**i
# print(s)

# # 105

# s = 0
# n = int(input()) # ededlerin sayi
# for i in range(n):
#     a = int(input())
#     s = s + a
# print(s/n)

# # 106

# n = int(input('Say daxil et: '))
# b = []
# for i in range(n):
#     a = int(input('Ededi daxil et: '))
#     b.append(a)
# print('cavab: ',min(b))



# # 108

# for i in range(1,1000,2):
#     print(i)


# # 109

# a = [15,12,16,11,9]
# for i in range(0,len(a)):
#     if a[i]%2!=0:
#         print(a[i]**2)

# # 110

# s = 0
# for i in range(1,100):
#     i = str(i)
#     s = s + i.count('3')
# print(s)

# # 111

# n = int(input())
# k = []
# m = []
# for i in range(n):
#     a = int(input())
#     if a%2==0:
#         m.append(a)
#     else:
#         k.append(a)
# print(m,k)

# # 112

# n = int(input())
# s = 0
# while n%10==0:
#     s = s + 1
#     n = n//10
# print(s)

# # 113

# n = int(input())
# F = 0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             F = 1
#     if F == 1:
#         print('Murekkeb')
#     else:
#         print('Sadedir')
    

# # 114

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + (-1)**(i+1)*i*(i+1)
# print(s)


# # 115

# a = [3,4,15,9,18,16]
# for i in a:
#     c = i**0.5
#     if c==int(c):
#         print(i)


# 116

# s = 0
# for x in range(-10,11):
#     if x>3:
#         y = x**2-5*x+6
#     else:
#         y = (x+2)**2
#     if y%3==0:
#         s = s + 1
# print(s)


# # 119

# x = int(input()) # 8
# a = int(input()) # 2
# if x>1 and a>1:
#     q = 0
#     while x/a>=1:
#         q = q + 1
#         x = x/a
#     if x==1:
#         print('Yes')
#     else:
#         print('No')

# x = int(input())
# a = int(input())
# f = 0
# if x>1 and a>1:
#     for i in range(a,x+1,a):
#         if i == x:
#             f = 1
# if f == 1:
#     print('Yes')
# else:
#     print('No')


# a = ['2','3','5','mandalin']
# a = ''.join(a)
# print(a) # 235mandalin


# Aylıq sınaq
# 1-30


# a = 'Python'
# for i in a:
#     print(i[-2])


# 9.1
# 5,4,39,22,16,11,8,31,32,34,33,37,46
# 53,55,19,49


# 9.2
# 60,63
# 65


# # Proqramlaşdırma Funksiya
# def cəm(list):
#     s = 0
#     for i in list:
#         s = s + i
#     return s
    
# a = [12,23,4,5,16,7,8]
# c = cəm(a)
# print(c)

# def ferid(ronaldo):
#     messi = ronaldo[0]
#     for i in ronaldo:
#         if i>messi:
#             messi = i
#     return messi


# a = [12,23,4,5,16,7,8]
# print(ferid(a))

# m = max(a)
# print(m)




# c = sum(a)
# print(c)

# a = '5'**10
# print(a)

# # Recursion function

# def f(n):
#     if n == 1:
#         return 1
#     return n * f(n-1)

# a = f(5)
# print(a)

# Funksiya



# a = int(input('a ='))
# b = int(input('b ='))
# c = int(input('c ='))
# print(a,b,c)


# a = ['5','4','3','15','143']
# #     0   0   0   01   012
# b = max(a)
# print(b)

# def f(n):
#     if n==1:
#         return 1
#     return n + f(n-1)

# a = f(5)
# print(a)

# # 128

# n = int(input())
# n = list(str(n))
# n.sort()
# n.reverse()
# n = ''.join(n)
# n = int(n)
# print(n)

# 129

# n = int(input())
# a = []
# b = []
# c = []
# for i in range(0,n):
#     aElement = int(input(f'1-ci listin {i+1}.elementi: '))
#     bElement = int(input(f'2-ci listin {i+1}.elementi:'))
#     a.append(aElement)
#     b.append(bElement)
#     c.append(aElement+bElement)
# print(c)
#130
# Amil=16
# Eltac=Amil/2
# Anar=Eltac+5
# print((Amil+Eltac+Anar)/3)

#131

# n=int(input())
# a=[]
# for i in range(0,n):
#     b=input()
#     a.append(b)
# s=0
# for i in a:
#     s=s+len(i)
# print(s)



# # 131

# n = int(input()) # 5
# a = []
# for i in range(n):
#     b = input()
#     a.append(b)
# c = []
# for i in a:
#     c.append(len(i))
# print(sum(c))
        

# # 132

# # 123111 ---> bir23birbirbir
# a = input()
# b = a.replace('1','bir')
# print(b)

# # 133

# n = int(input()) # 4
# y = []
# a = []
# for i in range(n):
#     b = int(input()) # 25 45 255 30
#     while b<=9 or b>99:
#         b = int(input('Ikireqemli olmalidir!: '))
#     a.append(b)
# for i in a:
#     i = str(i)
#     c = int(i[0]) + int(i[-1])
#     y.append(c)
# print(y)

# 134

# n = input().split() # ['Hello', 'world']
# print(len(n))

# # 135

# n = input()
# a = []
# for i in n:
#     if n.count(i)==1:
#         a.append(i)
# print(len(a))

# # 136

# a = ['Mandarin','Armud','Alma']
# b = []
# for i in a:
#     b.append(len(i))
# print(max(b))

# # 137

# n = input().split() # ['windows','view','www']
# j = 1
# for i in n:
#     c = i.count('w')
#     print('daxil edilmiş cümlənin',j,'saylı sözündə',c,'sayda w simvolu mövcuddur')
#     # print(f'daxil edilmiş cümlənin {j} saylı sözündə {c} sayda w simvolu mövcuddur')
#     j = j+1


# # 138

# n = int(input())
# if n>99:
#     n = list(str(n))
#     n.sort()
#     n.reverse()
#     n = ''.join(n)
#     n = int(n)
#     print(n)

# # 139

# n = int(input()) # 3
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# s = 0
# for i in b:
#     i = str(i)
#     if i.count('1') != 0:
#         s = s + 1
# print(s)

# # 140

# n = input()# Sd234rdf12
# s = ''
# rqmlr = '0123456789'
# for i in n:
#     if rqmlr.count(i) == 0:
#         s = s + i
# print(s)

# # 141

# n = input() # salam ---> salm
# b = []
# for i in n:
#     if b.count(i) == 0:
#         b.append(i)
# b = ''.join(b)
# print(b)


# # 142

# n = input().split()
# a = 0
# for i in n:
#     if i.count('s') > 0:
#         a = a + 1
# print(a)

# # 143

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# for i in range(len(a)):
#     print(a[i]*i)




# 144

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     while a==0:
#         a = int(input('0-dan ferqli eded olsun!: '))
#     b.append(a)
# for i in range(len(b)):
#     b[i] = -1*b[i]
# print(b)

# # 145

# n = int(input('Ededlerin sayı: ')) # 3
# b = []
# for i in range(n):
#     a = int(input('Ədəd daxil et: ')) # 5, 10, 20
#     b.append(a)
# for i in b:
#     i = str(i)
#     h = int(i[0])*int(i[len(i)-1])
#     print(h)

# # 146

# n = int(input())
# b = []
# for i in range(n):
#     a=int(input())
#     b.append(a)
# m = max(b)
# for i in range(0,len(b)):
#     s = b[i]+m
#     b[i] = s
# print(b)

# # 147

# n = input() # salam1123
# h = 1
# c = 0
# rqmlr = '0123456789'
# for i in range(len(n)):
#     if rqmlr.count(n[i]) == 1:
#         h *= int(n[i])
#     else:
#         c += i
# print(c,h)

# # 148

# n = int(input()) # 1328, 8321-->8321-1328
#                  # 0123
# k = str(n)
# g = k[1:len(k)-1] # 32
# a = k[0] # 1
# b = k[-1] # 8
# s = int(b+g+a)
# if s > n:
#     print(s-n)
# else:
#     print(n-s) 

# 149

# a = [3,4,5,6,7,8,2,9,1,12]
# average = sum(a)/len(a)
# for i in a:
#     if i>average:
#         print(i)

# 150

# n = int(input())
# if n>0:
#     n = list(str(n))
#     n.reverse()
#     n = ''.join(n)
#     n = int(n)
#     print(n)
# else:
#     print('Müsbət ədəd daxil et!!!!')

# 151

# a = [351,648,776,918]
# for i in a:
#     i = str(i)
#     c = (int(i[0]) + int(i[-1]))*2
#     print(c)

# # 152

# n = input() # aaaabbbb
# n = n.replace('a','*')
# n = n.replace('b','a')
# n = n.replace('*','b')
# print(n)

# # 153

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# menfi = []
# musbet = []
# for i in a:
#     if i<0:
#         menfi.append(i)
#     elif i>0:
#         musbet.append(i)
# print(min(musbet)+max(menfi))

# # 154

# n = int(input()) # 14276
# n = str(n)
# s = ''
# for i in n:
#     if i != '4' and i != '7':   
#         s = s + i
# if s != '':
#     s = int(s)
# else:
#     s = '----'
# print(s)

# # 155
# # ******
# n = input() # salam123 ---> 01234123
# n = list(n)
# rqmlr = '0123456789'
# for i in range(len(n)):
#     if rqmlr.count(n[i]) == 0:
#         n[i] = str(i)
# n = ''.join(n)
# print(n)

# 156

# months = ['Yanvar',
#           'Fevral',
#           'Mart',
#           'Aprel',
#           'May',
#           'Iyun'] 
# b = []
# for i in months:
#     s = int(input())
#     b.append(s)
# f = 0
# for i in range(1,len(b)-1):
#     if b[i-1]<b[i]>b[i+1]:
#         print(months[i],':',b[i],'ədəd')
#         f = 1
# if f == 0:
#     print('Uğurlu ay yoxdur')


# # 157
# def simpleOrCompound(n):
#     f = 0
#     for j in range(2,i//2+1):
#         if i%j==0:
#             f = 1
#     return f

# a = int(input())
# b = int(input())
# if 2<=a<b:
#     for i in range(a,b+1):
#         if simpleOrCompound(i) == 0:
#             print(i)

# # 158

# n = input() # 'H+2k3s8d*6'
# rqmlr = '0123456789'
# s = 0
# for i in n:
#     if rqmlr.count(i) == 1:
#         s = s + int(i)
# print(s)

# # 159
# a = int(input()) # 5486137
# a = str(a) # '5486137'
# b = int(max(a)) # 8
# k = int(min(a)) # 1
# c = b+k
# if c%2==0:
#     print('Cüt')
# else:
#     print('Tək')

# sınaq 11
# 29,30


# 29

# def simpleOrCompound(n):
#     f = 'Sade'
#     for i in range(2,n//2+1):
#         if n%i==0:
#             f = 'Mürəkkəb'
#     return f

# a = [245,348,124,422,334,232]
# b = []
# for i in a:
#     i = str(i)
#     c = int(i[0]) + int(i[len(i)-1])
#     if simpleOrCompound(c) == 'Sade':
#         b.append(i)
# print(b)


# 30

# a = [1,2,3,4,5]
# c = sum(a)
# for i in range(0,len(a)):
#     a[i] = c-a[i]
# print(a)



# a = '12.5'
# a = int(float(a))
# print(a)


# a = 'alabalaba'
# #    012345678
# print(a.find('laba',3,9))



# 
# import turtle

# t = turtle
# t.speed(1000)
# b = 100
# n = 0
# for i in range(37):
#     t.circle(100,360,10)
#     t.setheading(n)
#     n +=10
# t.done()
# n = 1
# while n>0:
#     t.forward(n)
#     t.left(1)
# t.done()


# 11.3
# 11.4
# 1,9,10,4,16,14,28,19,32,13,17,50,23,52,46,55,60,67

# n = 1
# while True:
#     if n == 100:
#         break
#     print(n)
#     n = n +1


# x = False
# y = True
# if y>x:
#     print('salam')


# # 101

# n =int(input())
# a = int(input())
# b = int(input())
# if n<a:
#     print('Solundadir')
# elif n>b:
#     print('Saghindadir')
# else:
#     print('Daxilindedir')



# # 102

# n = int(input())
# if n>2:
#     if n%2==0:
#         print(n-2)
#     else:
#         print(n-1)


# 103

# n = int(input())
# if 999<n<10000:
#     if n//1000==n//10%10:
#         if n//100%10 == n%10:
#             print('Beraberdir')
#     else:
#         print('Beraber deyil')

# n = int(input())
# if 999<n<10000:
#     if n//100 == n%100:
#         print('Beraberdir')
#     else:
#         print('Beraber deyil')


# 104

# n = int(input())
# if 99<n<1000:
#     a = n%10
#     b = n//10%10
# #     c = n//100
# #     k = (a**3+b**3+c**3)-(a**2+b**2+c**2)
# #     print(k)

# # 105

# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('Beraberterefli')
# elif a!=b!=c and a!=c:
#     print('muxtelif terefli')
# else:
#     print('beraberyanli')

# # 106

# n = int(input())
# if n%6==0:
#     print('He')
# else:
#     print('Yox')

# 107

# n = int(input())
# if 999<n<10000:
#     if n//10%2==1:
#         k = (n//10%10)*(n//100%10)
#     else:
#         k =(n//10%10)+(n//100%10)
#     print(k)

# 108

# n = int(input())
# if n==12 or n==1 or n==2:
#     print('Sizin ad gununuz qishdadir')
# elif n==3 or n==4 or n==5:
#     print('Sizin ad gununuz yazdadir')
# elif n==6 or n==7 or n==8:
#     print('Sizin ad gununuz yaydadir')
# elif n==9 or n==10 or n==11:
#     print('Sizin ad gununuz payizdadir')
# else:
#     print('Bele bir ay sirasi yoxdur!!')



# # 109

# n = int(input())
# if 0<n<100:
#     if n>9:
#         print('Ikireqemlidir')
#     else:
#         print('Birreqemlidir')

# 110

# n = int(input())
# if n%2==1:
#     print(n-1,n+1, 'cut ededlerdir')
# else:
#     print(n-1,n+1,'tek ededlerdir')


# n = input()
# if len(n)%2==0:
#     print(0)
# else:
#     print(n[len(n)//2])



# n = input()
# a = n[0]
# if n.count(a) == len(n):
#     print('eynidir')
# else:
#     print('eyni deyil')

# n = input()
# f = 0
# for i in n:
#     if n[0] != i:
#         f = 1
# if f==1:
#     print('eyni deyil')
# else:
#     print('eynidir')


# email = input('Email: ')
# password = input('Password: ')
# if email == 'email@inbox.ru' and password == '321abc':
#     print('Welcome')
# else:
#     print('Try again!!')

# # 123

# n = float(input()) # 5.6*10
# k = len(str(n))-2
# n = n*10**k
# t = int(n//10**k) # 5
# k = n%10**k/10**k
# print(t,k)


# # 119

# n = int(input())
# n = str(n)
# a = n[0]
# b = n[2]
# if a==b:
#     print('Eded zaten polindrom ededdir')
# elif n.count(a) == 2 or n.count(b) == 2:
#     print('Mumkundur')
# else:
#     print('mumkun deyil')



# 