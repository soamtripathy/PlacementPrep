#create nodes
#Create Linked List
# Add nodes to Linked List
#Print Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,newNode):
        #head=>John=>None
        if self.head is None:
            self.head = newNode
        else:
            #head=>John=>Ben=>None
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def printList(self):
        #head=>John=>Ben=>Mathews=>None
        # if self.head is None:
        #     print("List is empty")
        #     return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next 
#firstNode.data => John, firstNode.next = None
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode= Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Mathews")
linkedList.insert(thirdNode)
linkedList.printList()