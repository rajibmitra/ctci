from classes.linkedlist import *

def kthToLast(ml, k):
    '''kth to last element using indexing'''
    if len(ml) == 0 or k > len(ml) or k < 1:
        return None

    kth = len(ml) - k
    if kth < 1:
        return None

    n = ml.head
    for _ in range(kth):
        n = n.next
    return n

def kthToLastRunner(ml, k):
    if len(ml) == 0 or k >= len(ml) or k < 1:
        return None

    # go to node k
    kth = ml.head
    for _ in range(k):
        kth = kth.next

    # when node k reaches the end node n
    # is the kth to last node
    n = ml.head
    while kth:
        n, kth = n.next, kth.next
    return n

if __name__ == '__main__':
    ml = LinkedList(0)
    for i in (3, -5, 2, 40, -7):
        ml.append(i)
    print(ml)
    for i in (1, 3):
        n = kthToLast(ml, i)
        print('kthToLast({}) = {}'.format(i, n))
