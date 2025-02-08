class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Balanced_BST:
    def __init__(self):
        self.root: TreeNode = None
        self.size = 0

    def pre_traverse(self, root: TreeNode):
        if not root:
            return
        print(root.val, end= " ")
        self.pre_traverse(root.left)
        self.pre_traverse(root.right)
        
    def in_traverse(self, root: TreeNode):
        if not root:
            return
        self.in_traverse(root.left)
        print(root.val, end= " ")
        self.in_traverse(root.right)
        
    def post_traverse(self, root: TreeNode):
        if not root:
            return
        self.post_traverse(root.left)
        self.post_traverse(root.right)
        print(root.val, end= " ")
        
    def insert(self, root: TreeNode, val):
        if not self.root:
            self.root = TreeNode(val)
            self.size += 1
            return self.root
        if not root:
            self.size += 1
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        bf = self.getBF(root)
        if bf > 1 and self.getBF(root.left) >= 1: # LL
            return self.__rightRotate(root)
        if bf > 1 and self.getBF(root.left) <= -1: #LR
            root.left = self.__leftRotate(root.left)
            return self.__rightRotate(root)
        if bf < -1 and self.getBF(root.right) <= -1: #RR
            return self.__leftRotate(root)
        if bf < -1 and self.getBF(root.right) >= 1: #RL
            root.right = self.__rightRotate(root.right)
            return self.__leftRotate(root)
        return root
    
    
    def remove(self, root: TreeNode, val):
        if not root:
            return
        if val < root.val:
            root.left = self.remove(root.left, val)
        elif val > root.val:
            root.right = self.remove(root.right, val)
        else:
            if not self.root.left and not self.root.right:
                self.size = 0
                self.root = None
                return self.root
            if root != self.root and not root.left:
                self.size -= 1
                return root.right
            if root != self.root and not root.right:
                self.size -= 1
                return root.left
            predecessor = self.getPredecessor(root, val)
            root.val = predecessor.val
            root.left = self.remove(root.left, predecessor.val)
        
        bf = self.getBF(root)
        if bf < -1 and self.getBF(root.right) <= 0: ##RR
            return  self.__leftRotate(root)
        if bf < -1 and self.getBF(root.right) > 0: #RL
            root.right = self.__rightRotate(root.right)
            return self.__leftRotate(root)
        if bf > 1 and self.getBF(root.left) >= 0: ##LL
            return self.__rightRotate(root)
        if bf > 1 and self.getBF(root.left) < 0: #LR
            root.left = self.__leftRotate(root.left)
            return self.__rightRotate(root)     
        return root
    
    def getSuccessor(self, root: TreeNode, val):
        if not root:
            return None
        tmp = root
        successor = None
        while val != tmp.val:
            if val < tmp.val:
                successor = tmp
                tmp = tmp.left
            else:
                tmp = tmp.right
        if tmp.right:
            return self.getMin(tmp.right)
        else:
            return successor
        
    def getPredecessor(self, root: TreeNode, val):
        if not root:
            return None
        tmp = root
        predecessor = None
        while tmp.val != val:
            if val < tmp.val:
                tmp = tmp.left
            else:
                predecessor = tmp
                tmp = tmp.right
        if tmp.left:
            return self.getMax(tmp.left)
        else:
            return predecessor
    
    def getMin(self, root: TreeNode):
        if not root:
            return None
        tmp = root
        while tmp.left:
            tmp = tmp.left 
        
        return tmp
    
    def getMax(self, root: TreeNode):
        if not root:
            return None
        tmp = root
        while tmp.right:
            tmp = tmp.right
            
        return tmp
            
    def search(self, val)->bool:
        tmp = self.root
        while tmp:
            if val < tmp.val:
                tmp = tmp.left
            elif val > tmp.val:
                tmp = tmp.right
            else: 
                return True
        return False
    
    def getHeight(self, node: TreeNode):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1
    
    def getBF(self, node: TreeNode):
        if node == None:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def __leftRotate(self, node: TreeNode):
        mid = node.right
        T = mid.left
        mid.left = node
        node.right = T
        if node == self.root:
            self.root = mid
        return mid

    def __rightRotate(self, node: TreeNode):
        mid = node.left
        T = mid.right
        mid.right = node
        node.left = T
        if node == self.root:
            self.root = mid
        return mid
    
    def is_empty(self):
        return self.size == 0

tree = Balanced_BST()
tree.insert(tree.root, 2)
tree.insert(tree.root, 1)
tree.insert(tree.root, 4)
tree.insert(tree.root, 3)
tree.insert(tree.root, 5)
tree.insert(tree.root, 7)
tree.remove(tree.root, 7)
tree.remove(tree.root, 5)
tree.remove(tree.root, 1)
tree.remove(tree.root, 2)
tree.remove(tree.root, 4)
tree.remove(tree.root, 3)
print(tree.search(5))
print("post_traverse", end = ": ")
tree.post_traverse(tree.root)
print()
print(tree.getBF(tree.root))
print(tree.is_empty())
print(tree.size)

        


        
        

        
    