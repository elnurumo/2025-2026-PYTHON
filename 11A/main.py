# # # # Collatz sanısı

# # # # cüt ---> x/2
# # # # tek ---> 3*x+1
# # # # 4,2,1

# # # n = int(input())
# # # s = 0
# # # while n!=1:
# # #     s = s + n
# # #     if n%2==0:
# # #         n = n//2
# # #     else:
# # #         n = 3*n+1
# # # s = s + 1
# # # print(s)

# # # 118

# # # n = input() #'aAaa'
# # #             # 0123
# # # b = n[0] # a
# # # f = 0
# # # for i in n:
# # #     if b!=i:
# # #         f = 1
# # # if f == 1:
# # #     print('Eyni deyil')
# # # else:
# # #     print('Eynidir')    


# # # 2-ci gün əlavə
# # # 10:00 - 12:00
# # # 17:00 - 19:00 

# # # codera
# # # 10.5
# # #



# # # * -vurma
# # # / - bölmə
# # # // - tam bölmə
# # # % bölür qalıqı tapır
# # # ** - qüvvət üstün tapır

# # # if Elif Else

# # a = 5
# # b = 10
# # c = 20
# # if a<b:
# #     print('1')
# #     if a<c:
# #         print('2')
# #     if a>c:
# #         print('3')
# # if a<c:
# #     print('4')

# # 101


# # 108

# # n = int(input('Ad günün ay sırasın daxil et: '))
# # if n==12 or n==1 or n==2:
# #     print('Sizin ad gününüz qışdadır.')
# # elif 2<n<6:
# #     print('Sizin ad gününüz Yazdadır.')
# # elif 5<n<9:
# #     print('Sizin ad gününüz Yaydadır.')
# # elif 8<n<12:
# #     print('Sizin ad gününüz Payızdadır.')
# # else:
# #     print('Düzgün ay sırası daxil et!!!!')


# # kitab   info
# # 01234   0123
# #   t       0

# # n = input()
# # le = len(n)
# # if le%2==0:
# #     print(0)
# # else:
# #     print(n[le//2])

# # # list
# # a = [3,4,5,6,7]
# # for i in range(0,len(a)):
# #     if i == 2:
# #         a[i]=10
# # print(a)
# # # str
# # a = '34567'   
# # s = ''
# # for i in range(0,len(a)):
# #     if i == 2:
# #         s = s + '10'
# #     else:
# #         s = s + a[i]
# # a = s
# # print(a)

# # # Dinamik
# # a = 5
# # a = 'Salam'
# # print(a)

# # a = 'Hello'
# # i = 1
# # # # for , while
# # while i<=100:
# #     print(f'{i}. {a}')
# #     i = i+1

# # for i in range(100):
# #     print(i+1,'.', a)

# # integer, float, string, array,boolean
# # Boolean -- True, False
# # Array (List) --- [3,4,5,7,'alma']
# # String ---  'salam',  "Salam"
# # float --- 2.5, 5.0
# # integer --- 5,6 tam ədədlər

# # a = 25
# # print(a**0.5)

# # a) 5   b) 5.0


# # a = 5
# # b = 6

# # print(a+b) # 11
# # print('a'+'b') # 56 ab
# # # print('a+b') # a+b

# # # print("Abbaslı Fəxri",sep='\n')


# # a = 'Valide Aslanova'
# # a = a.lower()
# # s = a.count('a')
# # print(s)


# # upper
# # lower
# # capitalize
# # count
# # find
# # replace
# # strip

# # a = 'salam'
# # s = a.index('a',2,4)
# # print(s)

# # a = 'salam necesen'
# # a = a.split('')
# # print(a)

# # a = [1,2,3]
# # a = '5'.join(a)
# # print(a)

# # n = int(input())
# # a = n-1 
# # b = n+1
# # if n % 2 == 0 :
# #     print(a , b , "tekdiler")
# # else :
# #     print(a , b, "cutduler"


# # x = int(input()
# # if x <= 5 :
# #     y=abs(x+2) + 3x
# # elif x>7 :
# #     y=(x**3)-2
# # else : 
# #     y=((3x**4)**0,5)+10
# # print(y)

 


# #  a = int(input())
# #  b = int(input())
# #  c = int(input())
# #  if a==b and b==c and a==c :
# #       print(3)
# # elif a==b or a==c or b==c :
# #       print(2)
# # else :
# #       print(0)


# a = int(input())
# b = int(input())
# c = int(input())
# if b<a<c :
#     print(a)
# elif a<b<c :
#     print(b)
# else :
#     print(c)

