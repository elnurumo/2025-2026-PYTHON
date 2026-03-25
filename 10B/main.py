
# # # Codera
# # # 6,14,7,42,19,24,31,29,45,32,
# # # 25,34,37,46,50,49



# # # python

# # # Data Tiplər
# # # Number ---> Integer Int funksiyası int() Bütün tam ədədlər
# # # float ----> funksiyası float() Bütün həqiqi ədədlər
# # # string ---> funksiyası str() sətir tipi "", ''
# # # boolean ---> funksiyası bool()  True, False
# # # array --->  []

# # # a = 5+4
# # # print(a)

# # # a = 5
# # # b = 14
# # # print(a+b) # 19
# # # print('a'+'b') # ab
# # # print('a+b') # a+b

# # # a = 'a'
# # # b = 5
# # # print(a*b)

# # # +
# # # -
# # # *
# # # /
# # # // böləndə tam hissə
# # # % böləndə qalıq hissi
# # # ** qüvvət üstü

# # # a = 25
# # # # b = a**(1/2)
# # # b = a**0.5
# # # print(b)

# # # a = 5
# # # b = 4
# # # if a>b:  # mudur
# # #     print('1')
# # # elif a==5: # muavin
# # #     print('2')
# # # else: # asistan
# # #     print('3')


# # # a = 10
# # # b = 100
# # # if a<b:
# # #     print(1)
# # # if a!=10:
# # #     print(2)
# # #     if a>10:
# # #         print(3)
# # # elif b<1000:
# # #     print(4)
# # # else:
# # #     print(5)

# # # a = 15
# # # if a%2==0 and a%3==0:
# # #     print('Yes')
# # # else:
# # #     print('No')

# # # If else

# # #
# # # 67-72,

# # # a_b = 5
# # # print(a_b)

# # # end, sep

# # # print('Salam','Necəsən','mandalin',sep='\n')


# # # a = 5
# # # a = a*10
# # # a = a*2
# # # print(a)

# # # print(10)


# # #


# # # a = '2345'
# # # #    0123
# # # print(a[2])

# # # a = ['Zabit','Nazim','Məhəmməd'," Ömür","Zəhra","Elvin",'Onur','Subhan','Amin']
# # # print(a[len(a)-1])


# # # # 101

# # # n = int(input())
# # # a = int(input())
# # # b = int(input())
# # # if n<a:
# # #     print('Solunda')
# # # elif n>b:
# # #     print('Sağında')
# # # else:
# # #     print('Daxilindədir')


# # # # 102

# # # n = int(input())
# # # if n>2:
# # #     if n%2==0:
# # #         print(n-2)
# # #     else:
# # #         print(n-1)
# # # else:
# # #     print('N 2-den boyuk olmalidir')

# # # 103

# # # n = int(input()) # 5665
# # # a = n//100
# # # b = n%100
# # # if a==b:
# # #     print('Beraberdir')
# # # else:
# # #     print('Beraber deyil')


# # # 104

# # # n = int(input()) # 345
# # # n = abs(n)
# # # a = n//100 # 345//100 = 3
# # # b = n//10%10
# # # c = n%10
# # # f = a**3+b**3+c**3 - (a**2+b**2+c**2)
# # # print(f)

# # # a = int(input())
# # # b = int(input())
# # # c = int(input())
# # # if a==b==c:
# # #     print('BTrfli')
# # # elif a!=b and a!=c and b!=c:
# # #     print('Mtrfli')
# # # else:
# # #     print('Byanli')


# # # Codera 11.1


# # # a = 5
# # # a = pow(a,3)
# # # print(a)

# # # array = [1,2,15,20,30,40]
# # # #        0 1 2  3  4  5
# # # print(array[len(array)-1])

# # # split() vs list()
# # # Cərrah
# # # split
# # # a = 'Salam'
# # # a = a.split('a')
# # # print(a) # ['Salam','necesen']

# # # # List
# # # # Qəssab tikəliyir
# # # a = 'salam'
# # # a = list(a)
# # # print(a)

# # # 21
# # # join
# # # listden --->> str

# # # n = ['055','795','45','55']
# # # b = '-'.join(n)
# # # print(b)

# # # print('2'*3)

# # # print('salam\necesen')

# # # # 106
# # n = int(input())
# # if n%6==0:
# #     print('He')
# # else:
# #     print('Yox')

# # # # 107
# # n = int(input()) # 2345//10%10
# # a = n//100%10 # 3
# # b = n//10%10 # 4
# # if b%2!=0:
# #     print(a*b)
# # else:
# #     print(a+b)

# # # 108

