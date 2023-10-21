print("HELLO PYTHON")


list_=["Rahul","Atharva","Pratik","Sarthak","Minal"]
print(list_)
print(type(list_))
print(list_[1:4])
if "Pratik" in list_:
    print("available")
        

a=[1,2,3,4,5]
a[2]=10
print(a)

n = int(input("Enter any number"))
if n%2==0:
    if n>1 and n<6:
        print("not weird")
    elif n>5 and n<21:
        print("weird")
    elif n>=20:
        print("not weird")
else:
    print("weird")
    
    
a=["rahul","sandip","pratik","atharva","atul"]
a.append("jayesh")
a.insert(3,"tanmay")
a.remove("rahul")
a.reverse()
b=a.copy()
print(a)

set1={1,2,3,True,"True",False}
set2={"hello","pratik",1,5,6}
set1.update(set2)
set1.remove(2)
set1.discard(2)
print(set1)

