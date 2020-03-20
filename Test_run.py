from Tree import Tree
from Count import Count_from_tree as Count

class Test:
    def __init__(self, tree, sum, average, median):
        self.tree = tree
        self.sum = sum
        self.average = average
        self.median = median

    def check(self,sum, average, median):
        if self.sum == sum:
            if self.average == average:
                if self.median == median:
                    return True
        return False

# example showing how structure of tree looks like
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

tree_example_table = []
tree_example_table.append(Tree(8, [Tree(7, [ Tree(6), Tree(5), Tree(4)]), Tree(3, [Tree(2, [Tree(1)])])]))
tree_example_table.append(Tree(8, [Tree(7), Tree(3, [Tree(2, [Tree(1, [ Tree(6), Tree(5, [Tree(4)])])])])]))


def method_test(show_tree_and_result = False):
    """test checking if correct data is returned by methods:
        sum value
        average
        median
    """
    test = []
    test_number = 1

    test.append(Test(tree_1, 36, 4.5, 4.5))
    test.append(Test(tree_example_table[0], 36, 4.5, 4.5))
    test.append(Test(tree_example_table[1], 36, 4.5, 4.5))
    #   Method test
    print("=======================================================")
    print("Method test")
    for example in test:

        if example.check(Count.sum_value(example.tree), Count.average(example.tree), Count.median(example.tree)):
            print("test number ", test_number, "  SUCCESS")
            if show_tree_and_result:
                Count.draw(example.tree)
                Count.write_results(example.tree)
        else:
            print("test number ", test_number, "  FAIL")
            if show_tree_and_result:
                Count.draw(example.tree)
                Count.write_results(example.tree)
        test_number += 1
    print("=======================================================")

def tree_test(show_tested_functionality = False):
    """Tree class set/get/delete  branch test """
    print("=======================================================")
    print("Tree test")

    print("setBranch: ")
    test_number = 1
    if show_tested_functionality:
        print("string as a parameter")
    if not tree_1.setBranch("fas"):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("tree with branches as a parameter")
    if not tree_1.setBranch(tree_example_table[1]):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("tree without branches as a parameter")
    if tree_1.setBranch(Tree(9)):
        print("Test ",test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("number as a parameter")
    if not tree_1.setBranch(10):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")


    print("getBranch: ")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if tree_1.getBranch("fas") is None:
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index > 0 as a parameter")
    if tree_1.getBranch(100) is None:
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index < 0 as a parameter")
    if tree_1.getBranch(-100) is None:
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("object(Tree) as a parameter")
    if tree_1.getBranch(Tree(1)) is None:
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("correct int as a parameter")
    if not tree_1.getBranch(0) is None:
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")

    print("deleteBramch: ")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if not tree_1.deleteBramch("fas"):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index > 0 as a parameter")
    if not tree_1.deleteBramch(100):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index < 0 as a parameter")
    if not tree_1.deleteBramch(-100):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("object(Tree) as a parameter")
    if not tree_1.deleteBramch(Tree(1)):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("correct int as a parameter")
    if tree_1.deleteBramch(0):
        print("Test ", test_number, "  SUCCESS")
    else:
        print("Test ", test_number, "  Fail")




if __name__ == "__main__":

    method_test()

    tree_test()

#   Tree test (set,get,del)