# # n = int(input())
# # if n == 12 or n==1 or n==2:
# #     print('Sizin ad gününüz qışdadır.')
# # elif n==3 or n==4 or n==5:
# #     print('Sizin ad gününüz Yazdadır.')
# # elif n== 6 or n==7 or n==8:
# #     print('Sizin ad gününüz Yaydadır.')
# # elif n==9 or n==10 or n==11:
# #     print('Sizin ad gününüz payızdadır.')
# # else:
# #     print('Bele bir ay yoxdur')


# # # # 109

# # n = int(input())
# # if 0<n<=9:
# #     print('Birrəqəmli')
# # elif 10<=n<100:
# #     print('Ikireqemli')

# # # # 110

# # n = int(input()) # 26
# # if n%2==0:
# #     print(n-1,n+1,'tek ededlerdir')
# # else:
# #     print(n-1,n+1,'cut ededlerdir')


# # # # 111

# # import math
# # x = int(input())
# # if x<=5:
# #     y = abs(x+2) + 3*x
# # elif x>7:
# #     y = x**3 - 2
# # else:
# #     y = math.sqrt(3*x**4+10)



# # # # 112

# # a = int(input())
# # b = int(input())
# # if a<b:
# #     z = (3*b)/abs(a-b)+3*(a+b)
# # elif a>b:
# #     z = a**2/abs(a+b)
# # else:
# #     z = (2*a**2+abs(b**3))**0.5

# # # # 113

# # a = int(input())
# # b = int(input())
# # c = int(input())
# # if a == b == c:
# #     print(3)
# # elif a==b or a==c or b==c:
# #     print(2)
# # else:
# #     print(0)


# # # # 114

# # saat1 = int(input())*3600
# # deqiqe1 = int(input())*60
# # saniye1 = int(input())
# # saat2 = int(input())*3600
# # deqiqe2 = int(input())*60
# # saniye2 = int(input())
# # s1 = saat1+deqiqe1+saniye1
# # s2 = saat2+deqiqe2+saniye2
# # print(s2-s1)

# # # # 115
# # a = int(input())
# # b = int(input())
# # c = int(input())
# # if b<a<c:
# #     print('Qiymətcə orta olan=',a)
# # elif a<b<c:
# #     print('Qiymətcə orta olan=',b)
# # elif a<c<b:
# #     print('Qiymətcə orta olan=',c)


# # # 116

# # n = input() # kitab
# #             # 012
# # L = len(n)
# # if L%2==0:
# #     print(0)
# # else:
# #     print(n[L//2])
    
# # # 117

# # n = int(input())
# # if 0<=n<=30:
# #     q = 2
# # elif 31<=n<=60:
# #     q = 3
# # elif 61<=n<=80:
# #     q = 4
# # elif 81<=n<=100:
# #     q = 5
# # print(q)

# # # 118

# # n = input() # aaaa
# # #             0123
# # a = n[0]
# # f = 0
# # for i in n:
# #     if i!=a:
# #         f = 1
# # if f == 0:
# #     print('Eynidir')
# # else:
# #     print('Eyni deyil')


# # # 119

# # n = int(input())
# # if 99<n<1000:
# #     a = n%10
# #     b = n//10%10
# #     c = n//100
# #     if a==b or b==c or a==c:
# #         print('Mümkündür')
# #     else:
# #         print('Mumkun deyil')


# # 120

# # p = float(input())
# # kQ = float(input())
# # kS = p//kQ
# # pQ = p - kQ*kS
# # print(kS,pQ)

# # print(1-0.7)


# # 121

# # x = int(input())
# # y = int(input())
# # if x!=0 and y!=0:
# #     if x>0 and y>0:
# #         print('1-ci rub')
# #     elif x<0 and y>0:
# #         print('2-ci rub')
# #     elif x<0 and y<0:
# #         print('3-cu rub')
# #     else:
# #         print('4-cu rub')


# # # 122
# # Email = 'email@inbox.ru'
# # password = '321abc'


# # # 
# # EmailUser = input() # str tipine sade halda
# # passwordUser = input() # str tipinde sade halda
# # if Email == EmailUser and password ==passwordUser:
# #     print('Xoş geldin')
# # else:
# #     print('Email ve ya şifre yanlışdır')


# # # # 123

# # n = float(input()) # '5.25'
# # k = len(str(n))-2
# # t = int(n//1)
# # k = n*10**k%10**k/10**k  # 2500
# # print(t,k)


# # 11.1
# # 39,20,21,35,36,40


# # a = 'Salam'
# # #    01234
# # k = a[3:2:2]
# # print(k)

# # a = 'Elnurnur'
# # # a = a.lower()
# # # a = a.upper()
# # # a = a.capitalize()
# # # a = a.strip()
# # # a = a.replace('nur','mir')
# # print(a)

