# in this class we learn about loops in python

# while loop
# num = -4

# while num <= 5:
#     print("Num is smaller the " , num)
#     num += 1

# #for loop
# for i in range(1 , 5):
#     # print(i , "This is a number of i")

# for i in range(1, 10):
#     if i == 5:
#         break
#     # print(i)

for i in range(1 , 10):
    if i == 3:
        print("The loop comes in 3")
        continue
    if i > 5:
        print("The loop is break here")
        break
    print(i)

for i in range(10):
    print(i)