# # print("Hello world")

# # a = 'Hello world'

# # print('Məryəm',end=" ")
# # print('Məhərli',end=" ")
# # print("16")

# # İnteger, float, string, array, boolean

# a = 5 #integer --- tam ededler
# b = 5.5 # float --- rasional ededler
# # c = 'Salam' # setir string
# # arr = [1,2,3,4] # array list


# # True, False # boolean



# # arr = [1,2,3,4]
# #       #0 1 2 3
# # # print(arr[3])
# # print(arr)



# # # or and  
# # # 

# # a = 5
# # b = 6

# # if a<b:
# #     print(1)
# #     if a==5:
# #         print(2)
# #         if 4<5:
# #             print(6)
# #     else:
# #         print(3)
# # elif b==6:
# #     print(4)
# # if b>a:
# #     print(5)


# # If else Python


# # n = int(input())
# # if n>2:
# #     if n%2==0:
# #         n = n-2
# #     else:
# #         n = n-1
# #     print(n)

# # n = int(input())
# # a = n//1000
# # b = n//100%10
# # c = n//10%10
# # d = n%10
# # s = str(a)+str(b)
# # h = str(c)+str(d)
# # if s==h:
# #     print('Beraberdir')
# # else:
# #     print('Beraber deyil')


# n = input() # kitab necesen
#             # 01234 0123456
# if len(n)%2==0:
#     print(0)
# else:
#     print(n[len(n)//2])



# x1 = int(input())
# y1 = int(input())
# R = int(input())
# x2 = int(input())
# y2= int(input())
# if (x1-x2)**2 +(y2-y1)**2 == R**2:
#     print('Üzərindədi')
# else:
#     print('Üzərində deyil')

# n = int(input())
# m = n**(1/3)  
# print(m)
# if m == int(m):
#     print('Kubudur')
# else:
#     print('Kubu deyil')

# print(1-0.8)

# 125

# n = int(input()) # 325
# n = str(n) # '325'
# s = 0
# c = 0
# for i in n: # '3'
#     i = int(i)
#     if i%2!=0:
#         c = c + i
#         s = s + 1
# print(c,s)

# 124

# n = int(input())
# b = int(input())
# s = 0
# if b!=0:
#     for i in range(1,n):
#         if i**2%b == 0:
#             s = s + 1
#     print('ədədlərin sayı',s)
# else:
#     print('b 0 ola bilmez')

# 123

# n =float(input())
# m = str(n)
# l = len(m)-2
# n = n*10**l
# t = n//10**l
# k = n%10**l/10**l
# print(t,k)


# # 119

# n = int(input())
# if 99<n<1000:
#     a = n%10
#     b = n//10%10
#     c = n//100
#     if a==b or b==c or a==c:
#         print('Mumkundur')
#     else:
#         print('Mumkun deyil')
# else:
#     print('Eded 3 reqemli olmalidir')

# # 118
# # 1-ci üsul
# n = input() #aaAa
# m = n[0] # a
# f = 0
# for i in n:
#     if i!=m:
#         f = 1
# if f == 1:
#     print('Eyni deyil')
# else:
#     print('Eynidir')

# # 2-ci üsul

# n = input() # aaaa
# if n.count(n[0]) == len(n):
#     print('Eynidir')
# else:
#     print('Eyni deyil')

# x1 = int(input())
# x2 = int(input())
# y1=int(input())
# y2 = int(input())
# R = int(input())
# if (x2-x1)**2+(y2-y1)**2 == R**2:
#     print('Yes')
# else:
#     print('No')

# # 126

# n = int(input())
# f = 0
# for i in range(1,n//2):
#     if i**3 == n:
#         f = 1
# if f == 1:
#     print('Yes')
# else:
#     print('No')

# m = n**(1/3) # 3.5
# print(m)
# if m == int(m):
#     print('Yes')
# else:
#     print('no')

# print('salam', 'necesen','alma','armud',sep="-ci \n")


# print(a[2][2:])