# # 
# # aaaabbbb sətrindəki a hərflərini b hərfi ilə, b hərfini a hərfi ilə əvəz edən kodu yaz.

# # a = input() # aaaabbbb
# # a = a.replace('a','*') # ****bbbb
# # a = a.replace('b','a') # ****aaaa
# # a = a.replace('*',"b") # bbbbaaaa
# # print(a)

# # # polindrom 121 232
# # n = int(input())  #-----> str ---- > list
# # k = n
# # n = list(str(n))
# # n.reverse()
# # if list(str(k)) == n:
# #     print('yes')
# # else:
# #     print('no')


# # a = 5
# # def polindrom():
# #     a = 7


# # print(polindrom(),a)


# # a = 'salam'
# # #    01234
# # b = a.find('a',2,4)
# # m = max(a)
# # print(b,m)


# # a = 'Salam'

# # while, for

# # for i in range(1,101,1):
# # #            range(start,stop,step)
# #     print(f'{i}.{a}')

# # a = [12,20,30,40,2,5,50]
# # maximum = a[0] 
# # for i in a:
# #     if maximum < i:
# #         maximum = i
# # print(maximum)

# # m = max(a)
# # print(m)


# # a = [-2,-10,-5,-100]
# # zabit = a[0]
# # for i in a:
# #     if zabit>i:
# #         zabit = i
# # print(zabit)


# # a = 'salam'
# # a = a.capitalize()
# # print(a)

# # a = [20,2,3,4,20,10,20]\
# # #    0  1 2 3 4  5  6
# # # a.append(39) # listin sonuna elave edir
# # # a.remove(20) # ilk 20 i silecek
# # # a.insert(2,40) # daxil edir istediyim indexe 1. index, 2. element
# # # a.sort() # artan sira ile duzur
# # # a.reverse() # tersine duzur 
# # # a = a.index(20) #  tapdigi ilk elementin indexin qaytarir
# # # a = a.count(20) # 20-in sayini qaytarir
# # print(a)


# # # ilk 100 ededin cemi
# # n = 100
# # s = 0
# # while n>0: #--- false
# #     s = s + n
# #     n = n - 1 
# # print(s)

# # Ededin sade ve ya murekkeb oldugun yoxlayir
# # n = int(input())
# # f = 0
# # for i in range(2,n//2+1):
# #     if n%i==0:
# #         f = 1
# # if f == 1:
# #     print('Murekkeb')
# # else:
# #     print('sade')


# # n = int(input())
# # if n%2==0:
# #     print('Cut')
# # else:
# #     print('Tek')


# # n = int(input()) # 257
# # if 99<n<1000:
# #     a = n//100
# #     b = n%10 
# #     print(a+b)

# # for , whiile

# # a = [2,3,4,20]
# # j = 1
# # for i in range(len(a)):
# #     print(i)

# # while

# # # 10 -luqdan 8-liye keçid
# # n = 123
# # s = ''
# # while n>0:
# #     q = n%8
# #     s = str(q) + s
# #     n = n//8
# # print(s)

# # s = '4' + '5'
# # print(s)


# # s = 23//10%2**3
# # print(s)


# # 44,47,52

# # # 124

# # n = int(input())
# # b = int(input())
# # s = 0
# # if b!=0:
# #     for i in range(1,n):
# #         if i**2%b == 0:
# #             s = s + 1
# #     print('ədədlərin sayı',s)


# # # 125

# # n = int(input()) # 
# # c = 0
# # s = 0
# # while n>0:
# #     q = n%10
# #     if q%2!=0:
# #         c = c + q
# #         s = s + 1
# #     n = n//10
# # print(c,s)

# # # 126

# # n = int(input()) # 27
# # k = n**(1/3)
# # if k == int(k): # 3.0 == 3
# #     print('yes')
# # else:
# #     print('No')


# # # 127

# # R = int(input())
# # x1 = int(input())
# # y1 = int(input())
# # x2 = int(input())
# # y2 = int(input())
# # if (x1-y1)**2+(x2-y2)**2==R**2:
# #     print('yes')
# # else:
# #     print('no')




# # a = 'salam necesen'
# # a = a.split() # ['salam','necesen']
# # # a = ' '.join(a)
# # # a = list(a)
# # for i in a:
# #     print(len(i))
# # # print(a)

# # n = input().split() # ['5','15']
# # a = int(n[0])*int(n[1])
# # print(a)

# # # 12

# # n = input().split() # ['25','7','88']
# # # 25 7 8
# # s = int(n[0])%10 + int(n[1])%10 + int(n[2])%10
# # print(s)

# # # 15

# # a = int(input())
# # b = int(input())
# # if 9<a<100 and 9<b<100:
# #     t = a%10+b%10
# #     o = a//10 + b//10
# #     print(t,o)