# x = int(input())
# if x<100 :


# 123

# print(1-0.8)

# n = float(input()) 
# m = str(n)
# l = len(m)-2
# print(l)
# n = n*10**l
# t = n//10**l
# k = n%10**l/10**l
# print(t,k)


# İxtiyari bir ədəd daxil edilir və istifadəçi həmin ədədin sağına və soluna ixtiyari bir söz yaza bilər(hərf,rəqəm,simvol) Bunu Python kodu ilə düzəldin.
# Giriş
# 245     
# Çıxış
# Salam245Salam

# k=int(input())
# d=''
# b=(input()).lower()
# c='abcdefghijklmnopqrstuvwxyz'
# for i in b:
#     d=d+c[(c.find(i)+k)%len(c)]
# print(d)


# n = int(input())
# a,b = 0,1
# for i in range(n):
#     a , b = b, b+a
# print(a)


# a=int(input())
# b = [0,1]
# i = 0
# while len(b)<=a:
#     c = b[i] + b[i+1]
#     b.append(c)
#     i = i + 1
# print(b[a-1])



# 120

# pul = float(input())
# keksQiymet = float(input())
# keksSayi = pul//keksQiymet
# pulQaliq = pul - keksQiymet*keksSayi
# print(keksSayi,pulQaliq)

# # 118
# # 1-ci üsul
# n = input() #aaaa
# if n.count(n[0]) == len(n):
#     print('eynidir')
# else:
#     print('eyni deyil')

# # 2-ci üsul

# n = input() # aaAa
# m = n[0] #a
# f = 0
# for i in n:
#     if i!=m:
#         f = 1
# if f == 1:
#     print('Eyni deyil')
# else:
#     print('eynidir')


# 133

# n = int(input())
# sade_vuruq = 2
# while n>1:
#     if n%sade_vuruq == 0:
#         n = n//sade_vuruq
#         print(sade_vuruq)
#     else:
#         sade_vuruq = sade_vuruq+1


# n = int(input())
# l = []
# sade_bolen = 2
# while n>1 :
#     if n%sade_bolen == 0 :
#         n=n//sade_bolen
#         if l.count(sade_bolen)== 0:
#             l.append(sade_bolen)
#     else :
#         sade_bolen=sade_bolen+1
# print(l)

# n=int(input())
# n=n+1
# while n%2==0 or n%3==0 or n%5==0 :
#     n=n+1
# print(n)


# n=int(input())
# s=0
# for i in range(1,n+1) :
#     s=s+1/(i**2)
# print(s)

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+(1/n)**n
# print(s)

# 


# n=int(input())
# s=0
# for i in range(0,n):
#     a=int(input())
#     s=s+a
# print(s/n)

# n=int(input())
# l=[]
# for i in range(0,n):
#     a=int(input())
#     l.append(a)
# print(max(l))

# 


# l=[]
# for i in range(1,1000):
#     if i%2==1 :
#         l.append(i)
# print(l) 

# a=[]
# l=[15,12,16,11,9]
# for i in l:
#     if i%2==1 :
#         k=i**2
#         a.append(k)
# print(a)


# s=0
# for i in range(1,100):
#     b=str(i)
#     if b.count('3')>0:
#         s=s+b.count('3')
# print(s)

# n=int(input())
# c=[]
# t=[]
# for i in range(0,n):
#     k=int(input())
#     if k%2==0 :
#         c.append(k)
#     else :
#         t.append(k)
# print(c,t)

# n=int(input())
# s=0
# while n%10==
#     s=s+1
#     n=n//10
# print(s)

# n = input()
# n = n.split('2')
# n = '1'.join(n)
# print(n)


# # 28

# x = float(input())
# a = float(input())
# b = float(input())
# if a<=x<=b:
#     print('Yes')
# else:
#     print('No')

# # 29
# n = int(input())
# i = 1
# f = 1
# while f<n:
#     f = f * i
#     i = i+1
# if n == f:
#     print('Beli')
# else:
#     print('Xeyr')

# 30

# n = int(input())
# k = len(str(n))
# b = []
# while n>0:
#     a = n%10
#     if a%2!=0:
#         b.append(a)
#     n = n//10
# if len(b) == k:
#     print('Yes')
# else:
#     print('No')

# n = int(input())
# n = str(n)
# f = 0
# for i in n:
#     if int(i)%2==0:
#         f =1
# if f == 0:
#     print('yes')
# else:
#     print('No')

# a = '111'
# #    012
# b = '12'
# #    01
# print(b>a)
# a = ['111','12','A1','a2','aa','b','b1','d3']
# a.sort()
# print(a)

