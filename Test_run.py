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
                     Tree(7),
                     Tree(3,
                          [
                              Tree(2,
                                   [
                                       Tree(1,
                                              [
                                                  Tree(6), Tree(5,
                                                                [
                                                                    Tree(4)
                                                                ])
                                              ])
                                   ])
                          ])
                 ])


def method_test():
    """test checking if correct data is returned by methods:
        sum value
        average
        median
    """
    test = []

    test.append(Test(tree_1, 36, 4.5, 4.5))
    test.append(Test(tree_2, 36, 4.5, 4.5))
    test.append(Test(tree_3, 36, 4.5, 4.5))
    #   Method test
    test_number = 1
    print("Method test")
    for example in test:

        if example.check(Count.sum_value(example.tree), Count.average(example.tree), Count.median(example.tree)):
            print("test number ", test_number, "  SUCCESS")
            # Count.draw(example.tree)
            # Count.write_results(example.tree)
        else:
            print("test number ", test_number, "  FAIL")
            # Count.draw(example.tree)
            # Count.write_results(example.tree)
        test_number += 1

def tree_test():
    """Tree class set/get/delete  branch test """

    print("Tree test")
    #set
    if not tree_1.setBranch("fas"):
        print("Tree test number ", 1, "  SUCCESS")
    else:
        print("Tree test number ", 1, "  Fail")
    if not tree_1.setBranch(tree_2):
        print("Tree test number ", 2, "  SUCCESS")
    else:
        print("Tree test number ", 2, "  Fail")
    if tree_1.setBranch(Tree(9)):
        print("Tree test number ", 3, "  SUCCESS")
    else:
        print("Tree test number ", 3, "  Fail")
    if not tree_1.setBranch(10):
        print("Tree test number ", 4, "  SUCCESS")
    else:
        print("Tree test number ", 3, "  Fail")

if __name__ == "__main__":

    method_test()

    tree_test()

#   Tree test (set,get,del)