# # 

# # # for Etrafli
# # 120,124


# # # 106
# # n = int(input()) # say 5
# # b = []
# # if n>0:
# #     for i in range(n): # [0;n)
# #         a = int(input())
# #         b.append(a)
# #     c = min(b)
# #     print(c)

# # # 109

# # a = [15,12,16,11,9]
# # for i in a:
# #     if i%2!=0:
# #         print(i*i)



# # # 110
# # s = 0
# # for i in range(1,100):
# #     i = str(i)
# #     s = s + i.count('3')
# # print(s)

# # # 111
# # n = int(input()) # say 5
# # k = []
# # m = []
# # for i in range(n):
# #     a = int(input())
# #     if a%2==0:
# #         m.append(a)
# #     else:
# #         k.append(a)
# # print(m,k)

# # 114

# # n = int(input())
# # if n>0:
# #     s = 0
# #     for i in range(1,n+1,1):
# #         s = s + (-1)**(i+1)*i*(i+1)
# #     print(s)

# # # 116
# # s = 0
# # for x in range(-10,11):
# #     if x>3:
# #         y = x**2-5*x+6
# #     else:
# #         y = (x+2)**2
# #     if y%3==0:
# #         s = s + 1
# # print(s)

# # 119

# # x = int(input())
# # a = int(input())
# # if x>1 and a>1:
# #     q = 0
# #     while x>1:
# #         x = x/a
# #         q = q + 1
# #     if x == 1:
# #         print('Yes')
# #     else:
# #         print('no')

# # # 120

# # x=int(input())
# # n=int(input())
# # f = 1
# # s = 1
# # for i in range(1,n+1,1):
# #     f = f * i
# #     if i%2==0:
# #         s = s + x**(i)/f
# # print(s)


# # 100
# # Ədədlər 3 tipi var
# # İnteger, Float, Complex

# # n = int(input()) # 2564
# # n = str(n)
# # for i in n:
# #     print(i)

# # a = 'Salam'
# # a = a.index('a',2,1)
# # print(a)

# # # list
# # a = [5,3,2,5]
# # a = a.count(5)
# # print(a)
# # # None

# # # split
# # # string ----> list
# # a = '101010102030405'
# # a = a.split('0')
# # print(a) # ['1','1','1','1','2','3','4','5']


# # # join
# # # list ---> string
# # a = ['Kenan','Dəmirzadə']
# # a = ' '.join(a)
# # print(a)

# # # 
# # a = 'salam'
# # a = list(a) # qessab
# # print(a)

# # print('a','b','c',' ',sep='#')

# # print(5)
# # print(7,end=' ')
# # print(8)


# # # Klaviaturadan 5 rəqəmi göndərilir
# # a = float(input()) # 10.0
# # a = str(a)  # '10.0'
# # a = a+'1' # '10.0' + '1' = '10.01'
# # a = a *2  # '10.01' * 2 = '10.0110.01'
# # a = a.split('0')  # ['1','.','11','.','1']
# # a = '1'+'1'.join(a)  # '1' + '11.1111.11' = '111.1111.11'
# # print(a) # '111.1111.11'

# # print('a','b','c',sep='@',end=' ')                   
# # print('d','\ne',end='*')
# # print('c,d')  

# # # a@b@c d
# # # e*c,d

# # print('a','b','c',sep='\n')
# # # a
# # # b
# # # c

# # # 101

# # n = int(input())
# # n = n+1
# # while n%2==0 or n%3==0 or n%5==0:
# #     n = n + 1
# # print(n)

# # # 102

# # n = int(input())
# # s = 0
# # for i in range(1,n+1,1):
# #     s = s + 1/i**2
# # print(s)

# # # # 103

# # n = int(input())
# # # s = 0
# # # for i in range(1,n+1,2):
# # #     s = s + (1/i)**i
# # # print(s)

# # # 104

# # n = int(input()) # 2400
# # s = 0
# # k = str(n) # '2400'
# # for i in k: 
# #     s = s + int(i)
# # if n%s==0:
# #     print('Bölünür!')
# # else:
# #     print('Bölünmür!')


# # # 105

# # n = int(input()) # 5
# # s = 0
# # for i in range(n):
# #     a = int(input())
# #     s = s + a
# # print(s/n)

# # n = int(input())
# # a = []
# # for i in range(n):
# #     b = int(input())
# #     a.append(b)
# # print(min(a))


# # # 110

# # s = 0
# # for i in range(1,100):
# #     while i > 0:
# #         q = i%10
# #         if q==3:
# #             s = s + 1
# #         i = i//10
# # print(s)


# # sep, end

