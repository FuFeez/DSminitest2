
import sys
import timeit

sys.setrecursionlimit(150000)

print(sys.getrecursionlimit())

testdata = []
import random

from random import randrange
for i in range(500000) :
  a = i
  testdata.append(a)
random.seed(10)
random.shuffle(testdata)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node
        while(current.leftChild is not None):
            current = current.leftChild
        return current

    def delete(self, data):
        if self is None:
            return None
        if data < self.data:
            self.leftChild = self.leftChild.delete(data)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data)
        else:
            if self.leftChild is None:
                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:
                temp = self.leftChild
                self = None
                return temp
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data)
        return self

    def find(self, data):
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ', end = ' ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ',end = ' ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
index = 0
indexofdel = 0
indexofsearch = 0
indexofinsert = 0
def dell():
  global index
  tree.delete(testdata[index])
  index +=1
  return 

def searchbst():
  global indexofsearch
  key = indexofsearch
  tree.find(key)
  indexofsearch +=1
  return 
def bstinserttest():
  global indexofinsert
  global root
  tree.insert(testdata[indexofinsert])
  indexofinsert = indexofinsert + 1 
  return indexofinsert

tree = Tree()
insertbsttime = timeit.repeat(lambda:bstinserttest() ,number=50000,repeat=10)
searchbsttime = timeit.repeat(lambda:searchbst(),number=50000,repeat=10)
deletebsttime= timeit.repeat(lambda:dell(),number=10000,repeat=10)


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
 

class AVL_Tree(object):
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 

        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))
 

        balance = self.getBalance(root)
 

        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 

        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 

        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 

        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 

    def find(self,root,key):
      if (key == root.val):
        return True
      elif (key < root.val):
        if root.left:
          return self.find(root.left,key)
        else:
          return False
      else:
        if root.right:
          return self.find(root.right,key)
        else:
          return False
    
    
    def delete(self, root, key):
 
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        if root is None:
            return root
 
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        balance = self.getBalance(root)
 

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
 
    def preOrder(self, root):
 
        if not root:
            return
 
        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)
 
 

myTree = AVL_Tree()
root = None

indexofdel = 0
indexofsearch = 0
Index_Avl_Insert = 0
def delAvl():
  global indexofdel
  key = index
  myTree.delete(root,key)
  indexofdel +=1
  return index

def searchAvl():
  global indexofsearch
  key = indexofsearch
  myTree.find(root,key)
  indexofsearch +=1
  return index

def insertAvl():
  global Index_Avl_Insert
  global root
  root = myTree.insert(root,testdata[Index_Avl_Insert])
  Index_Avl_Insert = Index_Avl_Insert + 1
  return Index_Avl_Insert



insertavltime = timeit.repeat(lambda:insertAvl(),number=50000,repeat=10)
searchavltime = timeit.repeat(lambda:searchAvl(),number=50000,repeat=10)
deleteavltime = timeit.repeat(lambda:delAvl() ,number=10000,repeat=10)

print(insertavltime,'\n',deleteavltime,'\n',searchavltime,'\n')

import sys

class Node():
    def __init__(self, data):
        self.data = data  
        self.parent = None 
        self.left = None 
        self.right = None 
        self.color = 1 


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def __pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(str(node.data) + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != TNULL:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != TNULL:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(node.data + " ")

    def __search_tree_helper(self, root, key):
      if (key == root.data):
        return True
      elif (key < root.data):
        if root.left:
          return self.__search_tree_helper(root.left,key)
        else:
          return True
      else:
        if root.right:
          return self.__search_tree_helper(root.right,key)
        else:
          return False


    def __fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    # case 3.1
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left 

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print( "Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.__fix_delete(x)
    
    def  __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left 
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right 

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent 
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print( str(node.data) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)
    

    def preorder(self):
        self.__pre_order_helper(self.root)


    def inorder(self):
        self.__in_order_helper(self.root)


    def postorder(self):
        self.__post_order_helper(self.root)


    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node


    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):

        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y


    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1 

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.__fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, data):
        self.__delete_node_helper(self.root, data)

    def pretty_print(self):
        self.__print_helper(self.root, "", True)

rb = RedBlackTree()
Index_Rb_Insert = 0
Index_Rb_Del = 0 
Index_Rb_Search = 0 


