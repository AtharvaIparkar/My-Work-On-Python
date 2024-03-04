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





