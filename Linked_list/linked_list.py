#creating a object node
class Node:
    #node has two attributes value and Reference 
    def __init__(self,value,ref = None):
        self.value = value
        self.ref = ref
    #This method will link two nodes 
    def link(self,Node):
        self.ref = Node
    #This traverrs the whole list with while loop
    def traverse(self):
        while True:
            print(self.value,'->')
            if self.ref is None:
                print('Null')
                break
            self = self.ref
node1 = Node(10)
node2 = Node(20)
node1.link(node2)
node1.traverse()
print(node1.value)
print(node2.value)
