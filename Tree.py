class node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class Tree:
    def __init__(self):
        self.Root = None
        self.Parent = 0
        self.Leaf = 0
        self.All = 0

    def Insert(self, No):

        newn = node(No)

        if self.Root == None:
            self.Root = newn

        else:
            temp = self.Root

            while True:
                if temp.data == No:
                    print("Unable to insert the node as element is already present")
                    break

                elif No > temp.data:
                    if temp.rchild == None:
                        temp.rchild = newn
                        break
                
                    temp = temp.rchild

                else:
                    if temp.lchild == None:
                        temp.lchild = newn
                        break

                    temp = temp.lchild

    def Inorder(self):
        return self.InTraverse(self.Root)
    

    def InTraverse(self,root):
       
        if root != None:
            self.InTraverse(root.lchild)
            print(root.data, end="\t")
            self.InTraverse(root.rchild)

    def Postorder(self):
        return self.PTraverse(self.Root)
    
    def PTraverse(self,root):
        
        if root != None:
            
            self.PTraverse(root.lchild)
            self.PTraverse(root.rchild)
            print(root.data, end="\t")

    def Preorder(self):
        return self.PreTraverse(self.Root)
    
    def PreTraverse(self,root):
        
        if root != None:
            
            print(root.data, end="\t") 
            self.PreTraverse(root.lchild)
            self.PreTraverse(root.rchild)
            

    def CountLeaf(self):
        return self.CountL(self.Root)
    
    def CountL(self, root):

        if root != None:

            if root.lchild == None and root.rchild == None:
                self.Leaf = self.Leaf + 1

            self.CountL(root.rchild)
            self.CountL(root.lchild)

        return self.Leaf

    def CountParent(self):
        return self.CountP(self.Root)
    
    def CountP(self, root):

        if root != None:

            if root.lchild != None and root.rchild != None:
                self.Parent = self.Parent + 1

            self.CountP(root.rchild)
            self.CountP(root.lchild)

        return self.Parent
    
    def CountAll(self):
        return self.CountA(self.Root)
    
    def CountA(self, root):

        if root != None:

            self.All = self.All + 1
            self.CountA(root.rchild)
            self.CountA(root.lchild)

        return self.All
    
    def Search(self, iValue):

        bFlag = False

        if self.Root == None:
            print("Tree is empty")
        
        while self.Root != None:

            if self.Root.data == iValue:
                bFlag = True
                break

            elif iValue > self.Root.data:
                self.Root = self.Root.rchild

            elif iValue < self.Root.data:
                self.Root = self.Root.lchild

        if bFlag == True:
            print(iValue," Found")

        else:
            print(iValue," Not Found")


obj = Tree()

obj.Insert(121)
obj.Insert(151)
obj.Insert(11)
obj.Insert(21)
obj.Insert(101)
obj.Insert(51)


print("Inorder is: ")
obj.Inorder()
print()
print("Postorder is: ")
obj.Postorder()
print()
print("Preorder is: ")
obj.Preorder()

iLeaf = obj.CountLeaf()
print("\nNumber of leaf nodes are: ", iLeaf)

iParent = obj.CountParent()
print("\nNumber of parent nodes are: ", iParent)

iAll = obj.CountAll()
print("\nTotal number of nodes are: ", iAll)

obj.Search(161)