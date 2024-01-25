# conversion.py
a=1,2,3,4,4,4,5,6,6
print(list(a))
print(set(a))
print(tuple(a))

#defining a frozen set-({})
a=frozenset(["1","33","666","apple","banana","cherry"])
print(a)
print("apple" in a)
print("banana" not in a)

a=frozenset([1,2,3,4,5,6])
b=frozenset([4,5,6,7,8,9])
# Union
print(a|b) #output: frozenset({1, 2, 3, 4, 5, 6, 7, 8, 9})

#intersection
print(a&b) #output: frozenset({4, 5, 6})

#difference
print(a-b) #output: frozenset({1, 2, 3})


dict=("brand": "manindra", "model": "thar", "year":"2023"}
print(dict["brand"])

#overwriting of dictionary 
a=("brand": "mahindra", "model" "than", "year":"2023"}
a={"brand": "force", "model": "gurkha", "year":"1984"}
print(dict["year"])

#print keys & values diffrently
a={"brand":"mahindra", "model": "thar" "year":"2023"}
x=dict.keys(a)
y=dict.values(a)
print (x)
print(y)

a={"name":"Pratik","age":"18","roll.no.":"2019"}
print(type(a))

for x in a:
    print(x)

for x,y in a.items():
    print(x,y)
   
car={"brand":"ford","model":"mustang","year":"1964"}
x=car.items()
print(x)

# for addinon of keys
car["type"]="muscle car"
print(x)

# to access keys from dictionary
if "brand" in car:
    print("YES")
else:
    print("NO")

#for updation in  keys
car["year"]="2012"
print(car)
 
 # create a dictionary within a dictionary (nested dictionary)
city={
    "mumbai":{
        "state":"maharashtra",
        "known as":"city of dreams"
        },
    "kolkata":{
        "state":"west bengal",
        "known as":"city of joy"
        },
    "banglore":{
        "state":"karnataka",
        "known as":"IT hub"
        }
    }
print(city)

myfamily={
    "child1":{
        "name":"pratik",
        "year":"2025"
        },
    "child2":{
        "name":"sarthak",
        "year":"2028"
        },
    "child3":{
        "name":"anuj",
        "year":"2030"
        }
}
print(myfamily)
   
# crating a dictionary by taking input from the user 
dict={}
while True:
    a=input("enter the key: ")
    b=input("enter the value: ")
    dict[a]=b    #format: dict[key]=value
    other=input("do you want to enter more another pair?")
    if other!="yes":      # (!=):stands for not equal to
        break
print(dict)
       
   
