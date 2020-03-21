from Tree import Tree
from Count import Count_from_tree as Count


class Test:
    def __init__(self, tree, sum_value, average, median):
        self.tree = tree
        self.sum = sum_value
        self.average = average
        self.median = median

    def check(self, sum_value, average, median):
        if self.sum == sum_value:
            if self.average == average:
                if self.median == median:
                    return True
        return False

    def write_expected_results(self):
        print("Sum: ", self.sum)
        print("Average: ", self.average)
        print("Median: ", self.median)


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
tree_example_table.append(Tree(8, [Tree(7, [Tree(6), Tree(5), Tree(4)]), Tree(3, [Tree(2, [Tree(1)])])]))
tree_example_table.append(Tree(8, [Tree(7), Tree(3, [Tree(2, [Tree(1, [Tree(6), Tree(5, [Tree(4)])])])])]))
tree_example_table.append(Tree(83, [Tree(-41, [Tree(-15), Tree(26), Tree(-74), Tree(-77), Tree(-85), Tree(-11), Tree(-51), Tree(-99), Tree(-95), Tree(-42), Tree(-100), Tree(-87), Tree(-98), Tree(-30), Tree(4), Tree(-93, [Tree(17, [Tree(74, [Tree(78), Tree(27), Tree(68)])])])]), Tree(85, [Tree(-76), Tree(-17), Tree(-12), Tree(-59)]), Tree(60, [Tree(-52, [Tree(22), Tree(93)])])]))
tree_example_table.append(Tree(-18, [Tree(12, [Tree(0, [Tree(6, [Tree(-2, [Tree(12, [Tree(-4, [Tree(8)])])])])])])]))
tree_example_table.append(Tree(-65, [Tree(-47, [Tree(52), Tree(-76)]), Tree(-82, [Tree(-46, [Tree(-10, [Tree(44)])])]), Tree(-53, [Tree(-88), Tree(-39)])]))
tree_example_table.append(Tree(13, [Tree(46), Tree(81), Tree(-13), Tree(72, [Tree(-45)]), Tree(10), Tree(24, [Tree(-47), Tree(86), Tree(83)]), Tree(21), Tree(75, [Tree(-35), Tree(-6)]), Tree(94)]))
tree_example_table.append(Tree(-20, [Tree(-7, [Tree(31), Tree(-19, [Tree(77)])]), Tree(40, [Tree(27, [Tree(58), Tree(88, [Tree(35)])])])]))


def method_test_correct_value(show_tree_and_result=False):
    """test checking if correct data is returned by methods:
        sum value
        average
        median
    """
    test = []
    test_number = 1
    correct_result = 0
    test.append(Test(tree_1, 36, 4.5, 4.5))
    test.append(Test(tree_example_table[0], 36, 4.5, 4.5))
    test.append(Test(tree_example_table[1], 36, 4.5, 4.5))
    test.append(Test(tree_example_table[2], -577, -18.03125, -23.5))
    test.append(Test(tree_example_table[3], 14, 1.75, 3))
    test.append(Test(tree_example_table[4], -410, -37.27272727272727, -47))
    test.append(Test(tree_example_table[5], 459, 28.6875, 22.5))
    test.append(Test(tree_example_table[6], 310, 31, 33))

    print("=======================================================")
    print("Method test")
    for example in test:

        if example.check(Count.sum_value(example.tree), Count.average(example.tree), Count.median(example.tree)):
            print("Test ", test_number, "  SUCCESS")
            correct_result += 1
        else:
            print("Test ", test_number, "  FAIL")
        if show_tree_and_result:
            Count.draw(example.tree)
            print("Result Received:")
            Count.write_results(example.tree)
            print("Expected Result:")
            example.write_expected_results()
            print("===========")
        test_number += 1

    ############################################
    print("change data for 2 tree")
    tree_1.setBranch(Tree(12))
    if not test[0].check(Count.sum_value(test[0].tree), Count.average(test[0].tree), Count.median(test[0].tree)):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  FAIL")
    if show_tree_and_result:
        print("Result change after changing data (added 12)")
        Count.draw(test[0].tree)
        print("Result Received:")
        Count.write_results(test[0].tree)
        print("Expected Result(Old):")
        test[0].write_expected_results()
        print("===========")

    test_number += 1
    tree_example_table[3].getBranch(0).setBranch(Tree(100))
    if not test[4].check(Count.sum_value(test[4].tree), Count.average(test[4].tree), Count.median(test[4].tree)):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  FAIL")
    if show_tree_and_result:
        print("Result change after changing data(added 100)")
        Count.draw(test[4].tree)
        print("Result Received:")
        Count.write_results(test[4].tree)
        print("Expected Result(Old):")
        test[4].write_expected_results()
        print("===========")

    print("=======================================================")
    return test_number, correct_result


