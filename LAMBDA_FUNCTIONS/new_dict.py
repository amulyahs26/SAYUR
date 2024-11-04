#Dictionary Transformation Using Lambda
# Given a dictionary:products = {'apple': 2.5, 'banana': 1.0, 'orange': 3.0}
# Use dictionary comprehension and a lambda function to create a new dictionary where the
# prices are increased by 10%.

products = {'apple': 2.5, 'banana': 1.0, 'orange': 3.0}
new_products = {item: (lambda price: round(price * 1.1,2))(price) for item, price in products.items()}
print(new_products)

