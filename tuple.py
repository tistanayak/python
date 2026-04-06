tup=("A","B","A","D","A","C","B","A")
print("Original tuple", tup)
li=list(tup)
li[0]='PYTHON'
li[2]='CODE'
print(li)
b=[3,4,5]
b[0]=10
print(b)
a=(3,4,5)
c=list(a)
c[0]=12
print(c)
a=tuple(c)
print(a)
a=(3,4,5)
a=(24,)+a[1:]
print(a)

a=[2,24,10,16,15,25,84,45,12,13]
print(a[0:])
print(a[1:9:2])
print(a[-9])
print(a[::-1])
print(a[9::-1])


#STRING
str="Arghojit Das"
str[0]="S"
print(str)


str="racecar"
print(str==str[::-1])
