class SinglyLinkedListNode:
    def __init__(self, val, next_node: 'SinglyLinkedListNode' = None):
        self.val = val
        self.__next = next_node

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        if not isinstance(val, SinglyLinkedListNode):
            raise TypeError('Error type')

        self.__next = val

    def __next__(self):
        if self.__next:
            return self.__next
        else:
            raise StopIteration


class SinglyLinkedList:
    def __init__(self, query: list = None):
        if not query:
            query = list()
        start, end = 0, len(query)-1
        if end < 0:
            self.__head = None
            self.__tail = None
            self.__length = 0
            return
        link_list_start = SinglyLinkedListNode(query[start])
        temp = link_list_start
        while start < end:
            start += 1
            temp.next = SinglyLinkedListNode(query[start])
            temp = temp.next
        self.__head = link_list_start
        self.__tail = temp
        self.__length = len(query)

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, val: SinglyLinkedListNode):
        raise Exception('Do not simply set head')

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, val: SinglyLinkedListNode):
        raise Exception('Do not simply set tail')

    def __len__(self):
        return self.__length

    def __str__(self):
        if self.is_empty():
            return ''
        res = ''
        node = self.__head
        while node.next:
            res += str(node.val)+' -> '
            node = node.next
        res += str(node.val)
        return res

    def __iter__(self):
        self.current = self.__head
        return self

    def __next__(self):
        if self.current is not None:
            temp = self.current
            self.current = self.current.next
            return temp
        else:
            self.current = self.__head
            raise StopIteration

    def is_empty(self):
        return self.__head is None

    def add_first(self, value):
        if self.is_empty():
            self.__head = SinglyLinkedListNode(value, self.__head)
            self.__tail = self.__head
            self.__length += 1
        else:
            self.__head = SinglyLinkedListNode(value, self.__head)
            self.__length += 1

    def add_last(self, value):
        if self.is_empty():
            self.add_first(value)
            return
        self.__tail.next = SinglyLinkedListNode(value)
        self.__length += 1
        self.__tail = self.__tail.next

    def insert_after(self, target, value):
        if self.is_empty():
            return False
        node = self.__head
        while node.val != target and node.next:
            node = node.next
        if node.next is None and node.val != target:
            return False
        else:
            node.next = SinglyLinkedListNode(value, node.next)
            self.__length += 1
            return True

    def insert_before(self, target, value):
        if self.is_empty():
            return False
        prev, cur = self.__head, self.__head.next
        if prev.val == target:
            self.add_first(value)
            return True
        while cur.val != target and cur.next:
            prev, cur = cur, cur.next
        if cur.next is None and cur.val != target:
            return False
        else:
            prev.next = SinglyLinkedListNode(value, prev.next)
            self.__length += 1
            return True

    def remove(self, target):
        if self.is_empty():
            return False
        if self.__head.val == target:
            self.__head = self.__head.next
            self.__length -= 1
            return True
        prev, cur = self.__head, self.__head.next
        while cur.val != target and cur.next:
            prev, cur = cur, cur.next
        if cur.next is None and cur.val != target:
            return False
        else:
            prev.next = cur.next
            self.__length -= 1
            return True

    def reverse(self):
        _head = self.__head
        _tail = self.__tail
        if self.is_empty():
            return False
        if self.__head.next is None:
            return True
        if self.__length == 2:
            _head.next = None
            _tail.next = _head
            self.__head = _tail
            self.__tail = _head
            return True
        prev, cur, nxt = self.__head, self.__head.next, self.__head.next.next
        prev.next = None
        while nxt and nxt.next:
            nxt, cur.next, prev, cur = nxt.next, prev, cur, nxt
        cur.next = prev
        nxt.next = cur
        self.__head = nxt
        return True
