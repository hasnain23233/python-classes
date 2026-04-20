# in this class we learn about Dictionaries and sets

# Dictionaries

student = {
    "name" : "Fahad",
    "email": "fahad@gmail.com",
    "phone": 4934,
    "city": "Gilgit"
}


print(student)
print(student["name"])
print(student["email"])
print(student["phone"])
print(student["city"])

student["name"] = "Hasnain"

print(student.pop("city"))
print(student)


# sets

num = {1 , 2 ,3 , 4 ,5 ,6 , 7}
print(num)
num.add(8)
print(num)