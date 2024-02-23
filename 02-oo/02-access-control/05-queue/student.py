class Queue:
    def __init__(self):
        self.new_queue = []


    def add(self, item):
        self.new_queue.append(item)

    def next(self):
        new_item = self.new_queue[0]
        del self.new_queue[0]
        return new_item
    
    def is_empty(self):
        return len(self.new_queue) == 0
        
