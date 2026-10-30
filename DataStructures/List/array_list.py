def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist


def get_element(my_list, index):
    return my_list["elements"][index]


def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list


def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list


def size(my_list):
    return my_list["size"]


def first_element(my_list):
    if my_list["size"] <= 0:
        raise IndexError("list index out of range")
    return my_list["elements"][0]

def last_element(my_list):
    if my_list["size"] <= 0:
        raise IndexError("list index out of range")
    return my_list["elements"][-1]

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    return False

def delete_element(my_list, pos):
    if 0 > pos or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    
    result_list = new_list()
    for i in range(my_list["size"]):
        if i == pos:
            continue
        else:
            add_last(result_list, my_list["elements"][i])
    return result_list

def remove_first(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    
    removed_element = my_list["elements"][0]
    result_list = []
    
    for i in range(1, my_list["size"]):
        result_list.append(my_list["elements"][i])

    my_list["elements"] = result_list
    my_list["size"] -= 1
    return removed_element

def remove_last(my_list):
    if is_empty(my_list):
        raise IndexError("list index out of range")
    
    removed_element = my_list["elements"][-1]
    result_list = []
    
    for i in range(my_list["size"] - 1):
        result_list.append(my_list["elements"][i])

    my_list["elements"] = result_list
    my_list["size"] -= 1
    return removed_element

def insert_element(my_list, element, pos):
    if 0 > pos or pos > len(my_list["elements"]):
        raise IndexError("list index out of range")
    result_list = []
    
    for i in range(my_list["size"] + 1):
        if i == pos:
            result_list.append(element)
        if i < len(my_list["elements"]):
            result_list.append(my_list["elements"][i])
            
    my_list["elements"] = result_list
    my_list["size"] += 1
    return my_list
            
def change_info(my_list, pos, new_info):
    if 0 > pos or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if((0 > pos1 or pos1 >= my_list["size"]) or
        (0 > pos2 or pos2 >= my_list["size"])):
        raise IndexError("list index out of range")
    my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    new_size = pos_i + num_elements
    if((0 > pos_i or pos_i > my_list["size"]) or
            (0 > new_size or new_size > my_list["size"])):
        raise IndexError("list index out of range")
    sub_list_result = new_list()
    for i in range(pos_i, new_size):
        add_last(sub_list_result, my_list["elements"][i])
    return sub_list_result

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

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
def selection_sort(my_list, sort):
    for i in range(0, my_list["size"] - 1):
        peque = i
        for j in range(i + 1, my_list["size"]):
            if sort(my_list["elements"][j], my_list["elements"][peque]):
                peque = j
        if peque != i:
            exchange(my_list, i, peque)
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
    elements = my_list["elements"]
    y = x//2
    while y > 0:
        for i in range(y,x):
            z = elements[i]
            j = i
            while j >= y and not sort_crit(elements[j - y] ,z):
                elements[j] = elements[j - y]
                j -= y
            elements[j] = z
        y = y//2
    return my_list

def merge_sort(my_list, sort_criteria):
    if size(my_list) > 1:
        mitad = size(my_list)//2
        derecha = sub_list(my_list, 0, mitad)
        izquierda = sub_list(my_list, mitad, size(my_list) - mitad)
        merge_sort(derecha, sort_criteria)
        merge_sort(izquierda, sort_criteria)
        i = j = k = 0
        while i < size(derecha) and j < size(izquierda):
            if sort_criteria(get_element(derecha, i), get_element(izquierda, j)):
                change_info(my_list, k, get_element(derecha, i))
                i += 1
            else:
                change_info(my_list, k, get_element(izquierda, j))
                j += 1
            k += 1
        while i < size(derecha):
            change_info(my_list, k, get_element(derecha, i))
            i += 1
            k += 1
        while j < size(izquierda):
            change_info(my_list, k, get_element(izquierda, j))
            j += 1
            k += 1
    return my_list
def partition(lst, sort_criteria, lo, hi):
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


def quick_sort(lst, sort_criteria=default_sort_criteria):
    quick_sort_recursive(lst, sort_criteria, 0, size(lst) - 1)
    return lst


def quick_sort_recursive(lst, sort_criteria, lo, hi):
    if lo < hi:
        pivot_index = partition(lst, sort_criteria, lo, hi)
        quick_sort_recursive(lst, sort_criteria, lo, pivot_index - 1)
        quick_sort_recursive(lst, sort_criteria, pivot_index + 1, hi)
