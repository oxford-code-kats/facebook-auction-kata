from collections import Counter, namedtuple
from functools import partial


Product = namedtuple('Product', ('price', 'weight'))


def strictly_preferred(product, other):
    if product.price < other.price and product.weight <= other.weight:
        return True
    elif product.weight < other.weight and product.price <= other.price:
        return True
    return False


def bargain(product, other):
    return not strictly_preferred(other, product)


def terrible_deal(product, other):
    return not strictly_preferred(product, other)


def filter_products(products, filter):
    for product in products:
        if all(filter(product, other) for other in products):
            yield product


bargains = partial(filter_products, filter=bargain)
terrible_deals = partial(filter_products, filter=terrible_deal)


def next_product(product, M, K, A, B, C, D):
    price = (A * product.price + B) % M + 1
    weight = (C * product.weight + D) % K + 1
    return Product(price, weight)


def generate_products(N, price, weight, *args):
    product = Product(price, weight)
    yield product

    for i in range(1, N):
        product = next_product(product, *args)
        yield product


def count(deals, products):
    return sum(products[deal] for deal in deals)


def count_deals(products):
    products = Counter(products)
    return (
        count(terrible_deals(products), products),
        count(bargains(products), products),
    )
