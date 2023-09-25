class MinStat:
    def __init__(self):
        self.v = []
 
    def add_number(self, n):
        self.v.append(n)
 
    def result(self):
        if self.v == []:
            return None
        else:
            return min(self.v)
 
 
class MaxStat:
    def __init__(self):
        self.v = []
 
    def add_number(self, n):
        self.v.append(n)
 
    def result(self):
        if self.v == []:
            return None
        else:
            return max(self.v)
 
 
class AverageStat:
    def __init__(self):
        self.v = []
 
    def add_number(self, n):
        self.v.append(n)
 
    def result(self):
        if self.v == []:
            return None
        else:
            n = len(self.v)
            s = sum(self.v)
            return s / n
