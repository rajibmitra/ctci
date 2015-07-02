import unittest
from classes.linkedlist import *
from removeduplicates import *
from kthlast import *
from deletenode import *

class TestNode(unittest.TestCase):
    def testStrRepr(self):
        '''The string representation of a node should be the expected'''
        n = Node(3)
        self.assertEqual(str(n), '3')

    def testValue(self):
        '''The value of a node should be the expected'''
        n = Node(8)
        self.assertEqual(n, 8)

    def testNoLink(self):
        '''The next node of a new node should be None'''
        n = Node(1)
        self.assertEqual(n.next, None)

class TestLinkedList(unittest.TestCase):
    def testSizeNewList(self):
        '''The size of a fresh list with one node should be 1'''
        ml = LinkedList(4)
        self.assertEqual(len(ml), 1)

    def testSizeFilledList(self):
        '''The size of a list with known number of inserted elements should be the expected'''
        ml = LinkedList(0)
        [ml.append(i) for i in range(1, 5)]
        self.assertEqual(len(ml), 5)

    def testKthOutOfBounds(self):
        '''kth should return None for out of bounds nodes'''
        ml = LinkedList(9)
        self.assertEqual(ml.kth(0), None)
        self.assertEqual(ml.kth(-1), None)
        self.assertEqual(ml.kth(20), None)

    def testKthKnown(self):
        '''kth should return the expected node when it is known'''
        ml = LinkedList(8)
        [ml.append(i) for i in (3, -5, 24, 11, -9)]
        self.assertEqual(ml.kth(1), 8)
        self.assertEqual(ml.kth(3), -5)
        self.assertEqual(ml.kth(6), -9)

    def testRemoveDupl(self):
        '''removeDupl must remove all duplicates from known structures'''
        orig = [38, -5, 14, 8, 8, 8, 7, -5, 38, 9, 38]
        exp  = [38, -5, 14, 8,       7,         9    ]
        ml = LinkedList(orig[0])
        [ml.append(i) for i in orig[1:]]
        removeDupl(ml)
        self.assertEqual(str(ml), str(exp))

    def testRemoveDuplNoBuf(self):
        '''removeDuplNoBuf must remove all duplicates from known structures'''
        orig = [38, -5, 14, 8, 8, 8, 7, -5, 38, 9, 38]
        exp  = [38, -5, 14, 8,       7,         9    ]
        ml = LinkedList(orig[0])
        [ml.append(i) for i in orig[1:]]
        removeDuplNoBuf(ml)
        self.assertEqual(str(ml), str(exp))

    def testKthToLast(self):
        '''kthToLast must return the expected node'''
        ml = LinkedList(8)
        [ml.append(i) for i in (3, -5, 24, 11, -9)]
        self.assertEqual(kthToLast(ml, 0), None)
        self.assertEqual(kthToLast(ml, 6), None)
        self.assertEqual(kthToLast(ml, 1), -9)
        self.assertEqual(kthToLast(ml, 3), 24)

    def testKthToLastRunner(self):
        '''kthToLastRunner must return the expected node'''
        ml = LinkedList(8)
        [ml.append(i) for i in (3, -5, 24, 11, -9)]
        self.assertEqual(kthToLastRunner(ml, 0), None)
        self.assertEqual(kthToLastRunner(ml, 6), None)
        self.assertEqual(kthToLastRunner(ml, 1), -9)
        self.assertEqual(kthToLastRunner(ml, 3), 24)

    def testDeleteNodeNoSizeOne(self):
        '''deleteNode should not remove anything from lists of size 1'''
        orig = exp = [8]
        ml = LinkedList(orig[0])
        n = ml.kth(1)
        deleteNode(n)
        self.assertEqual(str(ml), str(exp))

    def testDeleteNodeLast(self):
        '''deleteNode should not remove the last node'''
        orig = exp = [8, 10]
        ml = LinkedList(orig[0])
        [ml.append(i) for i in orig[1:]]
        n = ml.kth(2)
        deleteNode(n)
        self.assertEqual(str(ml), str(exp))

    def testDeleteNodeKnown(self):
        '''deleteNode should remove the expected node'''
        orig = [1, 2, 3, 4, 5, 6]
        exp =  [1, 2,    4, 5, 6]
        ml = LinkedList(orig[0])
        [ml.append(i) for i in orig[1:]]
        n = ml.kth(3)
        deleteNode(n)
        self.assertEqual(str(ml), str(exp))

if __name__ == '__main__':
    unittest.main()
