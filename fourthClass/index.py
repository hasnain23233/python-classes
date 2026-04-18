# In here we lean about the condition list and tuple


#conditions

# user = int(input("Enter your age :) "))

# if user >= 18:
#     print("Now you can start driving")
# elif user == 17:
#     print("Now you wait one year than you start driving")
# else:
#     print("Sorry you can`t drive the car")


# list means Array
number = [1 , 2 ,3 ,4 , 5 ,6]
print(number[3])
updateValue = number[3] = 5
print(updateValue)

number.append(20)
print(number)
number.remove(2)
print(number)
number.pop()
print(number)
number.sort()
print(number)
number.sort(reverse=True)
print(number)
print(len(number))
number.reverse()
print(number)

print(number.index(5))



# loop
for num in number:
    print(f"{num} is the index in loop {number}")


# mixdata

data = ["Hasnain" , 23 , True]
print(data)