class Point:
    x=0
    y=0
    
    def get(self):
        return print(self.x, self.y)
    
    def set(self, x, y):
        self.x = x
        self.y = y

point = Point()
point.set(3,5)
point.get()
point.set(5,8)
point.get()
