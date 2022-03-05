# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return int((i - 1) / 2)


class Heap:
    def __init__(self):
        self.array = []

    def minHeapify(self, index):
        minimum = index
        l = left(index)
        r = right(index)
        if l in range(len(self.array)) and self.array[l].val < self.array[minimum].val:
            minimum = l
        if r in range(len(self.array)) and self.array[r].val < self.array[minimum].val:
            minimum = r
        if minimum != index:
            self.array[minimum], self.array[index] = self.array[index], self.array[minimum]
            self.minHeapify(minimum)

    """def buildMinHeap(self, arr):
        self.array = arr
        for i in range(int(len(self.array)/2) - 1, -1, -1):
            self.minHeapify(i)
        return self.array"""

    def extractMin(self):
        n = len(self.array)
        if n == 0:
            return
        if n == 1:
            return self.array.pop()
        root = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.minHeapify(0)
        return root

    # inserts listNodes and not numbers
    def insert(self, value):
        self.array.append(value)
        i = len(self.array) - 1
        while i != 0 and self.array[i].val < self.array[parent(i)].val:
            self.array[i], self.array[parent(i)] = self.array[parent(i)], self.array[i]
            i = parent(i)

    def printHeap(self):
        print(self.array)


class Solution:
    def mergeKLists(self, lists) -> ListNode:
        heap = Heap()
        for ls in lists:
            if ls:
                heap.insert(ls)
        res = None
        res_next = None
        while True:
            temp = heap.extractMin()
            if not temp:
                return res
            if not res:
                res = temp
                res_next = temp
                temp = temp.next
                if temp:
                    heap.insert(temp)
                res.next = None
            else:
                res_next.next = temp
                temp = temp.next
                res_next = res_next.next
                if temp:
                    heap.insert(temp)
                    res_next.next = None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
