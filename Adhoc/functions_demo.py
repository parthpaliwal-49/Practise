# def fun_exa():
#     print("You are inside the function")
#
# fun_exa()

# def send_mail(email_address,use_gmail=True):
#     if use_gmail:
#         print("sending mail to {}".format(email_address))
#         return True
#     else:
#         return False
#
# send_mail('parth',False)


# def print_ids(*ids):
#     print(ids[0],ids[1],ids[2])
#
# print_ids(1,2,3)

# def send_mail(**args):
#     if args.get('use_mail'):
#         print("sending mail to {}".format(args.get('email')))
#
# send_mail(email='parth',use_mail=True)
# #
# RETRY = 5
# def send_mail(**args):
#     count = 1
#     while count <= RETRY:
#         print("sending mail to {}".format(args.get('email')))
#         count += 1
#     return True, count, "hii"
#
# return_vals = send_mail(email='parth',use_mail=True)
#
# print(return_vals)

def multiply(*args):
    product = 1
    num = len(args)
    for i in range(num):
        product *= args[i]
    return product

print(multiply(1,2,3,4))
































