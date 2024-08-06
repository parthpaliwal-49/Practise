import csv
file_path = 'product_data.csv'


# def read_csv(file_path):
#     file = open(file_path, encoding='utf-8')
#     csv_reader = csv.DictReader(file)
#     category = {}
#     for row in csv_reader:
#         print('Category : {}'.format(row.get('Category')))
#         cat = row.get('Category')
#         if cat not in category:
#             category[cat] = 1
#         else:
#             category[cat] += 1
#     file.close()
#     return category
#
# print(read_csv(file_path))

def read_csv(file_path):
    with open(file_path, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        category_products = {}
        for row in csv_reader:
            c_name = row.get('Category')
            p_name = row.get('ProductName')

            if c_name not in category_products:
                category_products[c_name] = set()

            category_products[c_name].add(p_name)

    return category_products

category_products = read_csv(file_path)

for category, products_set in category_products.items():
    print(f"Category: {category} \n Unique Products Count: {len(products_set)}"'\n')
