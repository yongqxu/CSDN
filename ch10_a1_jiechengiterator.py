
class JieChengIterator:
    def __init__(self):
        self.n = 1
        self.result = self.n
    def __iter__(self):
        return self
    def __next__(self):
        self.result *= self.n
        self.n += 1
        return  self.result
    def reset(self):
        self.n = 1
        self.result = 1

JieCheng = JieChengIterator()
for i in JieCheng:
    if i > 10000:
        break
    print(i, end=' ')
JieCheng.reset()