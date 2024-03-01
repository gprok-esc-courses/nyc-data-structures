
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None 


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None 
        self.tail = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

    def remove_front(self):
        data = None
        if self.head is not None:
            data = self.head.data
            self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def insert_back(self, data):
        new_node = Node(data)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = new_node

    def remove_back(self):
        data = None 
        if self.tail is not None:
            data = self.tail.data
            iter = self.head 
            if iter == self.tail:
                self.tail = None
                self.head = None
            else:
                while iter.next != self.tail:
                    iter = iter.next
                iter.next = None 
                self.tail = iter
        return data
    
    def insert_after(self, data, existing_data):
        iter = self.head
        while iter is not None and iter.data != existing_data:
            iter = iter.next
        if iter is None:
            print(existing_data, "not found")
        else:
            new_node = Node(data)
            new_node.next = iter.next
            iter.next = new_node
            if iter == self.tail:
                self.tail = new_node

    def traverse(self):
        iter = self.head
        while iter is not None:
            print(iter.data)
            iter = iter.next

    def size(self):
        counter = 0
        iter = self.head
        while iter is not None:
            counter += 1
            iter = iter.next
        return counter


if __name__ == "__main__":
    list = SinglyLinkedList()
    list.insert_front("Peter")
    list.insert_front("John")
    list.insert_front("Mary")
    list.insert_back("Tom")
    # print("Removed:", list.remove_front())
    # print("Removed:", list.remove_back())
    list.insert_after("Bob", "Tom")
    list.remove_back()
    list.traverse()
    print(list.size())