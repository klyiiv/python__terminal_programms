class MinMaxWordFinder:
 
    def __init__(self):
        self.text = []
 
    def add_sentence(self, s):
        self.text += s.split()
 
    def shortest_words(self):
        self.text = sorted(self.text, key=len)
        return sorted(list(filter(lambda x: len(x) == len(self.text[0]), self.text)))
 
    def longest_words(self):
        self.text = sorted(self.text, key=len)
        return sorted(list(set(sorted(list(filter(lambda x: len(x) == len(self.text[-1]), self.text))))))
