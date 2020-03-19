from modules.Tree import Tree
from Count import Count_from_tree as Count

class Test:
    def __init__(self, tree, sume, average, median):
        self.tree = tree
        self.sume = sume
        self.average = average
        self.median = median

    def check(self,sume, average, median):
        if self.sume == sume:
            if self.average == average:
                if self.median == median:
                    return True
        return False

tree_1 = Tree(1,
                 [
                     Tree(2,
                          [
                              Tree(3), Tree(4), Tree(5)
                          ]),
                     Tree(6,
                          [
                              Tree(7,
                                   [
                                       Tree(8)
                                   ])
                          ])
                 ])

tree_2 = Tree(8,
                 [
                     Tree(7,
                          [
                              Tree(6), Tree(5), Tree(4)
                          ]),
                     Tree(3,
                          [
                              Tree(2,
                                   [
                                       Tree(1)
                                   ])
                          ])
                 ])

tree_3 = Tree(8,
                 [
                     Tree(7,
                          [
                              Tree(6), Tree(5), Tree(4)
                          ]),
                     Tree(3,
                          [
                              Tree(2,
                                   [
                                       Tree(1)
                                   ])
                          ])
                 ])





if __name__ == "__main__":

    test = []

    test.append(Test(tree_1, 36, 4.5, 4.5))
    test.append(Test(tree_2, 36, 4.5, 4.5))

    test_number = 0
    for example in test:

        if example.check(Count.sum_value(example.tree), Count.avarage(example.tree), Count.median(example.tree)):
            print("test number ", test_number, "  SUCCESS")
        else:
            print("test number ", test_number, "  FAIL")
            # Count.draw(example.tree)
            # Count.write_results(example.tree)
        test_number += 1
