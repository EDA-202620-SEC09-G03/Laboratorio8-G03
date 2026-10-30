def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1

    if not is_in_array:
        count = -1
    return count
def add_first(my_list, element):
    dicit = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["last"] = dicit
    else:
        dicit["next"] = my_list["first"]
    my_list["first"] = dicit
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    dicit = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = dicit
    else:
        my_list["last"]["next"] = dicit
    my_list["last"] = dicit
    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    return my_list["first"]["info"]
def is_empty(my_list):
    return my_list["size"] == 0


def last_element(my_list):
    return my_list["last"]["info"]


def insert_element(my_list, element, pos):
    if pos == 0:
        add_first(my_list, element)
    elif pos >= my_list["size"]:
        add_last(my_list, element)
    else:
        prev = my_list["first"]
        searchpos = 0
        while searchpos < pos - 1:
            prev = prev["next"]
            searchpos += 1
        node = {"info": element, "next": prev["next"]}
        prev["next"] = node
        my_list["size"] += 1
    return my_list


def remove_first(my_list):
    if is_empty(my_list):
        return None
    removed = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["size"] == 0:
        my_list["last"] = None
    return removed


def remove_last(my_list):
    if is_empty(my_list):
        return None
    removed = my_list["last"]["info"]
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        node = my_list["first"]
        while node["next"] != my_list["last"]:
            node = node["next"]
        node["next"] = None
        my_list["last"] = node
    my_list["size"] -= 1
    return removed


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    if pos == 0:
        remove_first(my_list)
    elif pos == my_list["size"] - 1:
        remove_last(my_list)
    else:
        prev = my_list["first"]
        searchpos = 0
        while searchpos < pos - 1:
            prev = prev["next"]
            searchpos += 1
        prev["next"] = prev["next"]["next"]
        my_list["size"] -= 1
    return my_list


def change_info(my_list, pos, new_info):
    node = my_list["first"]
    searchpos = 0
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    node["info"] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    node1 = my_list["first"]
    searchpos = 0
    while searchpos < pos1:
        node1 = node1["next"]
        searchpos += 1

    node2 = my_list["first"]
    searchpos = 0
    while searchpos < pos2:
        node2 = node2["next"]
        searchpos += 1

    node1["info"], node2["info"] = node2["info"], node1["info"]
    return my_list


def sub_list(my_list, pos, num_elements):
    sublist = new_list()
    node = my_list["first"]
    searchpos = 0
    while searchpos < pos:
        node = node["next"]
        searchpos += 1

    count = 0
    while node is not None and count < num_elements:
        add_last(sublist, node["info"])
        node = node["next"]
        count += 1
    return sublist

def default_sort_criteria(element_1, element_2):
   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def default_sort_criteria_dict(element_1, element_2):

   is_sorted = False
   if float(element_1["average_rating"]) < float(element_2["average_rating"]):
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_crit=default_sort_criteria):
    for i in range(0, my_list["size"] - 1):
        min_index = i
        for j in range(i + 1, my_list["size"]):
            if sort_crit(get_element(my_list, j), get_element(my_list, min_index)):
                min_index = j
        if min_index != i:
            exchange(my_list, i, min_index)
    return my_list

def insertion_sort(my_list, sort_criteria=default_sort_criteria):
    for i in range(size(my_list)):
        actual = i
        while sort_criteria(get_element(my_list, actual), get_element(my_list, actual - 1)) and actual > 0:
            exchange(my_list, actual, actual - 1)
            actual -= 1
    return my_list

def shell_sort(my_list,sort_crit=default_sort_criteria):
    x = my_list["size"]
    y = x//2
    while y > 0:
        for i in range(y,x):
            z = get_element(my_list, i)
            j = i
            while j >= y and not sort_crit(get_element(my_list, j - y) ,z):
                change_info(my_list, j, get_element(my_list, j - y))
                j -= y
            change_info(my_list, j, z)
        y = y//2
    return my_list

