# Write your solution here

def search(products: list, criterion: callable):
    lst = []
    for product in products:
        if criterion(product):
            lst.append(product)
    return lst

#OFFICIAL SOLUTION:
# def search(products: list, criterion: callable):
#     return [product for product in products if criterion(product)]