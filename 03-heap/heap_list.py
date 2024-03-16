
class MaxHeapEmptyException(Exception):
    pass


class MaxHeap:
    def __init__(self) -> None:
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0
    
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        return self.remove(0)

    def remove(self, pos):
        if self.is_empty():
            raise MaxHeapEmptyException("Priority list empty")
        top = self.get_max()
        last = len(self.heap) - 1
        self.heap[pos] = self.heap[last]
        self.heap.pop()
        self.heapify_down(pos)
        return top

    def get_parent_pos(self, pos):
        return (pos - 1) // 2

    def get_max(self) -> int:
        if self.is_empty():
            raise MaxHeapEmptyException("Priority list empty")
        return self.heap[0]
    
    def heapify_up(self, pos):
        while pos > 0:
            parent = self.get_parent_pos(pos)
            if self.heap[parent] < self.heap[pos]:
                self.heap[parent], self.heap[pos] = self.heap[pos], self.heap[parent]
                pos = parent
            else:
                break

    def heapify_down(self, pos):
        while pos is not None:
            max_child = self.get_max_child_pos(pos)
            if max_child is not None:
                if self.heap[pos] < self.heap[max_child]:
                    self.heap[pos], self.heap[max_child] = self.heap[max_child], self.heap[pos]
                    pos = max_child
                else:
                    break
            else:
                pos = None
            
        # find max child pos
        # if max child > current pos, swap and go to max child pos, else stop
        pass


    def get_max_child_pos(self, pos):
        left = self.left_child_pos(pos)
        right = self.right_child_pos(pos)
        if left is None:
            return None
        elif right is None:
            return left 
        else:
            return left if self.heap[left] > self.heap[right] else right


    def left_child_pos(self, pos):
        left_pos = pos * 2 + 1
        if left_pos >= len(self.heap):
            return None
        else:
            return left_pos 
    
    def right_child_pos(self, pos):
        right_pos = pos * 2 + 2
        if right_pos >= len(self.heap):
            return None
        else:
            return right_pos


if __name__ == "__main__":
    heap = MaxHeap()

    try:
        print(heap.get_max())
    except MaxHeapEmptyException:
        print("No values in the priority queue")

    heap.insert(34)
    heap.insert(23)
    heap.insert(4)
    heap.insert(50)
    heap.insert(12)
    heap.insert(2)
    heap.insert(61)
    heap.insert(40)
    print(heap.heap)
    heap.pop()
    print(heap.heap)
            
