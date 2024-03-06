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




