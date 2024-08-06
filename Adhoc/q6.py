import math
num_lst = input("Please enter the numbers in comma seprated values : ")
num_lst = num_lst.split(",")
result_lst = list()
for i in num_lst:
	if i.isdigit():
		Q = math.sqrt((2*50*int(i))/30)
		result_lst.append(Q)

print(result_lst)
