class sort:
    def less(self, i, j):
        return i < j

    def exchange(self, array, i, j):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

    def isSorted(self, array):

        if len(array) == 1:
            return True

        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                return False
        return True


class inserting(sort):

    def sort(self, array):

        if len(array) == 1:
            return array

        for i in range(1, len(array)):
            for j in (i, 0, -1):
                if self.less(array[j], array[j-1]):
                    self.exchange(array, j-1, j)
        return array



class merge_sort(sort):

    def _merge(self, array, lo, hi):

        if hi <= lo:
            return

        self.sorted[lo:hi+1] = [i for i in array[lo:hi+1]]

        mid = (hi+lo)/2
        i = lo
        j = mid + 1

        for k in range(lo, hi+1):
            if i > mid:
                array[k] = self.sorted[j]
                j += 1
            elif j > hi:
                array[k] = self.sorted[i]
                i += 1

            elif self.less(self.sorted[i], self.sorted[j]):
                array[k] = self.sorted[i]
                i += 1
            else:
                array[k] = self.sorted[j]
                j += 1

    def _sort(self, array, lo, hi):
        if hi <= lo:
            return

        mid = (lo + hi)/2
        self._sort(array, lo, mid)
        self._sort(array, mid+1, hi)
        self._merge(array, lo, hi)

    def sort(self, array, lo=None, hi=None):
        if lo is None:
            lo = 0
        if hi is None:
            hi = len(array) - 1

        self.sorted = array[:]
        self._sort(array, lo, hi)
        print(array)




