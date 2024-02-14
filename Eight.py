
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

a=[1,2,3,5,14,33]
print(sum(a))
b=(sum(a)/len(a))
print(b)
if len(a):