# a = ['alma','armud','naringi','ananas']

# for i in [1,2,3,4,5]:
#     print(i)


# # listin içindəki hərifləri onun indexi ilə əvəz edib çapa ver

# a = ['a','b','b','c','d']
# #     0   1   2   3   4
# for i in range(len(a)):   #===========>>>>>>> RANGE ILE YAZILMALIDIR
#     a[i] = i
# print(a)

# # setrin içindəki hərifləri onun indexi ilə əvəz edib çap et

# a = 'abcde'
# s = ''
# for i in range(len(a)):  #=======>>>>>>> ERORR
#     a[i] = i
# print(a)


# a = 'abcde'
# s = ''
# for i in range(len(a)):  #==================>>>> DOĞRU VERSİYA
#     s = s + str(i)
# a = s
# print(a)

# # FOR , WHILE
# a = 1
# while a<=1000:
#     print(a)
#     a = a + 1


# arr = []
# arr = arr.append(5)
# print(arr)

# arr = ['1','2','3']
# arr = arr.count('1')
# print(arr)

# #    0 1 2   3  4
# m = 0
# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         m=a[i+1]
#     else:
#         m=a[i]
# print(m)


# def maximum(list):
#     m = list[0]
#     for i in list:
#         if i>m:
#             m = i

# a = [10,5,6,100,1000]
# print(maximum(a))


# max()



# # 102
# s= 0
# n = int(input())
# for i in range(1,n+1):
#     s = s + 1/i**2
# print(s)

# a = 'Salam necesen Ismayıl'
# a = a.split('e')
# print(a)

# a = ['+994', '051','391','23','33']
# a = '-'.join(a)
# print(a)

# # 100
# # 1-ci usul
# n = int(input())
# n = str(n)
# for i in n:
#     print(i)
# # 2-ci usul
# n = int(input())
# arr = []
# while n>0:
#     x = n%10
#     arr.append(x)
#     n = n//10
# arr.reverse()
# for i in arr:
#     print(i)

# # 102

# n=int(input())
# s=0
# for i in range(1,n+1):
#     s=s+1/i**2
    
# print(s)

# # 103

# n=int(input())
# s=0
# for i in range(1,n+1,2):
#     s=s+(1/i)**i
# print(s)

# # 104

# n=int(input())
# s=0
# k=n
# while(n>0):
#     a=n%10
#     s=s+a
#     n=n//10
# if k%s==0:
#   print('bolunur ')
# else:
#    print('bolunmur') 

# # 105

   
# # Sınaq 7
# # 28
# x = float(input())
# a = float(input())
# b = float(input())
# if x>=a and x<=b:
#     print('Daxildir')
# else:
#     print('Daxil deyil')


# a = '12'
# #    01
# b = '111'
# #    012
# print(a>b)

# # 29

# n = int(input()) # 25
# f = 1
# i = 1
# while f<n:
#     f = f * i
#     i = i+1
# if f == n:
#     print('Beli')
# else:
#     print('Xeyr')

# # 30

# n = int(input())
# k = str(n)
# s = 0
# while n>0:
#     a = n%10
#     if a%2 == 1:
#         s = s + 1
#     n = n//10
# if len(k) == s:
#     print('Yes')
# else:
#     print('No')


# n = input() # 2B
# L = len(n)-1 # 1
# reqemler = '0123456789ABCDEF'
# #           012345678910
# onluq = 0
# for i in n:
#     onluq = onluq + reqemler.index(i)*16**L
#     L = L-1
# print(onluq)


# 105

# n = int(input())
# s = 0
# i = 0
# while i<n:
#     a = int(input())
#     s = s + a
#     i = i+1
# print(s/i)

# 131

# n = int(input())
# a = []
# for i in range(n):
#     setr = input()
#     a.append(setr)
# s = 0
# for i in a:
#     s = s + len(i)
# print(s)


# 137

# n = input().split()
# j = 1
# for i in n:
#     s = i.count('w')
#     print('daxil edilmiş cümlənin',j,
#           'saylı sözündə',s, 
#           'sayda w simvolu mövcuddur.')
#     j = j+1