# # print('5','6',sep='2')
# # print(7)



# # 124

# # n = int(input())
# # s = 0
# # f = 1
# # k = -1
# # if n>0:
# #     for i in range(1,n+1):
# #         f = f * i
# #         s = s + k*(1/(f)**i)
# #         k = -k
# #     print(s)


# # n = int(input())
# # s = 0
# # k = 1
# # if n>=3:
# #     for i in range(3,n+1,2):
# #         s = s+i*k
# #         k = -k
# # print(s)


# # #126
# # s=0
# # for i in range(100,1000):
# #     a=i%10
# #     b=i//10%10
# #     c=i//100
# #     if a%3==0 and b%3==0 and c%3==0:
# #         s=s+1
# # print(s)


# # 127
# # s=0
# # for i in range(1000,10000):  
# #     a = i//1000
# #     b = i//100%10
# #     c = i//10%10
# #     d = i%10
# #     if a%2==1 and b%2==1 and c%2==1 and d%2==1:
# #         s = s+i
# # print(s)       


# # # 128
# # n= int(input())
# # b=[]
# # n= str(n)
# # for i in n :
# #     i=int(i)
# #     if i%2==1:
# #         b.append(i)
# # if len(b) == 0   :
# #     print("YOXDUR")
# # else:
# #     print(min(b))    


# # n = int(input(),base=2)
# # print(n)


# # n = input() # '2B'
# # rqmlr = '0123456789ABCDEF'
# # #        012345678910
# # L = len(n)-1
# # onluq = 0
# # for i in n:
# #     onluq = onluq + rqmlr.find(i)*16**L
# #     L = L - 1
# # print(onluq)



# # n = input() # '2B'
# # rqmlr = '01234567'
# # #        012345678910
# # L = len(n)-1
# # onluq = 0
# # for i in n:
# #     onluq = onluq + rqmlr.find(i)*8**L
# #     L = L - 1
# # print(onluq)


# # # 131
# # m = int(input())
# # for i in range(100,1000):
# #     a = i%10
# #     b = i//10%10
# #     c = i//100
# #     if a*b*c==m and a!=1 and b!=1 and c!=1:
# #         print(i) 


# # # 132
# # n = int(input()) # 257
# # s = 0
# # if n>0:
# #     n = str(n)
# #     for i in n:
# #         i = int(i)
# #         if i%2!=0:
# #             s = s + 1
# #     print(s)

# # 133

# # n = int(input()) # 20
# # sade_vuruq = 2
# # while n!=1:
# #     if n%sade_vuruq==0:
# #         n = n//sade_vuruq
# #         print(sade_vuruq)
# #     else:
# #         sade_vuruq = sade_vuruq+1


# # # sade bolen
# # n = int(input()) # 20
# # sade_vuruq = 2
# # b = []
# # while n!=1:
# #     if n%sade_vuruq==0:
# #         n = n//sade_vuruq
# #         if b.count(sade_vuruq) == 0:
# #             b.append(sade_vuruq)
# #             print(sade_vuruq)
# #     else:
# #         sade_vuruq = sade_vuruq+1


# # # 134

# # n = int(input())
# # n = str(n)
# # m = min(n)
# # s = n.count(m)
# # print(s)


# # # 135

# # n = int(input()) # 32 
# # k = n
# # q = 0
# # while n/2>=1:
# #     n = n//2       # 16, 8, 4, 2, 1
# #     q = q + 1
# # if k == 2**q:
# #     print(q)
# # else:
# #     print('2-in quvveti deyil')


# # # 136

# # d = 1
# # r = 5
# # q = 5
# # while d<=5:
# #     d = d + 1
# #     q = q+q*20/100
# #     r = r + q
# # print(r)

# # r= 5
# # q= 5
# # for i in range(1,6):
# #     q = q+q*20/100
# #     r = r + q
# # print(r)


# # # 137

# # x = int(input())
# # n = int(input()) # 5
# # f = 1
# # s = 0
# # for i in range(1,n+1,1):
# #     f = f * i
# #     s = s + (-1)**(i+1)*x**i/f
# # print(s)

# # # 138

# # n = int(input())
# # if n%2!=0:
# #     s = 0
# #     for i in range(1,n+1,2):
# #         s = s + i*(i+1)*(i+2)
# #     print(s)

# # # 139

# # n = int(input())
# # s = 0
# # for i in range(1,n+1):
# #     s = s + i*(i+1)
# # print(s)


# # 140

# # n = input() # Dim9912info2
# # rqmlr = '0123456789'
# # s = 0
# # for i in n:
# #     if rqmlr.count(i) == 1:
# #         s = s + 1
# # print(s)