def insertrb():
  global Index_Rb_Insert
  global root
  rb.insert(testdata[Index_Rb_Insert])
  Index_Rb_Insert = Index_Rb_Insert + 1
  return Index_Rb_Insert

def delrb():
  global Index_Rb_Del
  key = Index_Rb_Del
  rb.delete_node(key)
  Index_Rb_Del = Index_Rb_Del +1
  return Index_Rb_Del

def searchrb():
  global Index_Rb_Search
  key = Index_Rb_Search
  rb.searchTree(key)
  Index_Rb_Search = Index_Rb_Search + 1
  return Index_Rb_Search



insertrbtime = timeit.repeat(lambda:insertrb(),number=50000,repeat=10)
searchrbtime = timeit.repeat(lambda:searchrb(),number=50000,repeat=10)
deleterbtime = timeit.repeat(lambda:delrb() ,number=10000,repeat=10)

print(insertrbtime,'\n',searchrbtime,'\n',deleterbtime,'\n')

print('INSERT TIME BST :', insertbsttime)
print('INSERT TIME AVL :', insertavltime)
print('INSERT TIME RB  :', insertrbtime)

print('SEARCH TIME BST :', searchbsttime)
print('SEARCH TIME AVL :', searchavltime)
print('SEARCH TIME RB  :', searchrbtime)

print('DELETE TIME BST :', deletebsttime)
print('DELETE TIME AVL :', deleteavltime)
print('DELETE TIME RB  :', deleterbtime)

import matplotlib
import matplotlib.pyplot as plt

x = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
y1 = insertbsttime
y2 = insertavltime
y3 = insertrbtime
plt.figure(figsize=(7.195, 3.841), dpi=100)
plt.plot(x,y1,marker= 'p',ms=5.5,label='BST',color='#81A684')
plt.plot(x,y2,marker= 'p',ms=5.5,label='AVL',color='#84BAC9')
plt.plot(x,y3,marker= 'p',ms=5.5,label='REDBLACK',color='#D28BB5')
plt.xlabel('ordinal number',color = '#2e6173')
plt.ylabel('second', color = '#2e6173')
plt.title('INSERT \n COMPARE WITH BST , AVL , REDBLACK' , color= '#2e6173')
plt.tick_params(colors='#2e6173', which='both')
plt.legend(loc='best',labelcolor='#2e6173')
plt.grid(axis='y',color='#808080')
plt.savefig('insertgraph.png',transparent=True,dpi = 1000 )
plt.show()


x = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
y1 = searchbsttime
y2 = searchavltime
y3 = searchrbtime
plt.figure(figsize=(7.195, 3.841), dpi=100)
plt.plot(x,y1,marker= 'p',ms=5.5,label='BST',color='#81A684')
plt.plot(x,y2,marker= 'p',ms=5.5,label='AVL',color='#84BAC9')
plt.plot(x,y3,marker= 'p',ms=5.5,label='REDBLACK',color='#D28BB5')
plt.xlabel('ordinal number',color = '#2e6173')
plt.ylabel('second', color = '#2e6173')
plt.title('SEARCH \n COMPARE WITH BST , AVL , REDBLACK' , color= '#2e6173')
plt.tick_params(colors='#2e6173', which='both')
plt.legend(loc='best',labelcolor='#2e6173')
plt.grid(axis='y',color='#808080')
plt.savefig('searchgraph.png',transparent=True,dpi = 1000 )

plt.show()

x = ['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th']
y1 = deletebsttime
y2 = deleteavltime
y3 = deleterbtime
plt.figure(figsize=(7.195, 3.841), dpi=100)
plt.plot(x,y1,marker= 'p',ms=5.5,label='BST',color='#81A684')
plt.plot(x,y2,marker= 'p',ms=5.5,label='AVL',color='#84BAC9')
plt.plot(x,y3,marker= 'p',ms=5.5,label='REDBLACK',color='#D28BB5')
plt.xlabel('ordinal number',color = '#2e6173')
plt.ylabel('second', color = '#2e6173')
plt.title('DELETE \n COMPARE WITH BST , AVL , REDBLACK' , color= '#2e6173')
plt.tick_params(colors='#2e6173', which='both')
plt.legend(loc='best',labelcolor='#2e6173')
plt.grid(axis='y',color='#808080')
plt.savefig('deletegraph.png',transparent=True,dpi = 1000 )
plt.show()