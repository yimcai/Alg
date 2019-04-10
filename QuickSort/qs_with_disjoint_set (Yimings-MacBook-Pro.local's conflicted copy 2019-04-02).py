import numpy as np 


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class QS(object):
    def __init__(self, data):
        self.data = [Node(i) for i in data]
        self._sorted_array = []

    def _sort(self, data):
        if len(data) <= 1:
            return 
        root = data[-1]
        left, right = [], []
        for node in data[:-1]:
            if node.value <= root.value:
                left.append(node)
            else:
                right.append(node)
        root.left = left[-1] if left else None
        root.right = right[-1] if right else None 
        
        left_data = left[:-1] if left else []
        right_data = right[:-1] if right else []

        self._sort(left_data)
        self._sort(right_data)

    def _traverse(self, start_node):
        if start_node is None:
            return 
        self._traverse(start_node.left)
        self._sorted_array.append(start_node.value)
        self._traverse(start_node.right)

if __name__ == "__main__":
    arr = [19,52,1,70,27,97,93,24,67,78]
    qs = QS(arr)
    qs._sort(qs.data)
    qs._traverse(qs.data[-1])
    print(qs._sorted_array)
