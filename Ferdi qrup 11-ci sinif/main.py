# 103

n = int(input()) # 1212
#                  0123
if 999<n<10000:
    n = str(n)
    a = n[:2]
    b = n[2:]
    if a==b:
        print('Beraberdir')
    else:
        print('Beraber deyil')


# boolean
#     0     1
a = ['aa','a','aab','abc','aaaaabbbccc']
#     01   012  
a.sort()
print(a) # a, aa , aaaaabbbccc, aab , abc



a = 5
b = 7
print(a+b) # 12
print('a'+'b') # ab
print('a+b') # a+b


# 104

a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('Bereberterefli')
elif a!=b!=c and a!=c:
    print('muxtelif terefli')
else:
    print('Beraberyanli')


108


n = int(input())
if n == 12 or  n == 1 or n==2:
    print('Sizin ad gününüz qışdadır')
elif 3<=n<=5:
     print('Sizin ad gününüz yazdadır')
elif 6<=n<=8:
      print('Sizin ad gününüz yaydadır')
elif 9<=n<=11:
      print('Sizin ad gününüz payızdadır')
else:
     print('Belə bir ay sırası yoxdur!!!')


# 111
# 1-ci usul
a = 25
b = a**0.5

# 2-ci usul

import math
x = int(input())
if x<=5:
    y = abs(x+2)+3*x
elif x>7:
    y = x**3-2
else:
    y = math.sqrt(3*x**4+10)
print(y)



# 114

saat1 = int(input())*3600
deqiqe1 = int(input())*60
saniye1 = int(input())
saat2 = int(input())*3600
deqiqe2 = int(input())*60
saniye2 = int(input())
s1 = saat1+deqiqe1+saniye1
s2 = saat2+deqiqe2+saniye2
print(s2-s1)


a = 5
b = 3
print(f'qiymətcə orta olan={a}')
print('qiymetce orta olan=',a,sep='')

print('Səfərli', 'Asif',sep='\n')
print('salam\necesen')

n = input()
if len(n)%2==0:
    print(type(0))
else:
    print(n[len(n)//2])

# 118

n = input()
a = n[0]
if len(n)== n.count(a):
    print('Eynidir')
else:
    print('Eyni deyil')


n = int(input())
n = str(n)
k = list(str(n))
k.reverse()
k = ''.join(k)
a = n[0]
b = n[1]
if k==n:
    print('Zaten Polindrom ededdir')
elif n.count(a)==2 or n.count(b)==2:
    print('Mumkundur çevirmək')
else:
    print('Mumkun deyil')

n = float(input())  # '5.67'
k = len(str(n))
n = n*10**(k-2)
t = int(n//10**(k-2)) # 5
k = n%10**(k-2)/10**(k-2)
print(t,k)


a = float(input())
c = int(a-a%1)
b = a-a//1
if b==0.0:
    b=int(b)
print(c,b)


n = 'salam123' # 01234123
s = ''
rqmlr = '0123456789'
for i in range(len(n)):
    if rqmlr.count(n[i]) == 0:
        s = s + str(i)
    else:
        s = s + n[i]
n = s
print(n) 

# ETRAFLILAR

# 119

x = int(input())
a = int(input())
while x%a==0:
    x = x//a
if x == 1:
    print('Yes')
else:
    print('No')


# 129

n = int(input(),base=16)
print(n)

n = input().upper() # AA
rqmlr = '0123456789ABCDEF'
k = len(n)-1
onluq = 0
for i in n:
    onluq = onluq + rqmlr.index(i)*16**k
    k = k - 1
print(onluq)

# 119

n = int(input())
if 99<n<1000:
    n = str(n)
    a = n[1]
    if n[0]==n[2]:
        print('Zaten polindrom ededdir')
    elif n.count(a)==2:
        print('Mümkündür')
    else:
        print('Mumkun deyil')




# 133

n = int(input())
sade_bolen = 2
b = []
while n > 1:
    if n%sade_bolen==0:
        n = n // sade_bolen
        if b.count(sade_bolen) == 0:
            b.append(sade_bolen)
            print(sade_bolen,end=' ')
    else:
        sade_bolen = sade_bolen+1


# List vs Split
# list  ----- Qessab
n = 'salam necesen'
n = list(n)
print(n)
#  str ---->>>> list oxşar yanı
# split ---- NUsret
n = 'salam necesen'
n = n.split('')
print(n)

# str() vs join() array ---->> string
n = ['051','391','23','33']
n = str(n)
print(type(n))

n = ['051','391','23','33']
n = '-'.join(n)
print(n)

# Recursive function

def f(x,y):
    if x == 1:
        return y
    return x * f(x-1,y)

b = 1
a = f(5,b)
print(a)


# Klavituradan daxil edilmiş setrin reqem simvolların olduğu kimi saxla, herif simvollarını 
# isə indexsi ilə əvəz et
# String-də
n = input()
rqmlr = '0123456789'
s = ''
for i in range(len(n)):
    if rqmlr.count(n[i]) == 0:
        s = s + str(i)
    else:
        s = s + n[i]
n = s
print(n)

# List-də elementi dəyişirəmsə, indexinə müraciət edəcəm.

a = [20,40,30,50]
b = []
for i in a:
    b.append('salam')
a = b
print(a)

a = 5
b = a
a = a + 5
b = b + 10
print(a,b)

#  boolean --- > True , False
#                 1      0
a = [2,30,45,50,25]
b = [2,30,45,50,25]
print(a==b)
a.append(100) # [2,30,45,50,25,100]
b.append(20)  # [2,30,45,50,25,20]
print(a,b)