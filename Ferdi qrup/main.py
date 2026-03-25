# aparat təminatı toplu
# 

# a = 5
# b = 4
# print(a+b)



# # 145

# n = int(input()) # 5
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# for i in b:
#     i = str(i)
#     h = int(i[0])*int(i[len(i)-1])
#     print(h)


# 146

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# c = []
# m = max(b)
# for i in b:
#     s = i + m
#     c.append(s)
# print(c)


# 147

n = input()
h = 1
c = 0
rqml = '0123456789'
for i in range(0,len(n)):
    if rqml.count(n[i]) == 1:
        h = h * int(n[i])
    else:
        c = c + i
print(c,h)