from LinkedLists import LinkedListTail


class Stack:
    def __init__(self):
        self.myList = LinkedListTail

    def push(self,data):
        self.myList.push_head(data)

    def pop(self):
        return self.myList.pop_end()

class Queue:

    def __init__(self):
        self.myList = LinkedListTail()

    def push(self,data):
        self.myList.push_head(data)

    def pop(self):
        return self.myList.pop_end()