# 156

# aylar = ['Yanvar',
#          'Fevral',
#          'Mart',
#          'Aprel',
#          'May',
#          'Iyun']
# sell = []
# for i in range(0,len(aylar)):
#     prntSell = int(input())
#     sell.append(prntSell)
# f = 0
# for i in range(1,len(sell)-1):
#     if sell[i-1]<sell[i]>sell[i+1]:
#         print(aylar[i],':',sell[i],'ədəd')
#         f = 1
# if f == 0:
#     print('Uğurlu ay yoxdur')

# n = input() # 2B
# reqemler = '0123456789ABCDEF'
# L = len(n)-1
# onluq = 0
# f = 0
# for i in n:
#     if reqemler.count(i) == 1:
#         onluq = onluq + reqemler.index(i)*16**L
#         L = L-1
#     else:
#         f = 1
# if f == 0:
#     print(onluq)
# else:
#     print('wrong')

# 129

# n = int(input())
# arr1 = []
# arr2 = []
# arr3 = []
# for i in range(n):
#     a = int(input('arr1:'))
#     b = int(input('arr2:'))
#     arr1.append(a)
#     arr2.append(b)
#     c = a+b
#     arr3.append(c)
# print(arr3)


# 157

# a = int(input())
# b = int(input())
# arr =[]
# if 2<=a<b:
#     for i in range(a,b+1):
#         f = 0
#         for j in range(2,i//2+1):
#             if i%j == 0:
#                 f = 1
#         if f == 0:
#             arr.append(i)
#     for i in arr:
#         print(i)

# # 158

# n = input()
# s = 0
# reqemler = '0123456789'
# for i in n:
#     if reqemler.count(i) == 1:
#         s = s + int(i)
# print(s)


# 169

# n = input()
# s = ''
# for i in range(0,len(n)):
#     if 'a'<n[i]<'z' or 'A'<n[i]<'Z':
#         s = s + str(i)
# print(s)

# 146

# n = int(input())
# arr=[]
# for i in range(n):
#     a=int(input())
#     arr.append(a)
# m = max(arr)
# arr2=[]
# for i in arr:
#     c = i+m
#     arr2.append(c)
# print(arr2)


# # 108

# for i in range(1,1000,2):
#     print(i)


# # 113

# n = int(input())
# f = 0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             f = 1
#     if f == 1:
#         print("Mürəkkəb ədəddir")
#     else:
#         print("Sadə ədəddir")


# # 115

# a = [3,4,15,9,18,16]  
# for i in a:
#     if i**0.5 == int(i**0.5): 
#         print(i)



# # 117

# n = int(input()) # 130
# f = 1
# i = 1
# while f<n: # 1<130
#     i = i+1
#     f = f *i
# print(i-1)

# 118

# a = [3,4,2,1,6,9,7,8,12,10,5,14]
# #    0 1 2 3 4 5 6 7 8  9 10 11
# s = 0
# c = 0
# for i in range(0,len(a)):
#     if i%2!=0 and a[i]%2==0 or i%2==0 and a[i]%2!=0:
#         s = s + a[i]
#         c = c + 1
# print(s/c,s)

# # 119

# x = int(input())
# a = int(input())
# n = a
# while a<x:
#     a = a*n
# if a==x:
#     print('Yes')
# else:
#     print('No')

# # 136
# a = 5
# s = 5
# for i in range(4):
#     a = a + a*20/100
#     s = s + a
# print(s)

# 120

# x = int(input())
# n = int(input())
# s = 1
# f = 1
# for i in range(2,n+1,2):
#     f = f * i
#     s = s + x**i/f
# print(s)

# 142


# # 128

# n = int(input()) # 240135
# b = []
# n = str(n) # '240135'
# for i in n:
#     i = int(i)
#     if i%2!=0:
#         b.append(i)
# if len(b) == 0:
#     print('Ədəddə tək rəqəm yoxdur')
# else:
#     print(min(b))

