def draw_tree(tree, distance = ""):
    """ Draw structure of tree """
    if tree == None: return
    print(distance, tree)
    distance += "- - "
    for branch in tree.branches:
        draw_tree(branch, distance)
