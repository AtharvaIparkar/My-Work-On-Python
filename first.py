a=[1,2,3,8.7,"name"]
a.reverse()
print(a)

a=tuple()
a.reverse()
print(a)

t=("name",1,5.4)
print(type(t))

b=[]
for i in range(0,10):
    b.append(i)
print(b)

ls=[]
for i in range(10,0,-1):
    ls.append(i)
print(ls)



name=input()
if name=="ZEAL":
    print("OK")
else:
    print("Not OK")

n=int(input())
if n==0:
    print("zero")
elif n<0:
    print("negative")
else:
    print("positive")

name=input()
branch=input()
if branch=="cs":
    print("allowed")
elif branch=="it":
    print("allowed")
else:
    print("not allowed")

name=input()
branch=input()
if name=="zeal" and branch =="cs" or branch == "it":
    print("allowed")
else:
    print("not allowed")
    
for i in range(1,1001):
    if i%2==0:
        print(i)

for i in range(1,1001):
    if i%2==1:
        print(i)

even=[]
for i in range(1,1001):
    if i%2==0:
        even.append(i)
        
print(even)

odd=[]
for i in range(1,1001):
    if i%2==1:
        odd.append(i)
        
print(odd)
