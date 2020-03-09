    def list_DFS(self):
        """
        Retrieves a list of the nodes from the node its called from that is ordered in a Depth-First Manner.

        Returns:
            A list of all the nodes
        """
        l = []

        ntv = [self]

        while ntv != []:
            c = ntv[0]
            l.append(c)
            ntv = c.children + ntv[1:]

        return l

    def list_BFS(self):
        """
        Retrieves a list of the nodes from the node its called from that is ordered in a Breadth-First Manner.

        Returns:
            A list of all the nodes
        """
        l = []

        ntv = [self]

        while ntv != []:
            c = ntv[0]
            l.append(c)
            ntv = ntv[1:] + c.children

        return l
    
    def list_PRO(self):
        """
        Retrieves a list of the nodes from the node its called from that is based on a pre-order tree traversal.

        Returns:
            A list of all the nodes
        """
        l = []

        ntv = [self]
        while ntv != []:
            cur = ntv[-1]
            l.append(cur)
            ntv = ntv[:-1] + cur.children

        return l
    
    def list_INO(self):
        """
        Retrieves a list of the nodes from the node its called from that is based on a in-order tree traversal.

        Returns:
            A list of all the nodes
        """
        cur = self
        stack = []
        l = []

        while True:
            while cur != None:
                stack.append(cur)
                if cur.children != []:
                    cur = cur.children[0]
                else:
                    cur = None
            if stack == []:
                break
            cur = stack.pop()
            l.append(cur)
            if len(cur.children) > 1:
                cur = cur.children[1]
            else:
                cur = None
        
        return l

    def list_POO(self):
        """
        Retrieves a list of the nodes from the node its called from that is based on a 
        post-order tree traversal.

        Returns:
            A list of all the nodes
        """
        l = []

        ntv = [self]
        while ntv != []:
            cur = ntv[-1]
            l.insert(0, cur)
            ntv = ntv[:-1] + cur.children

        return l

    def __eq__(self, other):
        for x, y in zip(self.list_DFS(), other.list_DFS()):
            if x.name != y.name:
                return False
        
        return True