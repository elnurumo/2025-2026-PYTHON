
# # Codera
# # 6,14,7,42,19,24,31,29,45,32,
# # 25,34,37,46,50,49



# # python

# # Data Tiplər
# # Number ---> Integer Int funksiyası int() Bütün tam ədədlər
# # float ----> funksiyası float() Bütün həqiqi ədədlər
# # string ---> funksiyası str() sətir tipi "", ''
# # boolean ---> funksiyası bool()  True, False
# # array --->  []

# # a = 5+4
# # print(a)

# # a = 5
# # b = 14
# # print(a+b) # 19
# # print('a'+'b') # ab
# # print('a+b') # a+b

# # a = 'a'
# # b = 5
# # print(a*b)

# # +
# # -
# # *
# # /
# # // böləndə tam hissə
# # % böləndə qalıq hissi
# # ** qüvvət üstü

# # a = 25
# # # b = a**(1/2)
# # b = a**0.5
# # print(b)

# # a = 5
# # b = 4
# # if a>b:  # mudur
# #     print('1')
# # elif a==5: # muavin
# #     print('2')
# # else: # asistan
# #     print('3')


# # a = 10
# # b = 100
# # if a<b:
# #     print(1)
# # if a!=10:
# #     print(2)
# #     if a>10:
# #         print(3)
# # elif b<1000:
# #     print(4)
# # else:
# #     print(5)

# # a = 15
# # if a%2==0 and a%3==0:
# #     print('Yes')
# # else:
# #     print('No')

# # If else

# #
# # 67-72,

# # a_b = 5
# # print(a_b)

# # end, sep

# # print('Salam','Necəsən','mandalin',sep='\n')


# # a = 5
# # a = a*10
# # a = a*2
# # print(a)

# # print(10)


# #


# # a = '2345'
# # #    0123
# # print(a[2])

# # a = ['Zabit','Nazim','Məhəmməd'," Ömür","Zəhra","Elvin",'Onur','Subhan','Amin']
# # print(a[len(a)-1])


# # # 101

# # n = int(input())
# # a = int(input())
# # b = int(input())
# # if n<a:
# #     print('Solunda')
# # elif n>b:
# #     print('Sağında')
# # else:
# #     print('Daxilindədir')


# # # 102

# # n = int(input())
# # if n>2:
# #     if n%2==0:
# #         print(n-2)
# #     else:
# #         print(n-1)
# # else:
# #     print('N 2-den boyuk olmalidir')

# # 103

# # n = int(input()) # 5665
# # a = n//100
# # b = n%100
# # if a==b:
# #     print('Beraberdir')
# # else:
# #     print('Beraber deyil')


# # 104

# # n = int(input()) # 345
# # n = abs(n)
# # a = n//100 # 345//100 = 3
# # b = n//10%10
# # c = n%10
# # f = a**3+b**3+c**3 - (a**2+b**2+c**2)
# # print(f)

# # a = int(input())
# # b = int(input())
# # c = int(input())
# # if a==b==c:
# #     print('BTrfli')
# # elif a!=b and a!=c and b!=c:
# #     print('Mtrfli')
# # else:
# #     print('Byanli')


# # Codera 11.1


# # a = 5
# # a = pow(a,3)
# # print(a)

# # array = [1,2,15,20,30,40]
# # #        0 1 2  3  4  5
# # print(array[len(array)-1])

# # split() vs list()
# # Cərrah
# # split
# # a = 'Salam'
# # a = a.split('a')
# # print(a) # ['Salam','necesen']

# # # List
# # # Qəssab tikəliyir
# # a = 'salam'
# # a = list(a)
# # print(a)

# # 21
# # join
# # listden --->> str

# # n = ['055','795','45','55']
# # b = '-'.join(n)
# # print(b)

# # print('2'*3)

# # print('salam\necesen')

# # # 106
# n = int(input())
# if n%6==0:
#     print('He')
# else:
#     print('Yox')

# # # 107
# n = int(input()) # 2345//10%10
# a = n//100%10 # 3
# b = n//10%10 # 4
# if b%2!=0:
#     print(a*b)
# else:
#     print(a+b)

# # 108

# n = int(input())
# if n == 12 or n==1 or n==2:
#     print('Sizin ad gününüz qışdadır.')
# elif n==3 or n==4 or n==5:
#     print('Sizin ad gününüz Yazdadır.')
# elif n== 6 or n==7 or n==8:
#     print('Sizin ad gününüz Yaydadır.')
# elif n==9 or n==10 or n==11:
#     print('Sizin ad gününüz payızdadır.')
# else:
#     print('Bele bir ay yoxdur')


# # # 109

# n = int(input())
# if 0<n<=9:
#     print('Birrəqəmli')
# elif 10<=n<100:
#     print('Ikireqemli')

# # # 110

# n = int(input()) # 26
# if n%2==0:
#     print(n-1,n+1,'tek ededlerdir')
# else:
#     print(n-1,n+1,'cut ededlerdir')


# # # 111

# import math
# x = int(input())
# if x<=5:
#     y = abs(x+2) + 3*x
# elif x>7:
#     y = x**3 - 2
# else:
#     y = math.sqrt(3*x**4+10)



# # # 112

# a = int(input())
# b = int(input())
# if a<b:
#     z = (3*b)/abs(a-b)+3*(a+b)
# elif a>b:
#     z = a**2/abs(a+b)
# else:
#     z = (2*a**2+abs(b**3))**0.5

