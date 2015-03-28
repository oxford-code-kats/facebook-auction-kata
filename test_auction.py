import unittest

from auction import bargains, count_deals, generate_products, Product, next_product, strictly_preferred, terrible_deals


class TestAuction(unittest.TestCase):
    def test_not_strictly_preferred_bad_price_good_weight(self):
        product = Product(price=2, weight=1)
        comparison = Product(price=1, weight=2)
        self.assertFalse(strictly_preferred(product, comparison))
    
    def test_not_strictly_preferred_good_price_bad_weight(self):
        product = Product(price=1, weight=2)
        comparison = Product(price=2, weight=1)
        self.assertFalse(strictly_preferred(product, comparison))
    
    def test_strictly_preferred_good_price_equal_weight(self):
        product = Product(price=1, weight=1)
        comparison = Product(price=2, weight=1)
        self.assertTrue(strictly_preferred(product, comparison))

    def test_strictly_preferred_good_weight_equal_price(self):
        product = Product(price=1, weight=1)
        comparison = Product(price=1, weight=2)
        self.assertTrue(strictly_preferred(product, comparison))

    def test_not_strictly_preferred_both_equal(self):
        product = Product(price=1, weight=1)
        self.assertFalse(strictly_preferred(product, product))

    def test_not_strictly_preferred_both_bad(self):
        product = Product(price=2, weight=2)
        comparison = Product(price=1, weight=1)
        self.assertFalse(strictly_preferred(product, comparison))

    def test_bargains(self):
        product = Product(price=1, weight=1)
        products = [product, Product(price=1, weight=2), Product(price=2, weight=1)]
        self.assertEqual(list(bargains(products)), [product])

    def test_terrible_deals(self):
        product = Product(price=2, weight=2)
        products = [product, Product(price=1, weight=2), Product(price=2, weight=1)]
        self.assertEqual(list(terrible_deals(products)), [product])

    def test_next_product(self):
        P1, W1, M, K, A, B, C, D = 1, 4, 5, 7, 1, 0, 1, 2
        product = Product(P1, W1)
        self.assertEqual(
            next_product(product, M, K, A, B, C, D),
            Product(2, 7),
        )

    def test_products(self):
        N, P1, W1, M, K, A, B, C, D = 5, 1, 4, 5, 7, 1, 0, 1, 2
        products = generate_products(N, P1, W1, M, K, A, B, C, D)
        expected = [
            Product(P1, W1),
            Product(2, 7),
            Product(3, 3),
            Product(4, 6),
            Product(5, 2),
        ]
        self.assertEqual(list(products), expected)

    def test_count_deals(self):
        N, P1, W1, M, K, A, B, C, D = 5, 1, 4, 5, 7, 1, 0, 1, 2
        products = generate_products(N, P1, W1, M, K, A, B, C, D)

        self.assertEqual(count_deals(products), (3, 3))

    def test_count_deals_2(self):
        N, P1, W1, M, K, A, B, C, D = 3, 1, 3, 3, 3, 1, 0, 1, 1
        products = generate_products(N, P1, W1, M, K, A, B, C, D)

        self.assertEqual(count_deals(products), (3, 3))

    def test_count_deals_3(self):
        N, P1, W1, M, K, A, B, C, D = 8, 1, 3, 3, 3, 1, 0, 1, 2
        products = generate_products(N, P1, W1, M, K, A, B, C, D)

        self.assertEqual(count_deals(products), (2, 3))

    def test_count_deals_4(self):
        N, P1, W1, M, K, A, B, C, D = 13, 5, 7, 5, 9, 1, 3, 2, 5
        products = generate_products(N, P1, W1, M, K, A, B, C, D)

        self.assertEqual(count_deals(products), (2, 2))

    def test_count_deals_5(self):
        N, P1, W1, M, K, A, B, C, D = 11, 2, 3, 5, 7, 11, 13, 17, 19
        products = generate_products(N, P1, W1, M, K, A, B, C, D)

        self.assertEqual(count_deals(products), (3, 1))
