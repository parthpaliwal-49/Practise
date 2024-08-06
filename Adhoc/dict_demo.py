# emp1 = {}
# emp2 = dict()
# print(type(emp1),"\n",type(emp2))

# A key for dictionary must be immutable or hashable
# create hash , derive memory address and store value
emp1 = {
    "name":"parth",
    "dept":"BI",
    "id":41
}
# print(emp1)

employees = {
    "BI":['Parth','Naveen'],
    "Arch":['Abhishek','Shrikant']
}

# print(employees)
#
# print(emp1['name'])
#
# print(employees['BI'][1])

# print(employees.keys())

# print(employees.values())

# print(employees.get('SE'))
# # .get returns None if key does not exist istead of giving key error.
#
# print(employees.get('BI'))

# print(employees.get('SE', "dept does not exist"))
# # you can give another value for None by simply giving the default value in parameter of .get().

# print(employees.items())
# # .items() is used to give both key and values.

# # Adding new elements to Dictionary
# employees["SE"] = ["Sagar","Tushar"]
# print(employees)

# # Updating the values in dictionary
# employees['SE'][1] = "Digvijay"
# print(employees)

a = dict(a=1, b=2, c=3)
print(a)














