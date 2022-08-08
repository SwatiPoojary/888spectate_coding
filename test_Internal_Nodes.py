from Internal_Nodes import find_internal_nodes_num


def test_internal_node_success():
    my_tree = [4, 4, 1, 5, -1, 4, 5]
    result = find_internal_nodes_num(my_tree)
    assert result == 3

def test_internal_node_success_second():
    my_tree = [4, 4, 1, 5, -1, 4, 5, 3, 4, 6, 2, 2]
    result = find_internal_nodes_num(my_tree)
    assert result == 6