# 130

# n = int(input()) # 25
# n = str(n)
# onluq = 0
# # reqemler = '01234567'
# L = len(n)-1
# for i in n:
#     onluq = onluq + int(i)*8**L
#     L = L-1
# print(onluq)

# # 141

# n = input() # riyaziyyat
# array = []
# for i in n:
#     if array.count(i) == 0:
#         array.append(i)
# # print(array)

# # 142

# n = int(input())
# n = str(n)
# L = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + int(i)*2**L
#     L = L - 1
# sekkizlik = ''
# while onluq > 0:
#     q = onluq%8
#     sekkizlik = str(q) + sekkizlik
#     onluq = onluq//8
# print(sekkizlik)


# # 142

# # n = input() # 1110
# # L = len(n) 
# # if L%3 == 1:
# #     n = '00' + n
# # elif L%3 == 2:
# #     n = '0' + n
# # s = 0
# # for i in range(0,len(n)):
    
# # 146

# n = int(input())
# i = 0
# while n>0:
#     n = str(n)
#     a = n[0]
#     b = n[len(n)-1]
#     s = int(a)+int(b)
#     n = int(n)
#     n = n-s
#     i = i + 1
# print(i)

# n = int(input())
# f = 0
# while n>0:
#     a = n%10
#     if a>=8:
#         f = 1
#     n = n//10
# if f == 1:
#     print('Mövcud deyil')
# else:
#     print('Mövcuddur')

# n = int(input()) # 208
# n = str(n)  #
# m = max(n)
# if int(m)>=8:
#     print('Mövcud deyil')
# else:
#     print('Movcuddur')

    



# # 144

# p = 100
# a = 1
# while p<=200:
#     p = p + p*5/100
#     a = a + 1
# print(a,p)



# # 145

# s = 29
# x = 29
# g = 1
# while s<=100:
#     x = x + 5
#     s = s + x
#     g = g + 1
# print(g,s)


# # 146

# n = int(input())
# k = 0
# while n>0:
#     a = str(n)[0]
#     b = str(n)[len(str(n))-1]
#     s= int(a) + int(b)
#     n = n - s
#     k = k + 1
# print(k)

# # 147
# # Ixtiyari,random eded üçün
# n = int(input())
# f = 0
# while n>0:
#     q = n %10
#     if q % 2 != 0:
#         f = 1
#     n = n // 10
# if f == 1:
#     print('No')
# else:
#     print('Yes')

# # dordreqemli

# n= int(input())
# a = n//1000
# b = n//100%10
# c = n//10%10
# d = n%10
# if a%2==0 and b%2==0 and c%2==0 and d%2==0:
#     print('Yes')
# else:
#     print('No')


# # 148

# for i in range(200,1000,2):
#     a = i//100
#     b = i//10%10
#     if a%2==0 and b%2==0:
#         print(i)

# # 149

# n = int(input())
# a = str(n%1000)
# s = '5'+a
# print(s)

# # 150
# a = int(input())
# b =int(input())
# if 1000<=a<b<10000:
#     for i in range(a,b+1):
#         a = i//1000
#         b = i//100%10
#         c = i//10%10
#         d = i%10
#         if a!=b!=c!=d and a!=c and a!=d and b!=d:
#             print(i)




# b = 5
# def bmw(s):
#     b = (s[0]+s[len(s)-1])/2*len(s)
#     return b
# a = bmw([4,6,8,10,12])
# print(b,a)


# a = [2,3,4,5]
# b = [2,3,4,5]
# a.append(10)
# a.append(20)
# a.insert(3,40)
# print(b)




# a = 'Salam'
# s = ''
# for i in range(0,len(a)):
#     s = s + str(i)
# a = s
# print(a)



# # sinaq 9
# # 27,28,29,30,26,20,19



# ls = [4121,667,534,62,5557,647]
# maxi = ls[0]
# for i in ls:
#     if maxi<i:
#         maxi = i
# print(maxi)


