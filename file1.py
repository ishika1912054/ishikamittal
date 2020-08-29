# string-input a string and assign it to a variable

a = str(input("enter the string"))
b = "world"
print(a)
print(b)
print("---------------------------------------------")

# string-string are array

a = "world"
print(a[2])
print("----------------------------------------------")

# string-check if a phase is in string or not

a = "hello world , this is basic python programming"
x = "thon" in a
print(x)
print("-----------------------------------------------")

# string-concatenation

a = "hello"
b = "world"
c = a + b
print(c)
print(a * 3)
print(a + b + str(3))  # to add an integer to string
print("--------------------------------------------------")

# string-formatting

name = "john"
print("my name is %s !" % name)
print("my name is {} !".format("lily"))
txt = "we have {:<8} pencil"
print(txt.format(49))
txt = "we have {:>8} pencil"
print(txt.format(49))
txt = "we have {:^8} pencil"
print(txt.format(49))
print(name[0:3])
print("--------------------------------------------------")

# string-built-in methods

st = "hello world "
print(st.lower())  # converts to lower case
print(st.upper())  # converts to upper case
print(st.capitalize())  # capitalize the string
print(st.count("l"))  # counts no. of 'l' in the string
print(st.count("hello"))  # counts no. of "hello" in string
print(st.find("l"))  # returns true if 'l' is present in the string
print(st.find("z"))  # returns false if 'z' is present in the string
print(st.islower())  # checks if the string is in lower case or not
print(st.isupper())  # checks if string is in upper case or not
st.replace("hello", "hi")  # replace every occurance of "hello" with "hi"
print(st)
print(st.startwith("h"))  # tells if the string start with 'h' or not

st1 = "12345ft"
print(st1.isalpha())  # charcks if string is alphabetic or not
print(st1.isdigit())  # checks if the strong is in digit or not
print(st1.isalnum())  # checks if string is both alphabetic and digit
print(''.join(reversed(st1)))  # reversing of string function
