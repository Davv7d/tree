# Tree with unlimited number of branches

How to use Tree & Count:
    1. Import Tree, and Count:
    
        from Tree import Tree
        from Count import Count_from_tree as Count

   2. Create Object tree:
    
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

   3. Use methods from Count(example):
         
            print(Count.sum_value(tree))


 Test:
 At the end of Test_run.py you can add to methods paramter "True", after this you would see more details about tests
