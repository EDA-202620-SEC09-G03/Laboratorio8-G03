from DataStructures.Tree import bst_node as node
from DataStructures.List import single_linked_list as sl

def new_map():
    return {"root": None}
 
 
def default_compare(key, element):
    if key == node.get_key(element):
        return 0
    elif key > node.get_key(element):
        return 1
    return -1
 
 
def size_tree(root):
    if root is None:
        return 0
    return root["size"]
 
 
def size(my_bst):
    return size_tree(my_bst["root"])
 
 
def insert_node(root, key, value):
    if root is None:
        return node.new_node(key, value)
 
    compare = default_compare(key, root)
    if compare < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif compare > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value
 
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root
 
 
def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
 
 
def get_node(root, key):
    if root is None:
        return None
 
    compare = default_compare(key, root)
    if compare < 0:
        return get_node(root["left"], key)
    elif compare > 0:
        return get_node(root["right"], key)
    return root
 
 
def get(my_bst, key):
    found = get_node(my_bst["root"], key)
    if found is None:
        return None
    return node.get_value(found)


def contains(my_bst, key):
    return get_node(my_bst["root"], key) is not None


def is_empty(my_bst):
    return my_bst["root"] is None


def remove_node(root, key):
    if root is None:
        return None

    compare = default_compare(key, root)
    if compare < 0:
        root["left"] = remove_node(root["left"], key)
    elif compare > 0:
        root["right"] = remove_node(root["right"], key)
    else:
        # un solo hijo o ninguno
        if root["left"] is None:
            return root["right"]
        if root["right"] is None:
            return root["left"]
        # dos hijos: se reemplaza por el minimo del subarbol derecho
        minimo = get_min_node(root["right"])
        root["key"] = minimo["key"]
        root["value"] = minimo["value"]
        root["right"] = delete_min_node(root["right"])

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def remove(my_bst, key):
    my_bst["root"] = remove_node(my_bst["root"], key)
    return my_bst


def in_order(root, lista, que):
    # que = "key" o "value"
    if root is not None:
        in_order(root["left"], lista, que)
        sl.add_last(lista, root[que])
        in_order(root["right"], lista, que)


def key_set(my_bst):
    lista = sl.new_list()
    in_order(my_bst["root"], lista, "key")
    return lista


def value_set(my_bst):
    lista = sl.new_list()
    in_order(my_bst["root"], lista, "value")
    return lista


def get_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return root
    return get_min_node(root["left"])


def get_min(my_bst):
    minimo = get_min_node(my_bst["root"])
    if minimo is None:
        return None
    return minimo["key"]


def get_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root
    return get_max_node(root["right"])


def get_max(my_bst):
    maximo = get_max_node(my_bst["root"])
    if maximo is None:
        return None
    return maximo["key"]


def delete_min_node(root):
    if root is None:
        return None
    if root["left"] is None:
        return root["right"]
    root["left"] = delete_min_node(root["left"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def delete_min(my_bst):
    my_bst["root"] = delete_min_node(my_bst["root"])
    return my_bst


def delete_max_node(root):
    if root is None:
        return None
    if root["right"] is None:
        return root["left"]
    root["right"] = delete_max_node(root["right"])
    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root


def delete_max(my_bst):
    my_bst["root"] = delete_max_node(my_bst["root"])
    return my_bst


def floor_node(root, key):
    # mayor llave que es menor o igual a key
    if root is None:
        return None
    compare = default_compare(key, root)
    if compare == 0:
        return root
    if compare < 0:
        return floor_node(root["left"], key)
    candidato = floor_node(root["right"], key)
    if candidato is None:
        return root
    return candidato


def floor(my_bst, key):
    resultado = floor_node(my_bst["root"], key)
    if resultado is None:
        return None
    return resultado["key"]


def ceiling_node(root, key):
    # menor llave que es mayor o igual a key
    if root is None:
        return None
    compare = default_compare(key, root)
    if compare == 0:
        return root
    if compare > 0:
        return ceiling_node(root["right"], key)
    candidato = ceiling_node(root["left"], key)
    if candidato is None:
        return root
    return candidato


def ceiling(my_bst, key):
    resultado = ceiling_node(my_bst["root"], key)
    if resultado is None:
        return None
    return resultado["key"]


def select_node(root, pos):
    # llave que tiene pos llaves menores (pos empieza en 0)
    if root is None:
        return None
    tam_izq = size_tree(root["left"])
    if pos < tam_izq:
        return select_node(root["left"], pos)
    elif pos > tam_izq:
        return select_node(root["right"], pos - tam_izq - 1)
    return root


def select(my_bst, pos):
    if pos < 0 or pos >= size(my_bst):
        return None
    resultado = select_node(my_bst["root"], pos)
    if resultado is None:
        return None
    return resultado["key"]


def rank_node(root, key):
    # cantidad de llaves menores que key
    if root is None:
        return 0
    compare = default_compare(key, root)
    if compare < 0:
        return rank_node(root["left"], key)
    elif compare > 0:
        return 1 + size_tree(root["left"]) + rank_node(root["right"], key)
    return size_tree(root["left"])


def rank(my_bst, key):
    return rank_node(my_bst["root"], key)


def height_node(root):
    if root is None:
        return 0
    altura_izq = height_node(root["left"])
    altura_der = height_node(root["right"])
    if altura_izq > altura_der:
        return 1 + altura_izq
    return 1 + altura_der


def height(my_bst):
    return height_node(my_bst["root"])


def keys_range(root, lo, hi, lista, que):
    if root is None:
        return
    if lo < root["key"]:
        keys_range(root["left"], lo, hi, lista, que)
    if lo <= root["key"] and root["key"] <= hi:
        sl.add_last(lista, root[que])
    if hi > root["key"]:
        keys_range(root["right"], lo, hi, lista, que)


def keys(my_bst, key_initial, key_final):
    lista = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, lista, "key")
    return lista


def values(my_bst, key_initial, key_final):
    lista = sl.new_list()
    keys_range(my_bst["root"], key_initial, key_final, lista, "value")
    return lista
