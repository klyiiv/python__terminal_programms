class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = x + w
        self.h = y + h
 
    def intersection(self, elem):
        x, y = elem.get_x(), elem.get_y()
        w, h = elem.get_w(), elem.get_h()
 
        if ((x >= self.x + self.w) or (y >= self.y + self.h) or
                (self.x >= x + w) or (self.y >= y + h)):
            return
        else:
            other = Rectangle(0, 0, 0, 0)
            other.x = max(self.x, x)
            other.w = min(self.w, x + w) - other.x
            other.y = max(self.y, y)
            other.h = min(self.h, y + h) - other.y
            return other
 
    def get_y(self):
        return self.y
 
    def get_x(self):
        return self.x
 
    def get_w(self):
        return self.w
 
    def get_h(self):
        return self.h
