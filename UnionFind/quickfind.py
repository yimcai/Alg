class QuickFind(object):
    def __init__(self, data):
        self.data = data 

    def root(self, v):
        """return the root of node v"""

        if self.data[v] == v:
            return v
        return self.root(self.data[v])

    def union(self, p, q):
        """"""
        return NotImplemented 

    def find(self, i, j):
        """find whether i and j have the same root
        params:
        --------
        i: int, node i 
        j: int, node j 

        return:
        --------
        boolean, True or False
        """
        return self.root(i) == self.root(j)
    

if __name__ == "__main__":
    data = [3, 2, 6, 6, 1, 5, 6]
    QF = QuickFind(data)
    test_data = [(1,5), (2, 3), (4, 6)]
    for (p,q) in test_data:
        if QF.find(p,q):
            print(f"{p} and {q} are connected")
        else:
            print(f"{p} and {q} are not connected")
    
