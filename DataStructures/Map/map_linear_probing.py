import random
from DataStructures.List import array_list as lt
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me

def new_map(num_elements, load_factor, prime=109345121):
    my_table = {
        'prime': prime,
        'capacity': mf.next_prime(num_elements / load_factor),
        'scale': random.randint(1, prime - 1),
        'shift': random.randint(0, prime - 1),
        'table': lt.new_list(),
        'size': 0,
        'current_factor': 0,
        'limit_factor': load_factor
        
    }
    for i in range(my_table["capacity"]):
        lt.add_last(my_table["table"], me.new_map_entry(None, None))
    return my_table

def size(my_map):
    return my_map["size"]

def put(my_map, key, value):
    hash_v = mf.hash_value(my_map, key)
    disponible = find_slot(my_map, key, hash_v)
    lt.change_info(my_map["table"], disponible[1], me.new_map_entry(key, value))
    if not disponible[0]:
       my_map["size"] += 1
    my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    if my_map["current_factor"] > my_map["limit_factor"]:
       my_map = rehash(my_map)
    return my_map
 
def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
       if is_available(my_map["table"], hash_value):
             if first_avail is None:
                first_avail = hash_value
             entry = lt.get_element(my_map["table"], hash_value)
             if me.get_key(entry) is None:
                found = True
       elif default_compare(key, lt.get_element(my_map["table"], hash_value)) == 0:
             first_avail = hash_value
             found = True
             ocupied = True
       hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail

def default_compare(key, entry):
    if key == me.get_key(entry):
       return 0
    elif key > me.get_key(entry):
       return 1
    return -1

def rehash(my_map):
    new_capacity = mf.next_prime(my_map["capacity"] * 2)
    new = new_map(1, my_map["limit_factor"], my_map["prime"])
    new["capacity"] = new_capacity
    new["scale"] = my_map["scale"]
    new["shift"] = my_map["shift"]
    new["table"] = lt.new_list()
    for i in range(new_capacity):
        lt.add_last(new["table"], me.new_map_entry(None, None))
    for entry in my_map["table"]["elements"]:
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            new = put(new, key, me.get_value(entry))
    return new

def contains(my_map, key):
    for entry in my_map["table"]["elements"]:
        if me.get_key(entry) == key:
            return True
    return False

def get(my_map, key):
    hash_val = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_val)
    if found:
        entry = lt.get_element(my_map["table"], pos)
        return me.get_value(entry)
    return None

def is_available(table, pos):
    entry = lt.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
       return True
    return False

def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_value)
    if found:
        lt.change_info(my_map["table"], pos, me.new_map_entry("__EMPTY__", "__EMPTY__"))
        my_map["size"] -= 1
    return my_map

def is_empty(my_map):
    return my_map["size"] == 0

def key_set(my_map):
    res = lt.new_list()
    for entry in my_map["table"]["elements"]:
        key = me.get_key(entry)
        if key is None or key == "__EMPTY__":
            continue
        lt.add_last(res, (key))
    return res

def value_set(my_map):
    res = lt.new_list()
    for entry in my_map["table"]["elements"]:
        key = me.get_key(entry)
        if key is None or key == "__EMPTY__":
            continue
        lt.add_last(res, (me.get_value(entry)))
    return res