# a = 'anar'
# s1 = a[a.count('a')] + a[a.count('a')]
# print(s1)

# setirler
# 97,99,98,122,123




# aylar = [
#     'Yanvar',
#     'Fevral',
#     'Mart',
#     'Aprel',
#     'May',
#     'Iyun'
# ]
# sell =[]
# for i in range(len(aylar)):
#     sellCount = int(input())
#     sell.append(sellCount)
# f = 0
# for i in range(1,len(sell)-1):
#     if sell[i-1]<sell[i]>sell[i+1]:
#         print(aylar[i],':',sell[i],'ədəd')
#         f = 1
# if f == 0:
#     print('Uğurlu ay yoxdur')

# # 170

# n = input().split()
# m = []
# c = []
# d = []
# for i in n:
#     m.append(len(i))
# maxi1 = max(m)
# for i in m:
#     if i != maxi1:
#         c.append(i)
# maxi2 = max(c)
# for i in n:
#     if maxi2 == len(i):
#         if d.count(i) == 0:
#             d.append(i)
# print(d)

# # 175

# n = int(input())
# n = str(n)
# a = n[0]
# b = n[len(n)-1]
# if a>b:
#     print(a+b)
# else:
#     print(b+a)


# # 167

# hefteler = [
#     'Bazar ertesi',
#     'Çərşənbə axşamı',
#     'Çərşənbə',
#     "Cümə axşamı",
#     "Cümə",
#     "Şənbə",
#     "Bazar"
# ]
# n = int(input())
# hG = n%7 - 1
# print(hefteler[hG])


# 168

# b = input() # ['12' '24' '35' '47']
# a = b.split()
# c =[]
# for i in a:
#     if i[0] == '4':
#         c.append(int(i))
# print(sum(c))


# 1

# n = int(input())
# if n>0:
#     n = str(n)
#     n = '1'.join(n)
#     n = int(n)**2
#     print(n)

# n = int(input())
# n = str(n)
# s = ''
# for i in range(0,len(n)):
#     if i == len(n)-1:
#         s = s + n[i]
#     else:
#         s = s + n[i]+'1'
# print(int(s)**2)
    

# n = int(input())
# a = []
# for i in range(n):
#     x = int(input())
#     a.append(x)
#     a[i] = a[i]*-1
# print(a)


# 2

# a = input().split()
# b = input().split()
# c = []
# for i in a:
# #     if b.count(i) > 0 and c.count(i) == 0:
# #         c.append(i)
# # print(c,len(c))

# # 143

# n = int(input()) # 208
# n = str(n) # '208'
# m = max(n)
# if m<'8':
#     print('Mövcuddur')
# else:
#     print('Mövcud deyil')
 
# # 142

# n = int(input())
# n = str(n)
# onluq = 0
# L = len(n)-1
# for i in n:
#     onluq = onluq + int(i)*2**L
#     L = L-1
# s = ''
# while onluq>0:
#     q = onluq%8
#     s = str(q) + s
#     onluq = onluq//8
# print(s)

# # 142
# n = int(input())
# n = str(n)
# l = len(n)
# if l%3==1:
#     n = '00'+n
# elif l%3 == 2:
#     n = '0' + n
# s = ''
# for i in range(0,len(n),3):
#     s = s + str(int(n[i])*4+int(n[i+1])*2+int(n[i+2]))
# print(s)


# sinaq 8
# 29,30

# 28

# s = input()
# c = 0
# for i in range(len(s)):
#     if s[i] == 'a':
#         c = c + i
# print(c)

# 29

# n = input()
# s = ''
# b = []
# for i in n:
#     if '0'<=i<='9':
#         s = s + i
#     else:
#         if s != '':
#             b.append(int(s))
#             s = ''
# if s != '':
#     b.append(int(s))
# print(sum(b))

# n = 'Salam123necesen34sagol9'


# sinaq 9
# 29,30


# # 
# n = 'salam'
# s = ''
# for i in range(len(n)):
#     s = s + str(i)
# n = s
# print(n)


# a = [2,3,4,5]
# for i in range(len(a)):
#     a[i] = 'salam'
# print(a)


# # 30

# ls = [23,45,623,123,5,67,89,34,12,45,678]
# for i in range(len(ls)):
#     s = ''
#     if i%2!=0 and ls[i]%2==0:
#         while ls[i]>0:
#             q = ls[i]%8
#             s = str(q)+s
#             ls[i] = ls[i]//8
#         print(s)

# 28
