
class JieChengIterator:
    def __init__(self):
        self.n = 1
        self.result = self.n
    def __iter__(self):
        return self
    def __next__(self):
        self.result *= self.n
        self.n += 1
        if self.result > 10000: raise StopIteration
        return  self.result
    def reset(self):
        self.n = 1
        self.result = 1

JieCheng = JieChengIterator()
print([].extend(JieCheng))
JieCheng.reset()