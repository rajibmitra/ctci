class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

    def __str__(self):
        return str(self.data)

    def __eq__(self, data):
        return self.data == data

class LinkedList:
    def __init__(self, d):
        self.head = Node(d)
        self.size = 1

    def __len__(self):
        return self.size

    def __str__(self):
        s = '['
        n = self.head
        while n:
            s += '{}'.format(n)
            s += ', ' if n.next else ''
            n = n.next
        s += ']'
        return s

    def append(self, d):
        n = self.head
        # go to the last node
        while n.next:
           n = n.next
        # add the new node next to the last
        n.next = Node(d)
        self.size += 1

    def kth(self, n):
        if not self.head or n < 1:
            return None

        if n > len(self):
            return None

        k = self.head
        for _ in range(n - 1):
            k = k.next
        return k
                                                                                            

if __name__ == '__main__':
    ml = LinkedList(0)
    for i in range(1, 10):
        ml.append(i)
    print(ml)
    print(len(ml))
