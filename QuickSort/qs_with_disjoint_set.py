import sys
import numpy as np 


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class QS(object):
    def __init__(self, arr_to_sort):
        self._data = [Node(i) for i in arr_to_sort]
        self._sorted_arr = []

    def _sort(self, arr_index):
        """
        params:
        --------
        _data: list of index indicating the position in self._data
        """

        if len(arr_index) <= 1:
            return 
        root_index = arr_index[-1]
        left, right = [],[]  # index
        for node_index in arr_index[:-1]:
            if self.data[node_index].value <= self.data[root_index].value:
                left.append(node_index)
            else:
                right.append(node_index)
        self.data[root_index].left = left[-1] if left else None
        self.data[root_index].right = right[-1] if right else None

        self._sort(left)
        self._sort(right)
    
    def sort(self):
        self._sort(range(len(self.data)))

    def _traverse(self, node_index):
        if node_index is None:
            return 
        self._traverse(self.data[node_index].left)
        self._sorted_arr.append(self.data[node_index].value)
        self._traverse(self.data[node_index].right)
    
    def traverse(self):
        start_index = range(len(arr))[-1]
        self._traverse(start_index)
        return self._sorted_arr 

    def _bfs(self, node_index):
        from queue import Queue
        q = Queue()
        q.put(node_index)
        while not q.empty():
            root_index = q.get()
            print(self.data[root_index].value)
            left_index = self.data[root_index].left
            right_index = self.data[root_index].right
            if left_index is not None:
                q.put(left_index)
            if right_index is not None:
                q.put(right_index)
            

    @property
    def data(self,):
        return self._data

if __name__ == "__main__":
    arr = np.random.randint(0, int(sys.argv[1]), int(sys.argv[2]))
    # print(arr)
    qs = QS(arr)
    qs.sort()
    # depth first search 
    sorted_arr = qs.traverse()
    # breadth first search
    # qs._bfs(range(len(arr))[-1])
