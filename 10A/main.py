#  Dəyişən adı ola bilməz
a = 5

# + , -, /, //, %,*, **

# mesaj_gelenler = 5

# Data tiplər
# İnteger  Tam ədədlər
# Float    Həqiqi ədələr
# String   'salam',  "salam" 
# boolean  True, False

# Müqayisə operatorları
# ==
# !=
# >
# <
# >=
# <=

# a = 5
# b = 10
# print(a+b) # 15
# print('a'+'b') # ab  # 10+5
# print('a+b')  # a+b

# a = 5
# b = '10'
# # print(a+b) # 15 # xeta
# print(a*b) # 1010101010
# print('a'+b) # a10

# a = 5
# b = 7
# if a<b:         # mudur
#     print(1)
# elif a==5:      # muavini
#     print(2)
# elif b==7:      # asistani
#     print(3)
# else:           # fehle
#     print(4)


# a = 5
# b = 7
# if a>2:
#     print(1)
#     if a==5:
#         print(2)
#     else:
#         print(3)
# else:
#     print(4)



# a = 7
# b = 5
# if a>b:
#     print(1)
    
# if a==7:
#     print(2)
#     if b<10:
#         print(4)
#     else:
#         print(5)
# else:
#     print(3)


# Or , And


# b = int(input('b= '))
# if b%2 == 0 or b>0:
#     print('Yes')
# else:
#     print('NO')

# arr = ['armud','alma','mandarin','portağal','kivi']
# #        0       1       2             3       4
# s = 'salam dsfdsajflksadfsad fsad fsda f dsaf saf dg asg sagfsa gaf g dfsadf'
# #    01234
# # print(arr[len(arr)-1][len(arr[len(arr)-1])-1])
# start= 1
# stop = 10
# step = 1
# for i in range(start,stop,step):
#     print(i)


# n = int(input())
# a = int(input())
# b = int(input())
# if n<a:
#     print('Solundadıdr')
# elif n>b:
#     print('Sağındadır')
# else:
#     print('Daxilindədir')


# n = int(input())
# if n>2:
#     if n%2==0:
#         n = n-2
#     else:
#         n = n-1
#     print(n)
# else:
#     print('N 2 -den boyuk olmalidir')

# Toplu açıqlar
#

# # # 78
# if 7>3:
#     print(4)
#     if 5>4:
#         print(1)
#     else:
#         print(2)
# else:
#     print(3)


# a = int(input())
# print(a)

# # 103

# n = int(input()) # 1212//100
# a = n//100
# b = n%100
# if a==b:
#     print('Beraberdir')
# else:
#     print('Beraber deyil')


# # 104

# n = int(input()) # 324
# n=abs(n)
# a = n%10
# b = n//10%10
# c = n//100
# kubC = a**3+b**3+c**3
# kvaC = a**2+b**2+c**2
# print(kubC-kvaC)

# # # 105

# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('Brbrtrfli')
# elif a!=b!=c and a!=c:
#     print('mxtlftrfli')
# else:
#     print('brbryanli')


# # 106

# n = int(input())
# if n%2==0 and n%3==0:
#     print('HE')
# else:
#     print('Yox')

# # 107

# n = int(input()) # 2345
# a = n//100%10
# b = n//10%10
# if b%2==0:
#     c = a+b
# else:
#     c = a*b
# print(c)



# 108

# n = int(input())
# if n == 12 or n==1 or n==2:
#     print('Qış')
# elif n==3 or n==4 or n==5:
#     print('Yaz')
# elif n==6 or n==7 or n==8:
#     print('Yay')
# elif n==9 or n==10 or n==11:
#     print('Payız')


# 11-ci sinif
# 28


# # 101

# n = int(input())
# a = int(input())
# b = int(input())
# if a<=n<=b:
#     print('Daxilinde')
# elif n<a:
#     print('solundadir')
# else:
#     print('saginda')

# # 102

# n = int(input())
# if n>2:
#     if n%2==0:
#         print(n-2)
#     else:
#         print(n-1)

# # 103

# n = int(input())
# if 1000<=n<10000:
#     a = n//100
#     b = n%100
#     if a==b:
#         print('Beraberdir')
#     else:
#         print('Beraber deyil')

# 104

# n = int(input())
# n = abs(n)
# if 100<=n<1000:
#     a = n//100
#     b = n//10%10
#     c = n%10
#     ckub = a**3+b**3+c**3
#     ckvad = a**2+b**2+c**2
#     print(ckub-ckvad)

# # 105

# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('Beraberterefli')
# elif a==b or b==c or a==c:
#     print('beraberyanli')
# else:
#     print('muxtelifterefli')

# # 106

# n = int(input())
# if n%6==0:
#     print('he')
# else:
#     print('yox')

# # 107

# n = int(input()) # 2345
# a = n//100%10
# b = n//10%10
# c = str(a)+str(b)
# if int(c)%2==0:
#     print(a+b)
# else:
#     print(a*b)

# # 108

