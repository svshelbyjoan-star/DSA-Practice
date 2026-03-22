class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.top
        self.top=new_node
    def pop(self):
        if self.top is None:
            print("stack is empty")
            return 
        temp=self.top
        self.top=temp.next
        return self.top.data
    def peek(self):
        if self.top is None:
            print("stack is empty")
            return None
        return self.top.data
    def display(self):
        temp=self.top
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def search(self,key):
        temp=self.top
        while temp is not None:
            if temp.data==key:
                return True
            temp=temp.next
        return False
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
# Output:
# 30
# 20
# 10

print(s.peek())   # 30

s.pop()
s.display()
# Output:
# 20
# 10

print(s.search(20))   # True
print(s.search(100))  # False