def tree_test(show_tested_functionality=False):
    """Tree class set/get/delete  branch test """
    print("=======================================================")
    print("Tree test")

    print("setBranch: ")
    test_number = 1
    correct_result = 0
    if show_tested_functionality:
        print("string as a parameter")
    if not tree_1.setBranch("fas"):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("tree with branches as a parameter")
    if not tree_1.setBranch(tree_example_table[1]):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("tree without branches as a parameter")
    if tree_1.setBranch(Tree(9)):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("number as a parameter")
    if not tree_1.setBranch(10):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if not tree_1.setBranch(None):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")

    ############################################
    print("getBranch: ")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if tree_1.getBranch("fas") is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index > 0 as a parameter")
    if tree_1.getBranch(100) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index < 0 as a parameter")
    if tree_1.getBranch(-100) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("object(Tree) as a parameter")
    if tree_1.getBranch(Tree(1)) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("correct int as a parameter")
    if not tree_1.getBranch(0) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if tree_1.getBranch(None) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")

    ############################################
    print("deleteBramch: ")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if not tree_1.deleteBramch("fas"):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index > 0 as a parameter")
    if not tree_1.deleteBramch(100):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("int out of index < 0 as a parameter")
    if not tree_1.deleteBramch(-100):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("object(Tree) as a parameter")
    if not tree_1.deleteBramch(Tree(1)):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("correct int as a parameter")
    if tree_1.deleteBramch(0):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if not tree_1.deleteBramch(None):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")

    print("=======================================================")
    return test_number, correct_result


def count_from_tree_test(show_tested_functionality=False):
    """Count_from_tree class method test"""
    print("=======================================================")
    print("Count_from_tree test")

    print("average: ")
    test_number = 1
    correct_result = 0
    if show_tested_functionality:
        print("int as a parameter")
    if Count.average(1) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if Count.average("test") is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if Count.average(None) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1

    ############################################
    print("sum_value: ")
    if show_tested_functionality:
        print("int as a parameter")
    if Count.sum_value(1) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if Count.sum_value("test") is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if Count.sum_value(None) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1

    ############################################
    print("median: ")
    if show_tested_functionality:
        print("int as a parameter")
    if Count.median(1) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1

    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if Count.median("test") is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if Count.median(None) is None:
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1

    ############################################
    print("is_Tree: ")
    if show_tested_functionality:
        print("int as a parameter")
    if not Count.is_Tree(1):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("string as a parameter")
    if not Count.is_Tree("test"):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    test_number += 1
    if show_tested_functionality:
        print("None as a parameter")
    if not Count.is_Tree(None):
        print("Test ", test_number, "  SUCCESS")
        correct_result += 1
    else:
        print("Test ", test_number, "  Fail")
    print("=======================================================")
    return test_number, correct_result


if __name__ == "__main__":
    test_number = 0
    correct_result = 0

    result1 = method_test_correct_value() #add True to see more details about tests
    test_number += result1[0]
    correct_result += result1[1]

    result2 = tree_test() #add True to see more details about tests
    test_number += result2[0]
    correct_result += result2[1]

    result3 = count_from_tree_test() #add True to see more details about tests
    test_number += result3[0]
    correct_result += result3[1]

    print("Number of tests: ", test_number)
    print("Correct Results: ", correct_result)
