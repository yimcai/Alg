import sys
import argparse

class Node(object):
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

class QuickSort(object):
    def __init__(self,):
        self.sorted_array=[]

    def put(self, root, array_to_be_sorted):
        """pick last value to divide array"""
        if len(array_to_be_sorted) <= 1:
            return 

        divide_value = array_to_be_sorted[-1]  # last item

        left_array = [] 
        right_array = []

        for v in array_to_be_sorted[:-1]:
            if v <= divide_value:
                left_array.append(v)
            else:
                right_array.append(v)

        root.left = Node(left_array[-1]) if left_array else None
        root.right = Node(right_array[-1]) if right_array else None
    
        self.put(root.left, left_array)
        self.put(root.right, right_array)

    def traverse(self, root):
        if root is None:
            return 
        self.traverse(root.left)
        self.sorted_array.append(root.value) 
        self.traverse(root.right)

if __name__ == "__main__":
    """
     array = [3, 6, 4, 10, 15, 7]
          7
         / \
        4   15
       / \  /
      3  6 10
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", nargs="*")
    args = parser.parse_args(sys.argv[1:])
    print(args.list)

    #qs = QuickSort()
    #root = Node(array[-1])
    #qs.put(root, array)
    #qs.traverse(root)
    #print(qs.sorted_array)
