class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print (p1.name)
print (p2.name)
print (Person.name)

class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print (p1.name)
print (p2.name)
print (Person.name)