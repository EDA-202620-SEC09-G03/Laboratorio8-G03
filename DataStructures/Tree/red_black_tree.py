from DataStructures.Tree import rbt_node as rbt


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
