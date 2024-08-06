# # Convert two lists into a dictionary
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# new_dict = {}
# for i in range(len(keys)):
#     new_dict[keys[i]] = values[i]

# print(new_dict)


# # Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# result = dict1.copy()

# for key,value in dict2.items():
#     result[key] = value

# print(result)

# # second solution
# dict3 = dict1.copy()
# dict3.update(dict2)


# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])

# # Making dictionary from a default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# res = dict.fromkeys(employees, defaults)
# print(res)

# # Individual data
# print(res["Kelly"])



















