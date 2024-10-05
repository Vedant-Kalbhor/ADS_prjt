from collections import defaultdict
class TreeNode:
    def __init__(self, laptop):
        self.laptop = laptop
        self.left = None
        self.right = None
        self.height = 1  # New nodes are initially at height 1

class LaptopAVL:
    def __init__(self):
        self.root = None

    def insert(self, laptop):
        if self.root is None:
            self.root = TreeNode(laptop)
        else:
            self.root = self._insert_recursive(self.root, laptop)

    def _insert_recursive(self, node, laptop):
        # Standard BST insertion
        if laptop.price < node.laptop.price:
            if node.left is None:
                node.left = TreeNode(laptop)
            else:
                node.left = self._insert_recursive(node.left, laptop)
        else:
            if node.right is None:
                node.right = TreeNode(laptop)
            else:
                node.right = self._insert_recursive(node.right, laptop)

        # Update the height of the node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Get the balance factor to check if this node became unbalanced
        balance = self._get_balance(node)

        # Left Left Case (Right Rotation)
        if balance > 1 and laptop.price < node.left.laptop.price:
            return self._right_rotate(node)

        # Right Right Case (Left Rotation)
        if balance < -1 and laptop.price > node.right.laptop.price:
            return self._left_rotate(node)

        # Left Right Case (Left-Right Rotation)
        if balance > 1 and laptop.price > node.left.laptop.price:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case (Right-Left Rotation)
        if balance < -1 and laptop.price < node.right.laptop.price:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return the new root
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

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
