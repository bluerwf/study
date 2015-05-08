class Linklist:
    def __init__(self):
        self.lengh = 0
        self.head = None
        self.end = None

    def insert_node(self, data):
        node = Node(data)
        self.head = node
        self.end = node
        self.lengh += 1

    def travel_linklist(self):
        p = self.head
        while p:
            print p.data
            p = p.next

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data


def main():
    linklist = Linklist()
    linklist.insert_node('u')
    linklist.travel_linklist()

if __name__ == '__main__':
    main()

