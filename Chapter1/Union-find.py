import time

class quick_find:

    def __init__(self, N):
        self._count = N
        self.id = [i for i in range(N)]

    def count(self):
        return self._count

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        if self.connected(p, q):
            return
        else:
            pID = self.find(p)
            qID = self.find(q)
            for i in range(len(self.id)):
                if self.id[i] == pID:
                    self.id[i] = qID
            self._count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class quick_union:
    def __init__(self, N):
        self._count = N
        self.id = [i for i in range(N)]

    def count(self):
        return self._count

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if self.connected(p, q):
            return
        else:
            self.id[pRoot] = qRoot
            self._count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

class quick_union_w:
    def __init__(self, N):
        self._count = N
        self.id = [i for i in range(N)]
        self.size = [1 for i in range(N)]

    def count(self):
        return self._count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def find(self, p):
        while p!=self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        pRoot = self.find(p)
        qRoot = self.find(q)

        if self.connected(p, q):
            return
        else:
            if self.size[pRoot] > self.size[qRoot]:
                self.id[qRoot] = pRoot
                self.size[pRoot] += 1
            else:
                self.id[pRoot] = qRoot
                self.size[qRoot] += 1
            self._count -= 1

def read_array(file):
    with open(file, 'r') as f:
        array_size = int(f.readline().strip('\n'))
        lines = f.readlines()
        array = []
        for line in lines:
            (p, q) = line.split()
            array.append((int(p), int(q)))
    return array_size, array


if __name__ == '__main__':
    file_list = ["mediumUF.txt", "largeUF.txt"]

    for f in file_list:
        array_size, array = read_array(f)

        uf1 = quick_find(array_size)
        uf2 = quick_union(array_size)
        uf3 = quick_union_w(array_size)

        # start_time_1 = time.time()
        # for p, q in array:
        #     if uf1.connected(p, q):
        #         continue
        #     else:
        #         uf1.union(p, q)
        # elapsed_time_1 = time.time() - start_time_1


        # start_time_2 = time.time()
        # for p, q in array:
        #     if uf2.connected(p, q):
        #         continue
        #     else:
        #         uf2.union(p, q)
        # elapsed_time_2 = time.time() - start_time_2

        start_time_3 = time.time()
        for p, q in array:
            if uf3.connected(p, q):
                continue
            else:
                uf3.union(p, q)
        elapsed_time_3 = time.time() - start_time_3
        #
        # print("Running time for file: %s using algorithm quick_find is %s" %(f, elapsed_time_1))
        # print("Number of component for file: %s is %s\n" %(f, uf1.count()))
        #
        # print("Running time for file: %s using algorithm quick_union is %s" % (f, elapsed_time_2))
        # print("Number of component for file: %s is %s\n" % (f, uf2.count()))

        print("Running time for file: %s using algorithm quick_union_w is %s" % (f, elapsed_time_3))
        print("Number of component for file: %s is %s\n" % (f, uf3.count()))





