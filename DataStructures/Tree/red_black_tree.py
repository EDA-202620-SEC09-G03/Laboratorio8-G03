from DataStructures.Tree import rbt_node as rbt
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl


def new_map():
    my_rbt = {"root": None, "type": "RBT"}
    return my_rbt


def put(my_rbt, key, value):
    if my_rbt is None:
        my_rbt = new_map()
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    rbt.change_color(my_rbt["root"], rbt.BLACK)
    return my_rbt


def insert_node(root, key, value):
    if root is None:
        return rbt.new_node(key, value, rbt.RED)

    cmp = default_compare(key, root)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    if is_red(root["right"]) and not is_red(root["left"]):
        root = rotate_left(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]):
        root = rotate_right(root)
    if is_red(root["left"]) and is_red(root["right"]):
        flip_colors(root)

    root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
    return root


def default_compare(key, element):
    element_key = rbt.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1


def rotate_left(node_rbt):
    x = node_rbt["right"]
    node_rbt["right"] = x["left"]
    x["left"] = node_rbt
    rbt.change_color(x, node_rbt["color"])
    rbt.change_color(node_rbt, rbt.RED)
    x["size"] = node_rbt["size"]
    node_rbt["size"] = size_tree(node_rbt["left"]) + size_tree(node_rbt["right"]) + 1
    return x


def rotate_right(node_rbt):
    x = node_rbt["left"]
    node_rbt["left"] = x["right"]
    x["right"] = node_rbt
    rbt.change_color(x, node_rbt["color"])
    rbt.change_color(node_rbt, rbt.RED)
    x["size"] = node_rbt["size"]
    node_rbt["size"] = size_tree(node_rbt["left"]) + size_tree(node_rbt["right"]) + 1
    return x


def flip_node_color(node_rbt):
    if node_rbt is not None:
        if rbt.is_red(node_rbt):
            rbt.change_color(node_rbt, rbt.BLACK)
        else:
            rbt.change_color(node_rbt, rbt.RED)


def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])


def size_tree(root):
    if root is None:
        return 0
    return root["size"]


def is_red(node_rbt):
    if node_rbt is None:
        return False
    return rbt.is_red(node_rbt)


def get(my_rbt, key):
    return get_node(my_rbt["root"], key)


def get_node(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp < 0:
        return get_node(root["left"], key)
    elif cmp > 0:
        return get_node(root["right"], key)
    return rbt.get_value(root)


def contains(my_rbt, key):
    return get(my_rbt, key) is not None


def size(my_rbt):
    return size_tree(my_rbt["root"])


def is_empty(my_rbt):
    return size(my_rbt) == 0


def key_set(my_rbt):
    key_list = sl.new_list()
    key_set_tree(my_rbt["root"], key_list)
    return key_list


def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sl.add_last(key_list, rbt.get_key(root))
        key_set_tree(root["right"], key_list)
    return key_list


def value_set(my_rbt):
    value_list = sl.new_list()
    value_set_tree(my_rbt["root"], value_list)
    return value_list


def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root["left"], value_list)
        sl.add_last(value_list, rbt.get_value(root))
        value_set_tree(root["right"], value_list)
    return value_list


def get_min(my_rbt):
    return get_min_node(my_rbt["root"])


def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return rbt.get_key(root)
    return get_min_node(root["left"])


def get_max(my_rbt):
    return get_max_node(my_rbt["root"])


def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return rbt.get_key(root)
    return get_max_node(root["right"])


def height(my_rbt):
    return height_tree(my_rbt["root"])


def height_tree(root):
    if root is None:
        return 0
    return 1 + max(height_tree(root["left"]), height_tree(root["right"]))


def keys(my_rbt, key_initial, key_final):
    list_key = al.new_list()
    keys_range(my_rbt["root"], key_initial, key_final, list_key)
    return list_key


def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return list_key
    key = rbt.get_key(root)
    if key_initial < key:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= key <= key_final:
        al.add_last(list_key, key)
    if key < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)
    return list_key


def values(my_rbt, key_initial, key_final):
    list_value = al.new_list()
    values_range(my_rbt["root"], key_initial, key_final, list_value)
    return list_value


def values_range(root, key_initial, key_final, list_value):
    if root is None:
        return list_value
    key = rbt.get_key(root)
    if key_initial < key:
        values_range(root["left"], key_initial, key_final, list_value)
    if key_initial <= key <= key_final:
        al.add_last(list_value, rbt.get_value(root))
    if key < key_final:
        values_range(root["right"], key_initial, key_final, list_value)
    return list_value
