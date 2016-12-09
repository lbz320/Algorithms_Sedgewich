class sorting:
    def __init__(self, a):
        self._a = a
        self.a = a

    def exchange(self, i, j):
        t = self.a[i]
        self.a[i] = self.a[j]
        self.a[j] = t

    def less(self, i, j):
        return self.a[i]<self.a[j]

    def isSorted(self):
        for i in range(1, len(self.a)):
            if self.a[i] < self.a[i-1]:
                return False
        return True

    def insert_sort(self):

        self.a = self._a[:]

        for i in range(1, len(self.a)):
            for j in range(i-1, -1, -1):
                if self.less(j, i):
                    self.exchange(i, j)
if __name__ == "__main__":
    sample = [1,3,4,2,-1, 0]
    s = sorting(sample)
    s.insert_sort()
    print(s.a)
    print(s.isSorted())


