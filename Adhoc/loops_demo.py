num_list = [10,20,30,40,50,60,70,80,90]
# for i in num_list:
#     print(i)


# sum = 0
# for i in num_list:
#     sum += i
# print(sum)

# # range(start_index,end_index,step)
# print(range(10))
# print(list(range(10)))
# print(list(range(3,10)))
# print(list(range(2,10,2)))

# for i in range(len(num_list)):
#     print(num_list[i])

# list2 = []
# for i in range(1,21):
#     list2.append(i)
#
# print(list2)

# # Break
# for i in range(1,10):
#     if i==5:
#         print("Ending the loop")
#         break
#     print(i)

# # Continue
# for i in range(1,10):
#     if i==5:
#         print("skipping 5 in the loop")
#         continue
#     print(i)

for i in range(1,11):
    for j in range(1,11):
        print("{} * {} = {}".format(i,j,i*j))
    print()