# # 28

# s = input()
# c = 0
# for i in range(len(s)):
#     if s[i] == 'a':
#         c = c + i
# print(c)


# n = input()
# s = ''
# c = 0
# for i in n:
#     if '0'<=i<='9':
#         s = s + i
#     else:
#         if s != '':
#             c = c + int(s)
#         s = ''
# if s != '':
#     c = c + int(s)
# print(c)

# # 30
# ls = [23,45,623,123,5,67,89,34,12,45,678]
# #     0  1   2   3  4  5 6   7  8 9   10 
# for i in range(len(ls)):
#     if i%2!=0 and ls[i]%2==0:
#         s = ''
#         while ls[i]>0:
#             q = ls[i]%8
#             s = str(q) + s
#             ls[i] = ls[i]//8
#         print(s)
     

# # setir siyahi
# # 74,77,84,49,59,86,62,60,57,
# # 75,79,



# 28

# def simpleOrCompound(x):
#     f = 0
#     x = int(x)
#     for i in range(2,x//2+1):
#         if x%i==0:
#             f = 1
#     return f
# s = 0
# L = input().split()
# for i in L:
#     if len(i) == 3:
#         if simpleOrCompound(i) == 0:
#             s = s + int(i)
# print(s)

# 29

# s = input() 
# c = 0
# for i in s:
#     if s.count(i) == 1:
#         c = c + 1
# print(c)

# # 30

# n = input()
# rqmlr = '0123456789ABCDEF'
# #        012345678910
# L = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + rqmlr.find(i)*16**L
#     L = L-1
# s = ''
# while onluq>0:
#     q = onluq%2
#     s = str(q)+s
#     onluq = onluq//2
# print(s)


# # 127

# n = input().split() # salam necesen yaxshiyam sagol
# for i in n:
#     print(len(i))

# # split() vs list()
# # list -----> Qəssab
# n = 'salam necesen'
# n = list(n)
# print(n)

# # # split
# # n = 'salam necesen'
# # n = n.split()
# # print(n)


# # 129

# n = int(input()) # say
# arr1 = []
# arr2 = []
# arr3 = []
# for i in range(n):
#     a1 = int(input())
#     a2 = int(input())
#     arr1.append(a1)
#     arr2.append(a2)
#     c = a1+a2
#     arr3.append(c)
# print(arr3)


# # 155

# n = input()
# s = ''
# for i in range(len(n)):
#     if 'a'<=n[i]<='z' or 'A'<=n[i]<='Z':
#         s = s + str(i)
#     else:
#         s = s + n[i]
# n = s
# print(n)


# 156

# aylar = ['yanvar',
#          'fevral',
#          'mart',
#          'aprel',
#          'may',
#          'iyun']
# sell = input().split()
# f = 0
# for i in range(len(sell)):
#     sell[i] = int(sell[i])
# for i in range(1,len(sell)-1):
#     if sell[i-1]<sell[i]>sell[i+1]:
#         print(aylar[i],':',sell[i],'eded')
#         f = 1
# if f == 0:
#     print('Uğurlu ay yoxdur')

# # Join
# a = ['2','3','4','5']
# a = ' '.join(a)
# print(a)

# # split()
# a = 'Sebine Huseynova' # str---> list
# a = a.split(' ')
# print(a)

# # list vs split
# # list  ---- Qessab
# a = 'salam necesen'
# a = list(a)
# print(a)


# n= input().split()
# for i in n:
#     print(len(i))


# def simpleOrCompound(n):
#     f=0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             f = 1
#     return f

# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#     if simpleOrCompound(i) == 0:
#         print(i)

# 135

# n = input()
# b = []
# for i in n:
#     if n.count(i) == 1:
#         b.append(i)
# print(len(b))

# # 137
# n = input().split()
# for i in range(len(n)):
#     print(f'daxil edilmiş cümlənin {i+1} saylı sözündə {n[i].count("w")} sayda w simvolu mövcuddur')


