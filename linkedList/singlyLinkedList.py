class singlyLinkedListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return self.val

    def __next__(self):
        return self.next


class singlyLinkedList():
    def __init__(self, query=[]):
        start, end = 0, len(query)-1
        if end < 0:
            raise IndexError
        linkListStart = singlyLinkedListNode(query[start])
        temp = linkListStart
        while start < end:
            start += 1
            temp.next = singlyLinkedListNode(query[start])
            temp = temp.next
        self.head = linkListStart
        self.tail = temp
        self.length = len(query)

    def __str__(self):
        a = ''
        node = self.head
        while(node.next):
            a += str(node.val)+', '
            node = node.next
        a += str(node.val)
        return a

    def __len__(self):
        return self.length

    def addFirst(self, value):
        self.head = singlyLinkedListNode(value, self.head)
        self.length += 1

    def addLast(self, value):
        self.tail.next = singlyLinkedListNode(value)
        self.length += 1
        self.tail = self.tail.next

    def insertAfter(self, target, value):
        if self.head == None:
            return False
        node = self.head
        while node.val != target and node.next:
            node = node.next
        if node.next == None and node.val != target:
            return False
        else:
            node.next = singlyLinkedListNode(value, node.next)
            self.length += 1
            return True

    def insertBefore(self, target, value):
        if self.head == None:
            return False
        prev, cur = self.head, self.head.next
        if prev.val == target:
            self.addFirst(value)
            return True
        while cur.val != target and cur.next:
            prev, cur = cur, cur.next
        if cur.next == None and cur.val != target:
            return False
        else:
            prev.next = singlyLinkedListNode(value, prev.next)
            self.length += 1
            return True

    def remove(self, target):
        if self.head == None:
            return False
        if self.head.val == target:
            self.head = self.head.next
            self.length -= 1
            return True
        prev, cur = self.head, self.head.next
        while cur.val != target and cur.next:
            prev, cur = cur, cur.next
        if cur.next == None and cur.val != target:
            return False
        else:
            prev.next = cur.next
            self.length -= 1
            return True


if __name__ == "__main__":
    a = singlyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(a)
    print(len(a))
    a.addFirst(123)
    a.addLast(456)
    print(a)
    a.insertAfter(9, 10)
    print(a)
    print(len(a))
    a.insertBefore(5, 123)
    print(a)
    print(len(a))
    a.remove(1)
    print(a)
    print(len(a))
