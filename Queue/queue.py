class Queue():
    #creating constructor
    def __init__(self,*args):
        self.items = [*args]
        # A list will contain values of queue 
        if self.items:
            self.front = self.items[0]
            self.rear = self.items[-1]
        else:
            self.front = None
            self.rear = None
    #enque method will add an element to the queue
    def enque(self,value):
        self.items.insert(0,value)
    #here we are setting rear and front of queue
        self.front = self.items[0]
        self.rear = self.items[-1]
    #dequeue mthod which will delete items from the rear of the queue 
    def dequeue(self):
        self.items.pop()
        #here we are adjusting the rear 
        if self.items:
            self.rear = self.items[-1]
        else:
            self.front = None
            self.rear = None
    #here we are creating the string representaion of our queue
    def __str__(self):
        return f'Queue{self.items}'
            