# # n = input()
# # s = 0
# # for i in n:
# #     if '0'<=i<='9': # ASCII cədvəlinə əsasən
# #         s = s + 1
# # print(s)

# # # 141

# # n = input()
# # b = []
# # for i in n: # riyaziyyat
# #     if b.count(i) == 0:
# #         b.append(i)
# # print(b)

# # # 142
# # n = int(input()) # 1001110
# # n = str(n)
# # onluq = 0
# # L = len(n)-1  # 7-1 = 6
# # for i in n:
# #     onluq = onluq + int(i)*2**L
# #     L = L - 1
# # s = ''
# # while onluq>0:
# #     q = onluq%8
# #     s = str(q) + s
# #     onluq = onluq//8
# # print(s)


# # # 143

# # n = int(input())
# # n = str(n)
# # f = 0
# # for i in n:
# #     if i>='8':
# #         f = 1
# # if f == 1:
# #     print('Mövcud deyil')
# # else:
# #     print('Mövcuddur')



# # 

# # proqramın icrası zamanı ilk olaraq 38 daha sonra 5 daxil edilərsə, ekranda hansı ədəd çap olunar?
# # a = int(input()) # 38
# # b = int(input()) # 5
# # while a>=b: 
# #     a=a-b 
# # print(a)


# # a = [2,3,4,5]
# # a = a.append(5)
# # print(a)

# # def f(x):
# #     a= x
# #     print(a)
# #     return a

# # print(f(5))


# # List - in daxildeki elementi dəyişmək istəyirəmsə, indexsinə müraciət edəcəm yəni 
# # range(0, len(a)) -le for dövrünə salmalıyam 

# # a = [2,3,4,5]
# # for i in range(0, len(a)):
# #     a[i] = str(a[i])

# # a = ''.join(a)
# # print(a)

# # Sətrin daxilini dəyişmək istəsəm

# # a = 'salam123'
# # rqmlr = '0123456789'
# # b = []
# # for i in range(len(a)):
# #     if rqmlr.count(a[i]) == 0:
# #         a[i] = str(i)
# # print(a)

# # a = 'salam123'
# # rqmlr = '0123456789'
# # s = '' 
# # for i in range(len(a)):
# #     if rqmlr.count(a[i]) == 0:
# #         s = s + str(i)
# #     else:
# #         s = s + a[i]
# # print(s)



# # a = 5
# # b = a
# # b = 7
# # print(a,b)

# # a = [2,3,4]
# # b = a
# # a.append(5)

# # print(a,b)

# # 33*




# # a = ['z','yyyybc']
# # print(max(a))

# # a = 'salam123'
# # #    0123
# # s = ''
# # r = '0123456789'
# # for i in range(0,len(a)):
# #     if r.count(a[i]) == 1:
# #         s = s + a[i]
# #     else:
# #         s = s + str(i)
# # print(s)





# # a = 5
# # print(f'a-ın dəyər\n{a}-dir')

# # print("""Salam 
# # Aleykum""")


# # # 29

# # a = input() #'Alma10Armud11Heyva'
# # s = ''
# # b = []
# # for i in a:
# #     if i>='0' and i<='9':
# #         s = s + i
# #     else:
# #         if s != '':
# #             b.append(int(s))
# #             s = ''
# # if s != '':
# #     b.append(int(s))
# #     s = ''
# # print(sum(b))

# # 30

# # ls = [23,45,623,123,5,67,89,34,12,45,678]
# # for i in range(0,len(ls)):
# #     s = ''
# #     if i%2!=0 and ls[i]%2==0:
# #         while ls[i]>0:
# #             q = ls[i]%8
# #             s = str(q) + s
# #             ls[i] = ls[i]//8
# #         print(s)


# # Codera 9.2
# # 1,9,12,13,35,36,67




# # def cəm(x):
# #     s = 0
# #     for i in x:
# #         s = s + i
# #     return s

# # a = [2,4,5,10,20,30]
# # c = cəm(a)
# # print(c)

# def maximum(a):
#     maximum = a[0]
#     for i in a:
#         if i > maximum:
#             maximum = i
#     return maximum

# a = [-2,-4,-5,-10,-20,-30]
# #     0   1  2  3   4   5
# print(maximum(a))






# count, index, join 3 dənəsi mənimsədilərək yazılır
# a = ['2','3','4','5','3']
# s = a.count('3')
# i = a.index('3')
# j = ''.join(a)
# print(s,i,j) 


# Recursion (rekursiv funksiya) function

# def f(x):
#     if x==1:
#         return 1
#     return x + f(x-1)

# a = f(5)
# print(a)


# 127

# n = input().split() # salam necesen\
# # ['salam','necesen']
# for i in n:
#     print(len(i))