# # # 113

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print(3)
# elif a==b or a==c or b==c:
#     print(2)
# else:
#     print(0)


# # # 114

# saat1 = int(input())*3600
# deqiqe1 = int(input())*60
# saniye1 = int(input())
# saat2 = int(input())*3600
# deqiqe2 = int(input())*60
# saniye2 = int(input())
# s1 = saat1+deqiqe1+saniye1
# s2 = saat2+deqiqe2+saniye2
# print(s2-s1)

# # # 115
# a = int(input())
# b = int(input())
# c = int(input())
# if b<a<c:
#     print('Qiymətcə orta olan=',a)
# elif a<b<c:
#     print('Qiymətcə orta olan=',b)
# elif a<c<b:
#     print('Qiymətcə orta olan=',c)


# # 116

# n = input() # kitab
#             # 012
# L = len(n)
# if L%2==0:
#     print(0)
# else:
#     print(n[L//2])
    
# # 117

# n = int(input())
# if 0<=n<=30:
#     q = 2
# elif 31<=n<=60:
#     q = 3
# elif 61<=n<=80:
#     q = 4
# elif 81<=n<=100:
#     q = 5
# print(q)

# # 118

# n = input() # aaaa
# #             0123
# a = n[0]
# f = 0
# for i in n:
#     if i!=a:
#         f = 1
# if f == 0:
#     print('Eynidir')
# else:
#     print('Eyni deyil')


# # 119

# n = int(input())
# if 99<n<1000:
#     a = n%10
#     b = n//10%10
#     c = n//100
#     if a==b or b==c or a==c:
#         print('Mümkündür')
#     else:
#         print('Mumkun deyil')


# 120

# p = float(input())
# kQ = float(input())
# kS = p//kQ
# pQ = p - kQ*kS
# print(kS,pQ)

# print(1-0.7)


# 121

# x = int(input())
# y = int(input())
# if x!=0 and y!=0:
#     if x>0 and y>0:
#         print('1-ci rub')
#     elif x<0 and y>0:
#         print('2-ci rub')
#     elif x<0 and y<0:
#         print('3-cu rub')
#     else:
#         print('4-cu rub')


# 122

# Email = 'email@inbox.ru'
# password = '321abc'
# EmailUser = input() # str tipine sade halda
# passwordUser = input() # str tipinde sade halda
# if Email == EmailUser and password ==passwordUser:
#     print('Xoş geldin')
# else:
#     print('Email ve ya şifre yanlışdır')


# # # 123

# n = float(input()) # '5.25'
# k = len(str(n))-2
# t = int(n//1)
# k = n*10**k%10**k/10**k  # 2500
# print(t,k)


# 11.1
# 39,20,21,35,36,40


# a = 'Salam'
# #    01234
# k = a[3:2:2]
# print(k)

# a = 'Elnurnur'
# # a = a.lower()
# # a = a.upper()
# # a = a.capitalize()
# # a = a.strip()
# # a = a.replace('nur','mir')
# print(a)

# 
# aaaabbbb sətrindəki a hərflərini b hərfi ilə, b hərfini a hərfi ilə əvəz edən kodu yaz.

# a = input() # aaaabbbb
# a = a.replace('a','*') # ****bbbb
# a = a.replace('b','a') # ****aaaa
# a = a.replace('*',"b") # bbbbaaaa
# print(a)

# # polindrom 121 232
# n = int(input())  #-----> str ---- > list
# k = n
# n = list(str(n))
# n.reverse()
# if list(str(k)) == n:
#     print('yes')
# else:
#     print('no')


# a = 5
# def polindrom():
#     a = 7


# print(polindrom(),a)


# a = 'salam'
# #    01234
# b = a.find('a',2,4)
# m = max(a)
# print(b,m)


# a = 'Salam'

# while, for

# for i in range(1,101,1):
# #            range(start,stop,step)
#     print(f'{i}.{a}')

# a = [12,20,30,40,2,5,50]
# maximum = a[0] 
# for i in a:
#     if maximum < i:
#         maximum = i
# print(maximum)

# m = max(a)
# print(m)


# a = [-2,-10,-5,-100]
# zabit = a[0]
# for i in a:
#     if zabit>i:
#         zabit = i
# print(zabit)


# a = 'salam'
# a = a.capitalize()
# print(a)

# a = [20,2,3,4,20,10,20]\
# #    0  1 2 3 4  5  6
# # a.append(39) # listin sonuna elave edir
# # a.remove(20) # ilk 20 i silecek
# # a.insert(2,40) # daxil edir istediyim indexe 1. index, 2. element
# # a.sort() # artan sira ile duzur
# # a.reverse() # tersine duzur 
# # a = a.index(20) #  tapdigi ilk elementin indexin qaytarir
# # a = a.count(20) # 20-in sayini qaytarir
# print(a)


# # ilk 100 ededin cemi
# n = 100
# s = 0
# while n>0: #--- false
#     s = s + n
#     n = n - 1 
# print(s)

# Ededin sade ve ya murekkeb oldugun yoxlayir
# n = int(input())
# f = 0
# for i in range(2,n//2+1):
#     if n%i==0:
#         f = 1
# if f == 1:
#     print('Murekkeb')
# else:
#     print('sade')


# n = int(input())
# if n%2==0:
#     print('Cut')
# else:
#     print('Tek')


# n = int(input()) # 257
# if 99<n<1000:
#     a = n//100
#     b = n%10 
#     print(a+b)

