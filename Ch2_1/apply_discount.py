"""Chapter 2.1 Assert in Python - An Example"""

shoes = {'name': 'Fancy Shoes', 'price': 14900}

def apply_discount(product, discount):
    """assert statement to ensure 'price' is not less than zero
    and not more the 'cost' of the product
    """
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

# dummy code for figurative demonstration:
def is_admin(user):
    """check if user is an admin"""
    return True

def has_product(prod_id):
    """check if prod_id exists"""
    return True

def get_product(prod_id):
    """retrieve product, prod_id"""
    return prod_id

def delete(prod_id):
    return 'Product Deleted'

# this function uses asserts to validate privileges & product id:
def delete_product(prod_id, user):
    """using assert to validate user & prod_id.
    a problem if asserts are diabled at run-time.
    """
    assert user.is_admin(), 'Must be admin'
    assert store.has_product(prod_id), 'Unknown product'
    store.get_product(prod_id).delete()

# one correct way to deal with this kind of case:
def delete_product(product_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(product_id):
        raise ValueError('Unknown product id')
    store.get_product(product_id).delete()