# # # 139
# n = int(input())
# b = []
# s = 0
# for i in range(n):
#     a = int(input())
#     b.append(a)
# for i in b:
#     i = str(i)
#     if i.count('1') > 0:
#         s = s + 1
# print(s)


# # # 144

# n = int(input())
# b = []
# if n!=0:
#     for i in range(n):
#         a = int(input())
#         b.append(a)
#     for i in range(len(b)):
#         b[i] = -b[i]
#     print(b)


# a = [2,3,4]
# for i in a:
#     print(i)

# n = input() # asoasooooossada
# #             0123456789
#                       #1011121314
# s = 1
# b = []
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         s = s + 1
#         if i == len(n)-2:
#             b.append(s)
#     else:
#         b.append(s)
#         s = 1
# print(max(b))



# # 162

# a = input().split() # ['301','205','402']
# for i in range(len(a)):
#     maxi = int(max(a[i]))
#     mini = int(min(a[i]))
#     c = maxi**2+mini**2
#     a[i] = c
# print(a)


s = 0
c = 0
# for i in range(2,52,2):
#     c = c + 1
#     s = s+4
# print(s,c)


# v = 112
# s = 0
# while v>100:
#     print(v)
#     v = v//2
#     if v%2==0:
#         s = s +v
# print(s)





# n = 'salam 10-cu adam'
# s = ''
# for i in range(len(n)):
#     if 'a'<=n[i]<='z' or 'A'<=n[i]<='Z':
#         s = s + str(i)
#     else:
#         s = s + n[i]
# n = s
# print(n)


# 170,172,163,164,173,174


# # 172

# n = int(input())
# mus = []
# mef = []
# for i in range(n):
#     a = int(input())
#     if a<0:
#         mef.append(a)
#     elif a>0:
#         mus.append(a)
# if min(mus) + max(mef) > 0:
#     print('Müsbətdir')
# elif min(mus) + max(mef) < 0:
#     print('Müsbət deyil')
# else:
#     print('0-a beraberdir')

# # 173
# n = input()
# s = 0
# b = []
# for i in n:
#     if 'A'<=i<='Z':
#         s = s + 1
#     else:
#         b.append(i)
# print(b,s)

# # '#' simvollarının sayını tap
# i = 1
# while i<6:
#     print('#')
#     if i%2==1:
#         print('###')
#     if i>=4:
#         print('#####')
#     i = i+1

# # 
# p = 1
# i = 3
# while i<=10:
#     p = p*(i%5)
#     i = i+1
# print(p)

# # 
# a = 84
# b = 30
# while a!=0 and b!=0:
#     if a>b:
#         a = a%b
#     else:
#         b = b%a
# print(a+b)



# # 
# a = 22
# s = ''
# while a>0:
#     q = a%2
#     a = a//2
#     s = str(q)+s
# print(s.count('1'))


# # Klaviaturdan 60 ededi daxil edilerse
# n = int(input())
# s = 0
# i = 2
# while s<n:
#     s = s + i
#     i = i+2
# s = s-i+2
# print(s)


# # list
# a = [5,4,5,5,5] #---> [4,5]
# #    0 1 2 3 4         0 1 2 3
# b = []
# for i in a:
#     if i!=5:
#         b.append(i)
# print(b)
# for i in range(0,len(a)):
#     a.remove(a[i])
# print(a)


# # # Klaviaturadan 5 rəqəmi göndərilir
# a = float(input()) # 5.0
# a = str(a)  # '5.0'
# a = a+'1'  # '5.0' + '1' = '5.01'
# a = a *2   # '5.015.01'
# a = a.split('0')  # ['5.','15.','1']
# a = '1'+'1'.join(a) # '1' + '5.115.11' = '15.115.11'
# print(a) 


# Setirler siyahilar

# # 129

# n = int(input())
# a = []
# b = []
# for i in range(n):
#     aElement = int(input())
#     bElement = int(input())
#     a.append(aElement)
#     b.append(bElement)
# c = []
# for i in range(n):
#     cElement = a[i] + b[i]
#     c.append(cElement)
# print(c)

