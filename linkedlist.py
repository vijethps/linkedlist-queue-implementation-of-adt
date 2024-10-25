
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front_node = None  
        self.rear_node = None   
        self._size = 0          

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear_node is None:
            self.front_node = self.rear_node = new_node
        else:
            self.rear_node.next = new_node
            self.rear_node = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        result = self.front_node.data
        self.front_node = self.front_node.next
        if self.front_node is None: 
            self.rear_node = None
        self._size -= 1
        return result

    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front_node.data

    def is_empty(self):
        return self.front_node is None

    def size(self):
        return self._size

def process_queue_operations(n, operations):
    queue = Queue()

    for operation in operations:
        op = operation.split()
        if op[0] == 'enqueue':
            queue.enqueue(int(op[1]))
        elif op[0] == 'dequeue':
            print(queue.dequeue())
        elif op[0] == 'size':
            print(queue.size())
        elif op[0] == 'front':
            print(queue.front())

if __name__ == "__main__":
    n = int(input())
    operations = [input() for _ in range(n)]
    process_queue_operations(n, operations)
