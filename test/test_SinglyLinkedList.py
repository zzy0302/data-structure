import unittest
from linkedList.SinglyLinkedList import SinglyLinkedList


class SinglyLinkedListTest(unittest.TestCase):
    def test_create(self):
        true_lists = [
            [1, 2, 3, 4, 5],
            [1],
            [1, 2],
            [1, 2, 3, 4],
        ]
        for item in true_lists:
            temp = SinglyLinkedList(item)
            assert len(temp) == len(item)
            assert temp.is_empty() is False

        false_lists = [
            [],
            list(),
            None,
        ]
        for item in false_lists:
            temp = SinglyLinkedList(item)
            assert len(temp) == 0
            assert temp.is_empty() is True

    def test_head(self):
        temp = SinglyLinkedList([1, 2, 3, 4, 5])
        temp.head = 1
