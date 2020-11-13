class singlyLinkedListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class singlyLinkedList():
    def __init__(self, query=[]):
        start, end = 0, len(query)-1
        linkListStart = singlyLinkedListNode(query[start])
        temp = linkListStart
        while start < end:
            start += 1
            temp.next = singlyLinkedListNode(query[start])
            temp = temp.next
        self.head = linkListStart
        self.tail = temp

    def addFirst(self, value):
        self.head = singlyLinkedListNode(value, self.head)

    def addLast(self, value):
        self.tail.next = singlyLinkedListNode(value)
        self.tail = self.tail.next

    def __str__(self):
        a = ''
        node = self.head
        while(node.next):
            a += str(node.val)+', '
            node = node.next
        a += str(node.val)
        return a


if __name__ == "__main__":
    a = singlyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(a)
    a.addFirst(123)
    a.addLast(456)
    print(a)
