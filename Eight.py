l=[10,21,30,70,20,25,35,49,'a','b','c']
a=[]
b=[]
letters=[]
for i in l:
    if isinstance(i,int):
        if i%5==0:
            a.append(i)
        if i%7==0:
            b.append(i)
    else:
        letters.append(i)
print(a)
print(b)
print(letters)

# Adding input to a list
a=[]
while True:
    d=input()
    if d =="":
        break
    else:
        a.append(d)
print(a)

# Finding the average of no. present in list
a=[]
while True:
    d=input()
    if d =="":
        break
    else:
        a.append(float(d))
print(a)
print(sum(a))
print(sum(a)/len(a))

# Finding the no. of vowels in a given string
s="Create A Triangle By Word"
count=0
ss = s.lower()
for x in ss:
    if x in 'aeiou':
        count+= 1
print(count)

# Reversing a string
user = "Ram is a Good Boy"
line = user.split()
line = line[ ::-1]
rev_str = " "
for word in line:
    rev_str = rev_str + word + " "
print(rev_str)

# Function for addition of no. given by user
def add(*a):
    sum = 0
    for num in a:
        sum += num
    print(sum)
add(1,2,3,4,5)

# Displaying first letter of input and also in capital using a function
def format_name(name):
    d = ""
    s = name.split()
    for part in s:
        d += part[0].upper( ) + '.'
    return d[:-1]
print(format_name("raam sharma"))

# To convert no. taken as input in form of string into words using a function
def alpha_num(n):
    d = {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten"}
    for i in n:
        print(d[int(i)])
alpha_num("0123")

#Reversing a string using a function
def w(n):
    x=" "
    for i in range(len(n)-1,-1,-1):
        x+=n[i]
    print(x,end=" ") 
w("Hello")

    




