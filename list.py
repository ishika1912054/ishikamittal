#list- declaration and access its items

mylist=["square","cube","circle"]
print(mylist[2])
print(mylist[-2])
print("--------------------------------------------")

#list- range of indexes

mylist=["square","cube","circle"]
print(mylist[1:])
print(mylist[-3:-1])
print("---------------------------------------------")

#list- change the item

mylist=["square","cube","circle"]
mylist[2]="rectangle"
print(mylist)
print("----------------------------------------------")

#list- length
mylist=["square","cube","circle"]
print(len(mylist))
print("----------------------------------------------")

#list- add items

mylist=["square","cube","circle"]
mylist.insert(1,"circle")
print(mylist)
print("------------------------------------------------")

#list- remove an items

mylist=["square","cube","circle"]
mylist.pop(2)
print(mylist)
print("--------------------------------------------------")

#list- clear a list

mylist=["square","cube","circle"]
mylist.clear()
print(mylist)
print("--------------------------------------------------")

#list- copy a list

mylist=["square","cube","circle"]
list=mylist.copy()
print(list)
print("----------------------------------------------------")

#list- add two list

list1=["square","cube","circle"]
list2=["rectangle","parallelogram","rhombus"]
list3=list1+list2
print(list3)
print("----------------------------------------------------")

