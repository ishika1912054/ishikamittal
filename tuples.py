# tuples

tup=("jan","feb","march","april","may","june");           #accessing tuple element
print(tup[2])
print("--------------------------------------------")

tup1=(1,2,3);                                             #comparing tuples
tup2=(4,5,6);
if(tup1>tup2):
    print("tup1 is bigger")
else:
    print("tup2 is bigger")
print("---------------------------------------------")    

tup3=tup1+tup2                                            #updating tuples
print(tup3)
print("---------------------------------------------")

del tup3                                                  #deleting tuple

print(len(tup))                                           #tuple built-in function
print(tup1*3)
print(tup[-2])                                            #slicing of tuple
print(tup[1:5])
for x in tup2:                                            #for function on tuple
    print(x)
