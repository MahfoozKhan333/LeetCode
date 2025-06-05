class MyQueue(object):

    def __init__(self):
        self.stackLeft = []
        self.stackRight = []

    def push(self, x):
        self.stackLeft.append(x)

    def pop(self):
        if not self.stackRight:
            while self.stackLeft:
                self.stackRight.append(self.stackLeft.pop())
        return self.stackRight.pop()

    def peek(self):
        if not self.stackRight:
            while self.stackLeft:
                self.stackRight.append(self.stackLeft.pop())
        return self.stackRight[-1]

    def empty(self):
        return not self.stackLeft and not self.stackRight