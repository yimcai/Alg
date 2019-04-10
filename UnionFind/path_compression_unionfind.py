class UnionFind(object):
    def __init__(self, N):
        """
        params:
        --------
        N: int, number of nodes
        """
        self.N = list(range(N))
        self.size = [1]*N

    def _find(self, p):
        if self.N[p] == p: 
            return p
        return self.find(self.N[p])
    
    def find(self, p):
        root = self._find(p)
        while p != root:
            p_next = self.N[p]
            self.N[p] = root
            p = p_next
        return root

    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)
        if self.size[root_p] <= self.size[root_q]:
            self.N[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.N[root_q] = root_p
            self.size[root_p] += self.size[root_q]

    def connected(self, p, q):
        return self.find(p) == self.find(q)


if __name__ == "__main__":
    uf = UnionFind(7)
    pairs_to_union = [(0, 3), (3, 6), (4, 1), (2, 6), (1, 2)]
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
   
