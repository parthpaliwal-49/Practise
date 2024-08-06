import csv

file_path = 'product_data.csv'


def read_csv(file_path):
    file = open(file_path, encoding='utf-8')
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print('Product Name : {}, QTY : {}'.format(row[0], row[-1]))
        # print(type(row))
    file.close()


read_csv(file_path)


# def read_csvEx(file_path):
#     file = open(file_path, encoding='utf-8')
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print('Product Name : {}, QTY : {}'.format(row.get('ProductName'), row.get('Quantity')))
#         # print(type(row))
#     file.close()
#
#
# read_csvEx(file_path)


# write_file_path = 'write_file_demo.csv'
# def write_csv(write_file_path):
#     file = open(write_file_path,'w', encoding='utf-8', newline='')
#     fields = ['id','name','email']
#     csv_writer = csv.DictWriter(file, fieldnames=fields)
#     csv_writer.writeheader()
#
#     row = {
#         'id':1,
#         'name':'Parth',
#         'email':'parth@gmail',
#         'email2': 'parth@gmail'
#     }
#
#     csv_writer.writerow(row)
#     file.close()
#
#
# write_csv(write_file_path)


file_path = 'product_data.csv'