# # 128
# n = int(input())
# n = list(str(n))
# n.sort()
# n.reverse()
# n = ''.join(n)
# print(n)

# n = int(input())
# arr = []
# s = 0
# if 99<n<1000:
#     a = n//100
#     b = n//10%10
#     c = n%10
#     arr.append(a)
#     arr.append(b)
#     arr.append(c)
#     for i in arr:
#         if max(arr) == i:
#             a = i*100
#         elif min(arr) == i:
#             c = i
#         else:
#             b = i*10
#     print(a+b+c)


# # 129

# n = int(input())
# c = []
# for i in range(1,n+1):
#     a = int(input())
#     b = int(input())
#     s = a+b
#     c.append(s)
# print(c)


# # 130
# n = int(input())
# c = []
# for i in range(n):
#     a = int(input())
#     c.append(a)
# print(sum(c)/n)

# # 131

# n = int(input())
# a = []
# for i in range(n):
#     s = input('Ad daxil et: ')
#     a.append(len(s))
# print(sum(a))

# 132

# s = input() # hebirbiro worbird
# s = s.replace('1','bir')
# print(s)

# # 133

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     if 9<b<100:
#         a.append(b)
# y = []
# for i in a:
#     i = str(i)
#     s = int(i[0]) + int(i[1])
#     y.append(s)
# print(y)

# 134

# n = input().split()
# print(len(n))

# # 135
# n = input() # 'Hello world'
# b = []
# for i in n:
#     if n.count(i)==1:
#         b.append(i)
# print(len(b))


# # 136
# n = ['yusif','maqa2','elvin','subha']
# a = []
# for i in n:
#     a.append(len(i))
# print(max(a))


# 137

# n=input()
# n=n.split()
# for i in range(0,len(n)):
#     s = n[i].count('w')
#     print(f'daxil edilmis cümlənin {i+1} saylı sözündə {s} sayda w simvolu mövcuddur.')
#     print('daxil edilmis cümlənin', i+1 ,'saylı sözündə', s ,'sayda w simvolu mövcuddur.')


# # 138

# n = int(input())
# if n>99:
#     n = list(str(n))
#     n.sort()
#     n.reverse()
#     n = ''.join(n)
#     n = int(n)
#     print(n)


# 139

# n = int(input()) # 5
# a = []
# i = 1
# while i<=n:
#     b = int(input()) # 251
#     a.append(b)
#     i = i + 1
# s = 0
# for i in a:
#     i = str(i)
#     if i.count('1') > 0:
#         s = s + 1
# print(s)
    


# 140

# n = input()
# r = '0123456789'
# s = ''
# for i in n:
#     if r.count(i) == 0:
#         s = s + i
# print(s)

# # 141

# n = input() # salam ---> salm
# b = []
# for i in n:
#     if b.count(i)==0:
#         b.append(i)
# b = ''.join(b)
# print(b)


# # 142

# n = input().split() 
# s = 0
# for i in n:
#     if i.count('s') > 0:
#         s = s + 1
# print(s)

# # 143

# n = int(input()) # 3
# c = []
# for i in range(0,n):
#     b = int(input())
#     c.append(b)
# a = []
# for i in range(len(c)):
#    d = i*c[i]
#    a.append(d)
# print(a)

# 144

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     if a != 0:
#         b.append(a)
# for i in range(len(b)):
#     b[i] = -1*b[i]
# print(b)



# Sınaq 9
# 


# def f(n):
#     t = 0
#     while n!=0:
#         r = n%10
#         t = t*10+r
#         n = n//10
#     return t
# ls = [234,121,567,343,111]
# c = 0
# for x in ls:
#     if x == f(x):
#         c = c + 1
# print(c)


# # 28
# def simpleOrCompound(n):
#     f = 0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             f = 1
#     return f


# L = [245,354,421,865,103]
# s = 0
# for i in L:
#     if simpleOrCompound(i) == 0:
#         s = s + i
# print(s)

# # 145

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# c = []
# for i in a:
#     i = str(i)
#     h = int(i[0])*int(i[len(i)-1])
#     print(h,end=' ')


# # 146

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# m = max(b)
# c = []
# for i in b:
#     s = i+m
#     c.append(s)
# print(c)


# 147

# n = input() # sal%*&am256
# b = []
# h = 1
# s = 0
# rqml = '0123456789'
# for i in range(0,len(n)):
#     if rqml.count(n[i]) == 1:
#         h = h * int(n[i])
#     else:
#         s = s + i
# print(s,h)

# n = int(input()) # 2345
# n = str(n) # '2345'
# a = n[0] # '2'
# b = n[-1] # '5'
# k = n[1:len(n)-1] # '34'
# s = int(b+k+a)
# n = int(n)
# if n > s:
#     print(n-s)
# elif s>n:
#     print(s-n)
# else:
#     print('Ededler beraberdir')


