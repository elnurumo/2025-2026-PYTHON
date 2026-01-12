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


# evə
# 71, 72, 76, 77, 80, 81, 85, 90, 93, 94



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


# Etrafli
# 111,114,104,116,103,118,122,124,112
# 110,126,113,121,119,109

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

# split ---- str ---> list
a = 'salam necesen'
a = a.split(' ')
for i in range(len(a)):
    if a[i] == 'salam':
        a[i] = a[i].split('a')
        a[i] = ''.join(a[i])
    else:
        a[i] = a[i].split('e')
        a[i] = ''.join(a[i])
a = ' '.join(a)
print(a)

# # join list----> str
# a = ['051','391','23','33']
# a = '-'.join(a)
# print(a)
