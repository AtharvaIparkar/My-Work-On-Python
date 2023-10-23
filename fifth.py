def add(a):
    return a**2
print(add(10))

def a(string):
    return len(string)
print("the length of string is : " ,a("ZEAL COLLEGE"))

def atharva(a,b):
    return a-b
print(atharva(20,10))

def sq(a):
    sq=[]
    for i in a:
        sq.append(i**2)
    return sq
a=[1,2,3]
print(sq(a))
print("squares of the list are : ",sq(a))

def a(n1,n2=70):
    print(n1)
    print(n2)
a(30)
a(40,50)
