import modules.Draw as Draw
import modules.Methods as Method

class Count_from_tree:
    @staticmethod
    def sum_value(tree):
        return Method.total_value(tree)

    @staticmethod
    def average(tree):
        return Method.average_value(tree)

    @staticmethod
    def median(tree):
        return Method.median(tree)

    @staticmethod
    def draw(tree):
        Draw.draw_tree(tree)

    @staticmethod
    def write_results(tree):
        print("Sum: ", Count_from_tree.sum_value(tree))
        print("Average: ", Count_from_tree.average(tree))
        print("Median: ", Count_from_tree.median(tree))

