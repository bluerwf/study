
class LinkList:
    def __init__(self):
        self.len = 0
        self.head = None
        self.rear = None

    def insert_rear(self,node):
        if isinstance(node, Node):
            if not self.head:
                self.head = node
                self.rear = node
            else:
                p = self.rear
                p.next = node
                self.rear = node
                node.index = p.index +1
            self.len  += 1

    def insert_head(self, node):
        if isinstance(node, Node):
            if not self.head:
                self.head = node
                self.rear = node
            else:
                p = self.head
                self.head = node
                node.next = p
                while p:
                    p.index += 1
                    p = p.next
            self.len += 1

    def delete_node(self, idx):
        if idx < self.len:
            p = self.head
            while idx:
                p = p.next
                idx -= 1
            d = p.next    
            p.next = p.next.next
            d.next = None
            del d


    def middle(self):
        p = self.head
        q = self.head
        while q.next:
            p = p.next
            q = q.next.next
        return p

    def travel(self):
        p = self.head
        while p:
            p = p.next
            print p



class Node:
    def __init__(self, data):
        self.index = 0
        self.data = data
        self.next = None

    def __str__(self):
        next = self.next.index if self.next else -1
        return "{}: {} ---> {}".format(self.index, self.data, next) 

def main():

    llist = LinkList()
    data = ('anan', 'shanghai', 'china', '20', 'rong')
    for i in range(5):
        node = Node(data[i])
        #llist.insert_rear(node)
        llist.insert_head(node)
    #node = Node('anan')
    #llist.insert(node)
    llist.travel()
    #print llist.middle()


if __name__ == '__main__':
    main()
