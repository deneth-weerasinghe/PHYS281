def productList(list):
    product = 1
    for i in list:
        product *= i
    return product


my_list = [10.3, 100.3, -12.4]
print(productList(my_list))
