# python dictionary

dict={'charlie':18,'tim':12,'tiffany':22,'robert':25}
print(dict['tiffany'])                                     #accessing dictionary elements
print("-----------------------------------------------")

boys={'rohan':5,'raghav':7,'madhav':11,'aditya':13}
girls={'mahi':4,'palak':7,'rashi':9,'avni':15}
studentx=boys.copy()                                       #copy a dictionary
studenty=girls.copy()
print(studentx)
print(studenty)
print("-----------------------------------------------")

dict.update({'renesa':21})                                 #update a dictionary
print(dict)
print("-----------------------------------------------")

del dict['tim']                                            #deleting a deictionary item
print(dict)
print("-----------------------------------------------")

print("student name %s"%dict.items())
print("student name %s"%list(dict.items()))
print("-----------------------------------------------")

print("length=%d"%len(dict))                               #built-in functions
print("variable type=%s"%type(dict))
print(str(dict))
print(dict.values())
