class Stack:
    #instance method - function on top of method
    data=[]
    def push(self, name):  #self=this in JS
        self.data.append(name)
    def pop(self):
        return self.data.pop()
