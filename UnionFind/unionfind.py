class UnionFind(object):
    def __init__(self, N):
        """
        params:
        --------
        N: int, number of nodes
        """
        self.N = list(range(N)) 

    def find(self, p):
        if self.N[p] == p:
            return p
        return self.find(self.N[p])

    def union(self, p, q):
        self.N[p] = q 

    def connected(self, p, q):
        return self.find(p) == self.find(q)


if __name__ == "__main__":
    uf = UnionFind(7)
    pairs_to_union = [(0, 3), (3, 6), (4, 1) , (2, 6), (1, 2)]
    print("data before union: ", uf.N)
    for (p, q) in pairs_to_union:
        uf.union(p ,q)
    print("data after union: ", uf.N)

    test_data = [(1,5), (2, 3), (4, 6)]
    for (p,q) in test_data:
        if uf.connected(p,q):
            print(f"{p} and {q} are connected")
        else:
            print(f"{p} and {q} are not connected")
    
