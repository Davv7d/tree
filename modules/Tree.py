class Tree:
    def __init__(self, data, branches=[]):
        if not isinstance(data, int):
            raise ValueError("invalid data")
        for branch in branches:
            if not isinstance(branch, Tree):
                raise ValueError("invalid branch")

        self.data = data
        self.branches = branches

    def __str__(self):
        return str(self.data)

    def setBranch(self, tree):
        """ set new branch to tree """

        if tree == None:
            return False
        if isinstance(tree, Tree):
            if len(tree.branches) > 0:
                return False
            if len(self.branches) > 0:
                self.branches.append(tree)
            else:
                self.branches = [tree]
            return True
        return False

    def getBranch(self, id):
        """ get branch by id """

        if isinstance(id, int):
            if len(self.branches) > id:
                return self.branches[id]
            else:
                return None

        else:
            return None

    def deleteBramch(self, id=None):
        """ delete branch from tree """
        '''
        return value:
            -1  - it's not int
            0   - out of index
            1 - correct
        '''

        if isinstance(id, int):
            if len(self.branches) > id:
                del self.branches[id]
                return 1
            else:
                return 0
        else:
            return -1
