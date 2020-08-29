# arrays

flowers = ['tulip', 'lily', 'daisy', 'pancy', 'rose', 'hibiscus', 'lotus']
print(flowers[1])  # accessing array elements

print("------------------------------------------------")

print(len(flowers))  # length of array
print("------------------------------------------------")
for x in flowers:  # looping an array
    print(x)
print("-------------------------------------------------")    

flowers.append('sunflower')  # adding elements in array
print(flowers)
print("-----------------------------------------------")

flowers.pop(6)
print(flowers)
print("------------------------------------------------")


# python program to search an element

def search(arr, n):
    i = 0
    while (i < len(arr)):
        if (arr[i] == n):
            return True
        i = i + 1
    return False


a = 'lily'
if search(flowers,a):
    print("found")
else:
    print("not found")

