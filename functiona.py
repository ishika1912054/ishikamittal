# creating functions

def my_function():  # declaring the function
    print("hello from my function")
 
my_function()  # calling the function
print("-----------------------------------------------------")


def fact(n):  # function with arguement
    ans = 1
    for i in range(1, n + 1):  # for loop
        ans = ans * i
    print(ans)
print("-----------------------------------------------------")


a = int(input("enter the number to calculate the factorial"))
print("answer :-")
fact(a)
print("-----------------------------------------------------")


def num(n):

    return n*5                              #function returning a value
print("------------------------------------------------------")


p = int(input("enter number"))
q=num(p)
print(q)
print("task done")
print("------------------------------------------------------")



#to find wether a number is prime or not using break statement

n=int(input("enter number"))
i=2
count=0
while (i<n):
    if( n%i==0):
        count=count+1
        print("not a prime number")
        break                                 #break ststement
    i=i+1
if(count==0):
    print("prime number")

print("------------------------------------------------------")    

#continue statement - laeve 3 in the loop

i=0
while i<6:
    i=i+1
    if i==3:
        continue
    print(i)

