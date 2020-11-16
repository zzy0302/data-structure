class singlyLinkedListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __next__(self):
        if self.next:
            return self.next
        else:
            raise StopIteration


class singlyLinkedList():
    def __init__(self, query=[]):
        start, end = 0, len(query)-1
        if end < 0:
            self.head = None
            self.tail = None
            self.length = 0
            return
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
        if self.isEmpty():
            return ''
        a = ''
        node = self.head
        while(node.next):
            a += str(node.val)+' -> '
            node = node.next
        a += str(node.val)
        return a

    def __len__(self):
        return self.length

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is not None:
            temp = self.current
            self.current = self.current.next
            return temp
        else:
            self.current = self.head
            raise StopIteration

    def isEmpty(self):
        return self.head == None

    def addFirst(self, value):
        if self.isEmpty():
            self.head = singlyLinkedListNode(value, self.head)
            self.tail = self.head
            self.length += 1
        else:
            self.head = singlyLinkedListNode(value, self.head)
            self.length += 1

    def addLast(self, value):
        if self.isEmpty():
            self.addFirst(value)
            return
        self.tail.next = singlyLinkedListNode(value)
        self.length += 1
        self.tail = self.tail.next

    def insertAfter(self, target, value):
        if self.isEmpty():
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
        if self.isEmpty():
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
        if self.isEmpty():
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

    def reverse(self):
        _head = self.head
        _tail = self.tail
        if self.isEmpty():
            return False
        if self.head.next == None:
            return True
        if self.length == 2:
            _head.next = None
            _tail.next = _head
            self.head = _tail
            self.tail = _head
            return True
        prev, cur, nxt = self.head, self.head.next, self.head.next.next
        prev.next = None
        # self.head, self.tail = self.head, self.tail
        while nxt and nxt.next:
            nxt, cur.next, prev, cur = nxt.next, prev, cur, nxt
        cur.next = prev
        nxt.next = cur
        self.head = nxt
        return True


if __name__ == "__main__":
    a = singlyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(a)
    print(len(a))
    a.addFirst(123)
    print(a)
    print(len(a))
    a.addLast(456)
    print(a)
    print(len(a))
    a.insertAfter(9, 10)
    print(a)
    print(len(a))
    a.insertBefore(5, 123)
    print(a)
    print(len(a))
    a.remove(1)
    print(a)
    print(len(a))
    a.reverse()
    print(a)
    for i in a:
        print(i.val)
