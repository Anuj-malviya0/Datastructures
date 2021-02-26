#creating stack 
class stack():
    '''This objects uses list to implement stack '''
    #creating constructor
    def __init__(self):        
        self.items = []
        self.top = 0
    #creating push method 
    def push(self,value):
        '''inserts a element in to top of stack'''
        self.items.append(value)
        self.top = self.items[-1]
    #creating pop method
    def pop(self):
        '''deletes a element from top of stack'''
        self.items.pop()
        '''if stack is empty then top will have null value'''
        if self.items:
            self.top = self.items[-1]
        else:
            self.top = None
        
    