# # 149

# a = [3,4,5,6,7,8,2,9,1,12]
# average = sum(a)/len(a)
# for i in range(len(a)):
#     if a[i]>average:
#         print(a[i],end=' ')

# # 150

# n = int(input())
# n = list(str(n))
# n.reverse() # [2,34]
# n = ''.join(n)  # n = str(n)  # '[2,34]'
# n = int(n)
# print(n)

# # 151

# a = [351,648,776,918]
# for i in a:
#     i = str(i)
#     c = (int(i[0]) + int(i[len(i)-1]))*2
#     print(c)

# 152
# 1-ci Üsul
# n = input() # aaaabbbb
# n = n.replace('a','*')
# n = n.replace('b','a')
# n = n.replace('*','b')
# print(n)

# # 2-ci üsul

# n = input() # aaaabbbbcccc
# s = ''
# for i in n:
#     if i == 'a':
#         s = s + 'b'
#     elif i == 'b':
#         s = s + 'a'
# n = s
# print(n)

# # 154

# n = int(input())
# s = ''
# n = str(n)
# for i in n:
#     if i!='4' and i!='7':
#         s = s + i
# print(s)

# # 155

# n = input() 
# rqmlr = '0123456789'
# b = ''
# for i in range(len(n)):
#     if rqmlr.count(n[i])>0:
#         b = b + n[i]
#     else:
#         b = b + str(i)
# print(b)

# # 156

# months = ['yanvar','fevral','mart','aprel','may','iyun']
# b = []
# for i in months:
#     s = int(input())
#     b.append(s)
# f = 0
# for i in range(1,len(b)-1):
#     if b[i]>b[i-1] and b[i]>b[i+1]:
#         print(f'{months[i]}:{b[i]} ədəd')
#         f = 1
# if f == 0:
#     print('Uğurlu ay yoxdur')


# # 157

# a = int(input())
# b = int(input())
# if 2<=a<b:
#     for i in range(a,b+1):
#         f = 'sade'
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 f = 'murekkeb'
#         if f == 'sade':
#             print(i)
    

# # 158

# n = input()
# rqmlr = '0123456789'
# s = 0
# for i in n:
#     if rqmlr.count(i) > 0:
#         s = s + int(i)
# print(s)

# # 159

# n = int(input())
# n = str(n)
# maximum = int(max(n))
# minimum = int(min(n))
# s = maximum+minimum
# if s%2 == 0:
#     print('Cüt')
# else:
#     print('Tək')

# 160

# n = input() # aabbbaaabc
# s = 0
# b = []
# for i in n:
#     if i == 'a':
#         s = s + 1
#     else:
#         if s != 0:
#             b.append(s)
#             s = 0
# if s != 0:
#     b.append(s)
#     s = 0
# print(max(b))


# # 161

# shifre = input()
# rqmlr = '0123456789'
# b = []
# for i in rqmlr:
#     if shifre.count(i) == 0:
#         b.append(i)
# print(b,len(b))

# # 162

# a = [256,342234,432,4332,555,3451]
# for i in range(len(a)):
#     m = str(a[i])
#     mini = int(min(m))**2
#     maxi = int(max(m))**2
#     s = maxi+mini
#     a[i] = s
# print(a)


# 163


# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('B.t')
# elif a!=b!=c and a!=c:
#     print('M.t')
# else:
#     print('B.y')



# n = int(input()) # 1212
# if 999<n<10000:
#     a = n//100%10
#     b = n//10%10
#     if b%2==0:
#         print(a+b)
#     else:
#         print(a*b)



# def checkPolindrom(x):
#     return x


# a = checkPolindrom(10)

#111
# x = int(input())
# if x<=5:
#     y= abs(x+2)+3*x
# elif 5<x<=7:
#     y = (3*x**4+10)**0.5
# else:
#     y = x**3-2
# print(y)

#112
#a= int(input())
# b = int(input())
# if a<b:
#     z = 3*b/abs(a-b)+3*(a+b)
# elif a==b:
#     z = (2*a**2+abs(b**3))*0.5
# else:
#     z = a**2/abs(a+b)
# print(z)

#113 Aminin senet eseri
# n = int(input())
# a = int(input())
# b = int(input())
# d = int(input())
# e = int(input())
# c = int(input())
# if 0<n<24 and 0<a<60 and 0<b<60 and 0<d<24 and 0<e<60 and 0<c<60:
#      y= n*1000+a*100+b*10-(d*1000+e*100+c*10)
#      f = y//1000 *3600
#      g = y%1000//10*60
#      h = y%10
#      print(f+g+h)