# # 130

# Amil = 16
# Eltac = Amil/2
# Anar = Eltac+5
# c = (Amil + Eltac + Anar)/3
# print(c)

# # 131

# n = int(input())
# a = []
# for i in range(n):
#     b = input()
#     a.append(b)
# s = 0
# for i in a:
#     s = s + len(i)
# print(s)

# # 140

# n = input() # Sd234rdf12
# rqmlr = '0123456789'
# s = ''
# for i in n:
#     if rqmlr.count(i)==0:
#         s = s + i
# print(s)

# # 143

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# for i in range(len(b)):
#     c = i*b[i]
# #     print(c)

# # 145

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# for i in b:
#     i = str(i)
#     c = int(i[0]) * int(i[len(i)-1])
#     print(c)


# # 146

# n = int(input())
# a = []
# b = []
# for i in range(n):
#     c = int(input())
#     a.append(c)
# m = max(a)
# for i in a:
#     b.append(m+i)
# print(b)

# # 147

# n = input() # salam35
# a = '0123456789'
# h = 1
# s = 0
# for i in range(len(n)):
#     if a.count(n[i]) == 1:
#         h = h*int(n[i])
#     else:
#         s = s + i
# print(h,s)

# # 148

# n = int(input()) # 3455
# k = str(n)
# s = k[1:len(k)-1] # 45
# k = k[len(k)-1] + s + k[0]
# k = int(k)
# if k>n:
#     print(k-n)
# elif n>k:
#     print(n-k)

# # 149

# a = [3,4,5,6,7,8,2,9,1,12]
# e = sum(a)/len(a)
# for i in a:
#     if i>e:
#         print(i)

# 150

# n = int(input())
# n = list(str(n))
# n.reverse()
# n = ''.join(n)
# n = int(n)
# print(n)

# 151

# a = [351,648,776,918]
# for i in a:
#     i = str(i)
#     c = (int(i[0]) + int(i[len(i)-1]))*2
#     print(c)

# # 152

# n = input()
# n = n.replace('a','ə')
# n = n.replace('b','a')
# n = n.replace('ə','b')
# print(n)


# 153

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# mf = []
# ms = []
# for i in a:
#     if i<0:
#         mf.append(i)
#     elif i>0:
#         ms.append(i)
# mf = max(mf)
# ms = min(ms)
# print(mf+ms)

# # 154

# n = int(input())
# n = str(n)
# s = ''
# for i in n:
#     if i!='4' and i!='7':
#         s = s + i
# print(s)

# n = '14276'
# #    012345
# n = list(n)
# for i in n:                
#     if i=='7' or i == '4':    
#         n.remove(i)
# print(n)

# # 155

# n = input()
# r = '0123456789'
# s = ''
# for i in range(len(n)):
#     if r.count(n[i]) == 0: 
#         s = s + str(i)
#     else:
#         s = s + n[i]
# print(s)


# def f(x):
#     x = 5
#     print(5)


# # print(f(5))


# a = [2,3,4,5]
# # print(a[-5])

# print(a[0::2])

# a = ['aza','acb']
# print(max(a))


# print('salam\necesen')


# a = [2,3,4,5,6]
# b = [2,3,5,10,12]
# for i in a:
#     if i in b:
#         print(i)


# n = int(input(),base=16)
# print(n)


# def f(n):
#     if n==1:
#         return 1
#     return n * f(n-1)

# a = f(5)
# print(a)


# 
# 30

# s = input() # salam123
# n = ''
# for i in range(len(s)):
#     if '0'<=s[i]<='9':
#         n = n + s[i]
#     else:
#         n = n + str(i)
# print(n) 


# # 140

# n = input() # Sd234rdf12
# rqml = '0123456789'
# s = ''
# for i in n:
#     if rqml.count(i) == 0:
#         s = s + i
# print(s)


# a = [23,44,15,20]
# for i in a:
#     if i==15:
#         break
#     print(i)