def merge_sort(my_list, sort):
    es_contenedor = False
    if isinstance(my_list, dict):
        if "first" in my_list:
            es_contenedor = True
    if es_contenedor:
        nodo_actual = my_list["first"]
    else:
        nodo_actual = my_list
    if nodo_actual is None or nodo_actual["next"] is None:
        resultado = nodo_actual
    else:
        lento = nodo_actual
        rapido = nodo_actual["next"]
        while rapido is not None and rapido["next"] is not None:
            lento = lento["next"]
            rapido = rapido["next"]["next"]
        derecha = lento["next"]
        lento["next"] = None
        izquierda = nodo_actual
        izquierda = merge_sort(izquierda, sort)
        derecha = merge_sort(derecha, sort)
        lista_temporal = {"info": None, "next": None}
        ultimo_nodo = lista_temporal
        while izquierda is not None and derecha is not None:
            if sort(izquierda["info"], derecha["info"]):
                ultimo_nodo["next"] = izquierda
                izquierda = izquierda["next"]
            else:
                ultimo_nodo["next"] = derecha
                derecha = derecha["next"]
            ultimo_nodo = ultimo_nodo["next"]

        if izquierda is not None:
            ultimo_nodo["next"] = izquierda
        else:
            ultimo_nodo["next"] = derecha

        resultado = lista_temporal["next"]
    if es_contenedor:
        my_list["first"] = resultado
        if resultado is not None:
            ultimo = resultado
            while ultimo["next"] is not None:
                ultimo = ultimo["next"]
            my_list["last"] = ultimo
        else:
            my_list["last"] = None
        return my_list

    return resultado

def partition(lst, sort_criteria, lo, hi):
    """
    Función que va dejando el pivote (j) en su lugar, mientras mueve elementos menores a la izquierda del pivote y
    elementos mayores a la derecha del pivote
    Args:
    lst: lista a ordenar
    sort_criteria: función que da un orden total a los elementos de la lista
    lo: posición del primer elemento en el rango de elementos a ordenar
    hi: posición del ultimo elemento en el rango de elementos a ordenar
    Returns:
    La posición en el rango de elementos [lo, hi] donde quedo el pivote
    """
    pivot = get_element(lst, hi)
    pivot_index = lo

    for current_index in range(lo, hi):
        if sort_criteria(get_element(lst, current_index), pivot):
            if current_index != pivot_index:
                exchange(lst, current_index, pivot_index)
            pivot_index += 1

    if pivot_index != hi:
        exchange(lst, pivot_index, hi)

    return pivot_index

def quick_sort(lst, sort_criteria):
    """
    ordenamiento quick sort de una lista.
    Args:
    lst: lista a ordenar
    sort_criteria: función de ordenamiento total
    """
    quick_sort_recursive(lst, sort_criteria, 0, size(lst) - 1)
    return lst


def quick_sort_recursive(lst, sort_criteria, lo, hi):
    """
    Función recursiva para ordenar los menores y los mayores con respecto a un dato de referencia (pivote)
    Args:
    lst: lista a ordenar
    sort_criteria: función de ordenamiento total
    lo: posición del primer elemento en el rango de elementos a ordenar
    hi: posición del ultimo elemento en el rango de elementos a ordenar
    Paso 1. Aplicar la función partition separando los menores de los mayores con respecto a un pivote y
    obtener la posición del pivote
    Paso 2. Ordenamiento recursivo de los datos menores en el rango [lo, pivot-1]
    Paso 3. Ordenamiento recursivo de los datos mayores en el rango [pivot+1, hi]
    """
    if lo < hi:
        pivot_index = partition(lst, sort_criteria, lo, hi)
        quick_sort_recursive(lst, sort_criteria, lo, pivot_index - 1)
        quick_sort_recursive(lst, sort_criteria, pivot_index + 1, hi)