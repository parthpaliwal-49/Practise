num = input("please enter number in comma seperated fashion: ")
num_lst = num.split(',')
lst = list()
for num in num_lst:
	if num.isdigit():
		lst.append(int(num))

print(lst)
tpl = tuple(lst)
print(tpl)
