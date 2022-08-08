from collections import Counter

def find_internal_nodes_num(tree):
    my_tree_count = Counter(tree)
    del my_tree_count[-1]
    result = len(my_tree_count)
    return result

my_tree = [4, 4, 1, 5, -1, 4, 5]
print(find_internal_nodes_num(my_tree))