# n = int(input())
# if n==12 or n==1 or n==2:
#     print('Sizin ad gunu qishdadir')
# elif n==3 or n==4 or n==5:
#     print('Sizin ad gunu Yazdadir')
# elif n==6 or n==7 or n==8:
#     print('Sizin ad gunu yaydadir')
# elif n==9 or n==10 or n==11:
#     print('Sizin ad gunu payizdadir')
# else:
#     print('404')

    
# # 109

# n = int(input())
# if 0<n<100:
#     if n<10:
#         print('Birreqemli')
#     elif 10<=n:
#         print('Ikireqemli')


# # 110

# n = int(input())
# if n%2==0:
#     print(n-1,n+1,'Tek ededlerdir')
# else:
#     print(n-1,n+1,'cut ededlerdir')

        

# # 111

# x =int(input())
# if x<=5:
#     y = abs(x+2) + 3*x
# elif 5<x<=7:
#     y = (3*x**4+10)**0.5
# else:
#     y = x**3-2
# print(y)


# import math
# n = 625
# n = math.sqrt(n)
# print(n)

# n = 8
# n = n**(1/3)
# print(n)

# 114

# saat1 = int(input())*3600
# deqiqe1 = int(input())*60
# saniye1 =int(input())
# saat2 = int(input())*3600
# deqiqe2 = int(input())*60
# saniye2 =int(input())
# c1 = saat1+deqiqe1+saniye1
# c2 = saat2+deqiqe2+saniye2
# print(abs(c2-c1))

# # 115

# a = int(input())
# b = int(input())
# c = int(input())
# if b<a<c or c<a<b:
#     print(f'qiymetce orta olan={a}')
# elif a<b<c or c<b<a:
#     print(f'qiymetce orta olan={b}')
# else:
#     print(f'qiymetce orta olan={c}')


# # 116

# n = input() # str tipinde sade halda
# L = len(n)
# if L % 2 == 0:
#     print(0)
# else:
#     print(n[L//2])

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
# else:
#     print('Bal 0-100 aralighinda olmalidir')


# # 118

# n = input() # aaba
# m = n[0] # a
# f = 0
# for i in n:
#     if m!=i:
#         f = 1
# if f == 0:
#     print('eynidir')
# else:
#     print('Eyni deyil')


# # 119

# n = int(input())
# if n%100 != 0:
#     a = n//100
#     b = n//10%10
#     c = n%10
#     if a==b or b==c or a==c:
#         print('Mumkundur')
#     else:
#         print('Mumkun deyil')


# 120

# p = float(input())
# kQ = float(input())
# kS = p//kQ
# pQ = p - kQ*kS
# print(kS, pQ)

# n = round(0.54,1)
# print(n)

# 121

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

# 122

# Email = 'email@inbox.ru'
# password = '321abc'



# EmailUser = input('email: ')
# passwordUser = input('password: ')
# if Email == EmailUser and password == passwordUser:
#     print('Girish ughurludur')
# else:
#     print('Email ve ya shifre yanlishdir')


# 123

# n = float(input()) # '5.65'
# k = len(str(n))-2
# t = int(n//1)
# k = n*10**k%10**k/10**k
# print(t,k)



# a = input() # str # salam
#                   01234
# # a = a.lower()
# # a = a.upper()
# # a = a.capitalize()
# # a = a.strip()
# # a = a.replace('nur','mir')
# a = a.count('a')
# a = a.find('b') # [2,5)

# print(a)

# Daxil edilmiş setirdeki a hərfini b hərfi ilə, b hərfini a hərfi ilə əvəz edən kod yaz.
# "aaaaccccddddbbbb"  ----- "bbbbccccddddaaaa"

# n = input() #aaaabbbb
# n = n.replace('a','*') # ****bbbb
# n = n.replace('b','a') # ****aaaa
# n = n.replace('*','b') # bbbbaaaa
# print(n)


# a = [2,3,4,5,10,5]
# #    0 1 2 3 4  5  6
# #    0 1 2 3
# # a.append(10)
# # a.insert(2,15)
# b = []
# for i in a:
#     if i!=5:
#         b.append(i)
# a = b
# print(a)
#     0    1   2   3    4
# a = ['a','aa','aaa','aabc','ab','ac']
# #     0   01   012   0123   01   01
# a.sort() 
# a.reverse()
# print(a) # ac, ab, aabc, aaa, aa, a

# def salam():
#     a = 5

# print(salam())




# # list vs split
# n = 'Salam necesen sagol'
# # n = list(n)
# n = n.split(" ")
# print(n)

# # join list ---> str
# a = ['050','666','66','66']
# a = ''.join(a)
# print(a)

# print(1,2,3,4,5,sep='-ci sira\n')

# a = [5,28,29,30,12,19,20,21,24,26]
# # a.append(5)
# # a.remove(5)
# # a.insert(0,10)
# # a.reverse()
# a.sort()
# print(a)
# b = a.count(5)
# c = a.index(10)


# s = 'salam'
# m = s[-2] # a
# print(m)

# codera 11.2
# sinaq 7
# [ 20, 21, 24, 26, 28, 29, 30]

# a = 'informatika'
# #    0123
# k = a[9:2:2]
# print(k)

# a = 'Salam'
# # for , while
# for i in range(1,101):
#     print(f'{i}.{a}') 

