class MyCircularQueue:
    queue = []
    size = 0
    EMPTY_QUEUE = -1

    def __init__(self, k: int):
        self.size = k
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if len(self.queue) < self.size:
            self.queue.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if len(self.queue) > 0:
            self.queue = self.queue[1:]
            return True
        else:
            return False
        
    def Front(self) -> int:
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return self.EMPTY_QUEUE
        

    def Rear(self) -> int:
        if len(self.queue) > 0:
            return self.queue[len(self.queue)-1]
        else:
            return self.EMPTY_QUEUE

    def isEmpty(self) -> bool:
        return len(self.queue) == 0

    def isFull(self) -> bool:
        return len(self.queue) == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()