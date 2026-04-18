str1 = 'Python is a easy programming'
str2 = "Hasnain" 
str3 = '''This is a python course'''

print(str1)
print(str2)
print(str3)

print(str1 + str2)

print(len(str2 + str3))

# indexing
print(str1[0])
print(str2[1])
print(str3[2])


# userInput1 = input("Enter your first name :) ")
# userInput2 = input("Enter your last name :) ")

# print("The total lenght of the you first name and last is : " , userInput1 + " " + userInput2 , " is " , len(userInput1 + userInput2))


# sliceing in python

userData = "hasnain"
Job = "Web development"


print(userData[1: 5])
print(userData[ : 7])

print(userData[2:])

print(userData.upper())
print(userData.lower())
print(userData.title())
print(userData.replace("hasnain" , "developer"))
print(userData)
print(userData.count("n"))