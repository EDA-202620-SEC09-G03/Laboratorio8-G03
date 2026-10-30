

import random

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def _new_table(capacity):
    """
    Crea la tabla: un array_list de tamaño capacity donde cada elemento
    es una single_linked_list vacía.
    """
    table = al.new_list()
    for _ in range(capacity):
        al.add_last(table, sl.new_list())
    return table


def new_map(num_elements, load_factor, prime=109345121):
    """
    Crea una nueva tabla de símbolos (map) sin elementos.

    - prime: número primo usado para calcular el hash.
    - capacity: siguiente primo mayor a num_elements / load_factor.
    - scale: entero aleatorio entre 1 y prime - 1.
    - shift: entero aleatorio entre 0 y prime - 1.
    - table: array_list de tamaño capacity, con una single_linked_list vacía por posición.
    - current_factor: factor de carga actual (inicia en 0).
    - limit_factor: factor de carga límite antes de hacer rehash.
    - size: número de elementos en la tabla (inicia en 0).
    """
    capacity = mf.next_prime(num_elements / load_factor)
    scale = random.randint(1, prime - 1)
    shift = random.randint(0, prime - 1)

    my_map = {'prime': prime,
              'capacity': capacity,
              'scale': scale,
              'shift': shift,
              'table': _new_table(capacity),
              'current_factor': 0,
              'limit_factor': load_factor,
              'size': 0}
    return my_map


def default_compare(key, element):
    """
    Compara una llave con la llave de un map_entry.
    Retorna 0 si son iguales, 1 si key es mayor, -1 si es menor.
    """
    element_key = me.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1


def _find_in_bucket(bucket, key):
    """
    Busca la llave en el bucket. Retorna la posición del entry o -1 si no está.
    """
    for pos in range(sl.size(bucket)):
        entry = sl.get_element(bucket, pos)
        if default_compare(key, entry) == 0:
            return pos
    return -1


def put(my_map, key, value):
    """
    Agrega la pareja llave-valor. Si la llave ya existe, actualiza su valor.
    Si el factor de carga supera el límite, se hace rehash.
    """
    index = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map['table'], index)
    pos = _find_in_bucket(bucket, key)

    if pos != -1:
        # La llave ya existía: se actualiza el valor
        entry = sl.get_element(bucket, pos)
        me.set_value(entry, value)
    else:
        # Llave nueva: se agrega al final del bucket
        sl.add_last(bucket, me.new_map_entry(key, value))
        my_map['size'] += 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
        if my_map['current_factor'] > my_map['limit_factor']:
            my_map = rehash(my_map)
    return my_map


def contains(my_map, key):
    """
    Retorna True si la llave está en la tabla, False en caso contrario.
    """
    index = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map['table'], index)
    return _find_in_bucket(bucket, key) != -1


def get(my_map, key):
    """
    Retorna el valor asociado a la llave, o None si no existe.
    """
    index = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map['table'], index)
    pos = _find_in_bucket(bucket, key)
    if pos == -1:
        return None
    return me.get_value(sl.get_element(bucket, pos))


def remove(my_map, key):
    """
    Elimina la pareja llave-valor asociada a la llave (si existe).
    Retorna la tabla.
    """
    index = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map['table'], index)
    pos = _find_in_bucket(bucket, key)

    if pos != -1:
        # Se reconstruye el bucket sin el entry eliminado
        new_bucket = sl.new_list()
        for i in range(sl.size(bucket)):
            if i != pos:
                sl.add_last(new_bucket, sl.get_element(bucket, i))
        al.change_info(my_map['table'], index, new_bucket)
        my_map['size'] -= 1
        my_map['current_factor'] = my_map['size'] / my_map['capacity']
    return my_map


def size(my_map):
    """
    Retorna el número de parejas llave-valor en la tabla.
    """
    return my_map['size']


def is_empty(my_map):
    """
    Retorna True si la tabla no tiene elementos.
    """
    return my_map['size'] == 0


def key_set(my_map):
    """
    Retorna un array_list con todas las llaves de la tabla.
    """
    keys = al.new_list()
    table = my_map['table']
    for i in range(al.size(table)):
        bucket = al.get_element(table, i)
        for j in range(sl.size(bucket)):
            al.add_last(keys, me.get_key(sl.get_element(bucket, j)))
    return keys


def value_set(my_map):
    """
    Retorna un array_list con todos los valores de la tabla.
    """
    values = al.new_list()
    table = my_map['table']
    for i in range(al.size(table)):
        bucket = al.get_element(table, i)
        for j in range(sl.size(bucket)):
            al.add_last(values, me.get_value(sl.get_element(bucket, j)))
    return values


def rehash(my_map):
    """
    Duplica (aprox.) la capacidad de la tabla: la nueva capacidad es el
    siguiente primo mayor a 2 * capacity, y se reubican todos los entries.
    Retorna la tabla.
    """
    old_table = my_map['table']
    new_capacity = mf.next_prime(2 * my_map['capacity'])

    my_map['capacity'] = new_capacity
    my_map['table'] = _new_table(new_capacity)

    for i in range(al.size(old_table)):
        bucket = al.get_element(old_table, i)
        for j in range(sl.size(bucket)):
            entry = sl.get_element(bucket, j)
            index = mf.hash_value(my_map, me.get_key(entry))
            sl.add_last(al.get_element(my_map['table'], index), entry)

    my_map['current_factor'] = my_map['size'] / new_capacity
    return my_map