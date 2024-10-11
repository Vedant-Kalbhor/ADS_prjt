class AVLNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, product):
        if not root:
            return AVLNode(product)

        # Insert based on price
        if product.price < root.product.price:
            root.left = self.insert(root.left, product)
        else:
            root.right = self.insert(root.right, product)

        # Update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance the tree
        return self.balance_tree(root, product)

    def balance_tree(self, root, product):
        balance = self.get_balance(root)

        if balance > 1 and product.price < root.left.product.price:
            return self.right_rotate(root)
        if balance < -1 and product.price > root.right.product.price:
            return self.left_rotate(root)
        if balance > 1 and product.price > root.left.product.price:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and product.price < root.right.product.price:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, z):
        y = z.right
        z.right = y.left
        y.left = z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def right_rotate(self, z):
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def search_by_price(self, root, min_price, max_price, result=[]):
        if not root:
            return result

        # In-order traversal to get products in the price range
        if root.product.price >= min_price:
            self.search_by_price(root.left, min_price, max_price, result)
        
        if min_price <= root.product.price <= max_price:
            result.append(root.product)
        
        if root.product.price <= max_price:
            self.search_by_price(root.right, min_price, max_price, result)

        return result

# Utility function to search products with price range
def search_products_by_price(root, min_price, max_price):
    avl_tree = AVLTree()
    return avl_tree.search_by_price(root, min_price, max_price)

class LaptopGraph:
    def __init__(self):
        # A dictionary where each brand/type points to a list of laptops (nodes)
        self.graph = defaultdict(list)

    def add_laptop(self, laptop):
        # Add a laptop to the graph based on its brand and type
        self.graph[(laptop.brand, laptop.laptop_type)].append(laptop)

    def get_related_laptops(self, laptop):
        # Get all laptops that are related by brand and type
        return self.graph.get((laptop.brand, laptop.laptop_type), [])
