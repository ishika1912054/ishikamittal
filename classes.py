# classes

class organization:                     #creating the class
    x='employee deatils'
    def __init__(employee,name,age):
        employee.name=name
        employee.age=age
    def myname(person):
        print("name="+person.name)
        print("age=%d"%person.age)

p=organization("ramesh",40)             #creating its object
p.myname()
print("---------------------------------------------")

p.age=51                                 #modifying the value
p.myname()
print("----------------------------------------------")

del p                                    #deleting the object

class employee(organization):            #inheriting a class
    pass                                 #pass is used when you dont want to modify the parent class
x=employee("mike",45)
x.myname()
#otherwise we can use init function to modify the child class
