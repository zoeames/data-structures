class newQueue:
    data=[]
    def inqueue(self, name):
        self.data.insert(0, name)
    def dequeue(self):
        return self.data.pop()

