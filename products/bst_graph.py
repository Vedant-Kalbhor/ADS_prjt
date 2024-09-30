from collections import defaultdict
class TreeNode:
    def __init__(self, laptop):
        self.laptop = laptop
        self.left = None
        self.right = None

class LaptopBST:
    def __init__(self):
        self.root = None

    def insert(self, laptop):
        if self.root is None:
            self.root = TreeNode(laptop)
        else:
            self._insert_recursive(self.root, laptop)

    def _insert_recursive(self, node, laptop):
        if laptop.price < node.laptop.price:
            if node.left is None:
                node.left = TreeNode(laptop)
            else:
                self._insert_recursive(node.left, laptop)
        else:
            if node.right is None:
                node.right = TreeNode(laptop)
            else:
                self._insert_recursive(node.right, laptop)

    # Searching laptops within a price range
    def search_by_price_range(self, min_price, max_price):
        return self._search_recursive(self.root, min_price, max_price)

    def _search_recursive(self, node, min_price, max_price):
        if node is None:
            return []
        
        laptops_in_range = []
        if min_price <= node.laptop.price <= max_price:
            laptops_in_range.append(node.laptop)
        
        if min_price < node.laptop.price:
            laptops_in_range += self._search_recursive(node.left, min_price, max_price)
        
        if max_price > node.laptop.price:
            laptops_in_range += self._search_recursive(node.right, max_price, max_price)
        
        return laptops_in_range
    



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
