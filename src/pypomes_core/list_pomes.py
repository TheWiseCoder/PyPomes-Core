import contextlib
from base64 import b64encode
from collections import defaultdict
from collections.abc import Iterable
from datetime import date
from enum import Enum, IntEnum
from pathlib import Path
from typing import Any


def list_compare(list1: list,
                 list2: list) -> bool:
    """
    Compare the contents of the two lists *list1* e *list2*.

    Return *True* if all the elements in *list1* are also in *list2*, and vice versa, with the same cardinality.

    :param list1: the first list
    :param list2: the second list
    :return: True if the two lists contain the same elements, in the same quantity, in any order
    """
    # initialize the return variable
    result: bool = True

    # are the input parameters lists containing the same number of elements ?
    if isinstance(list1, list) and \
       isinstance(list2, list) and \
       len(list1) == len(list2):
        # yes, verify whether all elements in 'list1' are also in 'list2', in the same quantity
        for elem in list1:
            # is 'elem' in both lists, in the same quantity ?
            if list1.count(elem) != list2.count(elem):
                # no, the lists are not equal
                result = False
                break
    else:
        # no, the lists are not equal
        result = False

    return result


def list_flatten(source: list[str]) -> str:
    """
    Buiild and return a *str* by concatenating with "." the elements in *source*.

    Exemples:
        - ['1', '2', '']     -> '1.2.'
        - ['', 'a', 'b']     -> '.a.b'
        - ['x', '', '', 'y'] -> 'x...y'
        - ['z']              -> 'z'

    :param source: the source list
    :return: the concatenated elements of the source list
    """
    result: str = ""
    for item in source:
        result += "." + item
    return result[1:]


def list_unflatten(source: str) -> list[str]:
    """
    Build and return a *list*, by splitting *source* into its components separated by ".".

    This *list* will contain the extracted components. Exemples:
        - '1.2.'  -> ['1', '2', '']
        - '.a.b'  -> ['', 'a', 'b']
        - 'x...y' -> ['x', '', '', 'y']
        - 'z'     -> ['z']

    :param source: string with components concatenated by "."
    :return: the list of strings containing the concatenated components
    """
    # import the needed function
    from .str_pomes import str_split_on_mark

    return str_split_on_mark(source, ".")


def list_get_coupled(coupled_elements: list[tuple[str, Any]],
                     primary_element: str) -> Any:
    """
    Retrieve from *coupled_elements*, and return, the element coupled to *primary_element*.

    A coupled element is the second element in the tuple whose first element is *primary_element*.

    If *primary_element* contains an index indication (denoted by *[<pos>]*), this indication is removed.
    This function is used in the transformation of *dicts* (*dict_transform*) and *lists* (*list_transform*),
    from sequences of key pairs.

    :param coupled_elements: list of tuples containing the pairs of elements
    :param primary_element: the primary element
    :return: the couple element, or 'None' if it is not foundo
    """
    # initialize the return variable
    result: Any | None = None

    # remove the list element indication
    pos1: int = primary_element.find("[")
    while pos1 > 0:
        pos2: int = primary_element.find("]", pos1)
        primary_element = primary_element[:pos1] + primary_element[pos2+1:]
        pos1 = primary_element.find("[")

    # traverse the list of coupled elements
    for coupled_element in coupled_elements:
        # has the primary element been found ?
        if coupled_element[0] == primary_element:
            # yes, return the corresponding coupled element
            result = coupled_element[1]
            break

    return result


def list_transform(source: list,
                   from_to_keys: list[tuple[str, Any]],
                   prefix_from: str = None,
                   prefix_to: str = None) -> list:
    """
    Construct a new *list*, transforming elements of type *list* and *dict* found in *source*.

    The conversion of *dict* type elements is documented in the *dict_transform* function.

    The prefixes for the source and destination keys, if defined, have different treatments.
    They are added when searching for values in *Source*, and removed when assigning values
    to the return *dict*.

    :param source: the source 'dict' of the values
    :param from_to_keys: the list of tuples containing the source and destination key sequences
    :param prefix_from: prefix to be added to the source keys
    :param prefix_to: prefix to be removed from the target keys
    :return: the new list
    """
    # import the needed function
    from .dict_pomes import dict_transform

    # initialize the return variable
    result: list = []

    # traverse the source list
    for inx, value in enumerate(source):
        if prefix_from is None:
            from_keys: None = None
        else:
            from_keys: str = f"{prefix_from}[{inx}]"

        # obtain the target value
        if isinstance(value, dict):
            to_value: dict = dict_transform(source=value,
                                            from_to_keys=from_to_keys,
                                            prefix_from=from_keys,
                                            prefix_to=prefix_to)
        elif isinstance(value, list):
            to_value: list = list_transform(source=value,
                                            from_to_keys=from_to_keys,
                                            prefix_from=from_keys,
                                            prefix_to=prefix_to)
        else:
            to_value: Any = value

        # added the value transformed to 'result'
        result.append(to_value)

    return result


def list_elem_with_attr(source: list,
                        attr: str,
                        value: Any) -> Any:
    """
    Locate and return the first element in *source* having an attribute named *attr* with value *value*.

    Values obtained by invoking *get* on the element are also considered. *None* is a valid value for *value*.

    :param source: The list to search for the element
    :param attr: the name of the reference attribute
    :param value: the reference value
    :return: The element in *source* having an attribute *attr* with *value*, or *None*
    """
    # initialize the return variable
    result: Any = None

    # traverse the source list
    for element in source:
        if hasattr(element, attr) and getattr(element, attr) == value:
            result = element
            break
        with contextlib.suppress(Exception):
            if element.get(attr) == value:
                result = element
                break

    return result


def list_elem_starting_with(source: list[str | bytes],
                            prefix: str | bytes,
                            keep_prefix: bool = True) -> str | bytes:
    """
    Locate and return the first element in *source* prefixed by *prefix*.

    Retorna *None* se esse elemento não for encontrado.

    :param source: the list to be inspected
    :param prefix: the data prefixing the element to be returned
    :param keep_prefix: defines whether or not the found element should be returned with the prefix
    :return: the prefixed element, with or without the prefix, or *None* if not found
    """
    # initialize the return variable
    result: str | bytes | None = None

    # traverse the source list
    for elem in source:
        if elem.startswith(prefix):
            if keep_prefix:
                result = elem
            else:
                result = elem[len(prefix)+1:]
            break

    return result


def list_prune_duplicates(target: list) -> list:
    """
    Remove all duplicates from *target*.

    The pruned input list is returned, for convenience.

    :param target: the target list
    :return: the target list without duplicate elements
    """
    # a 'dict' maintains the insertion order of its elements
    uniques: dict[Any, None] = dict.fromkeys(target)
    return list(uniques.keys())


def list_prune_in(target: list,
                  ref: list) -> list:
    """
    Remove from *target* all its elements that are also in *ref*.

    The pruned input list is returned, for convenience.

    :param target: the target list
    :param ref: the reference list
    :return: the target list without the elements also in the reference list
    """
    # initialize the return variable
    result: list = target

    removals: list = [item for item in result if item in ref]
    for item in removals:
        result.remove(item)

    return result


def list_prune_not_in(target: list,
                      ref: list) -> list:
    """
    Remove from *target* all of its elements that are not also in *ref*.

    The pruned input list is returned, for convenience.

    :param target: the target list
    :param ref: the reference list
    :return: the target list without the elements not in the reference list
    """
    # initialize the return variable
    result: list = target

    removals: list = [item for item in result if item not in ref]
    for item in removals:
        result.remove(item)

    return result


def list_jsonify(source: list) -> list:
    """
    Return a new *list* containing the values in *source*, made serializable if necessary.

    Possible transformations:
        - *bytes* e *bytearray* are changed to *str* in *Base64* format
        - *date* and *datetime* are changed to their respective ISO representations
        - *Enum* and *StrEnum* are changed to its string representation
        - *IntEnum* is changeds to its integer representation
        - *Path* is changed to its POSIX representation
        - *Iterable* is changed to a *list*, which is then recursively *jsonified*
        - *dict* is recursively *jsonified* (its values, only) by invoking *dict_jsonify()* on it
        - all other types are left unchanged
    The serialization allows for these values to be used in JSON strings.
    HAZARD: depending on the type of object contained in *source*, the final result may not be serializable.

    :param source: the *dict* to be made serializable
    :return: a list with serialized values
    """
    result: list = []
    for value in source:
        if isinstance(value, dict):
            from .dict_pomes import dict_jsonify
            result.append(dict_jsonify(source=value,
                                       jsonify_values=True))
        elif isinstance(value, IntEnum):
            result.append(int(value))
        elif isinstance(value, Enum):
            result.append(str(value))
        elif isinstance(value, Path):
            result.append(value.as_posix())
        elif isinstance(value, bytes | bytearray):
            result.append(b64encode(value).decode())
        elif isinstance(value, date):
            result.append(value.isoformat())
        elif isinstance(value, Iterable) and not isinstance(value, str):
            result.append(list_jsonify(source=list(value)))
        else:
            result.append(value)

    return result


def list_hexify(source: list) -> list:
    """
    Return a new *list* containing the values in *source* changed to appropriate hexadecimal representations.

    Possible transformations:
        - *bytes* e *bytearray* are changed using their built-in *hex()* method
        - *str* is changed to its hexadecimal form (see warning below)
        - *date* and *datetime* are changed to the hexadecimal form of their respective ISO representations
        - *Path* is changed to the hexadecimal form of its POSIX representation
        - *Iterable* is changed to a *list*
        - for all the other types, *str()* is applied and its hexadecimal representation is used
    Note that the reversal of this process is limited to recovering the original strings back from their
    hexadecimal representation. Further recovery, when possible, would have to be carried out manually.
    HAZARD: will raise a *ValueError* exception if a target string has a character with codepoint greater than 255

    :param source: the dict to be made serializable
    :return: a list with serialized values
    :raises ValueError: if a target string has a character with codepoint greater than 255
    """
    # needed imports
    from .str_pomes import str_to_hex
    from .dict_pomes import dict_hexify

    result: list = []
    for value in source:
        if isinstance(value, dict):
            dict_hexify(source=value)
            result.append(value)
        elif isinstance(value, str):
            result.append(str_to_hex(value))
        elif isinstance(value, Iterable):
            result.append(list_jsonify(source=list(value)))
        elif isinstance(value, Path):
            result.append(str_to_hex(value.as_posix()))
        elif isinstance(value, bytes | bytearray):
            result.append(value.hex())
        elif isinstance(value, date):
            result.append(str_to_hex(value.isoformat()))
        else:
            result.append(str_to_hex(str(value)))

    return result


def list_hierarchize(source: list[list | tuple]) -> list:
    """
    Hierarquize a fully sorted list of tuples or list of lists by aggregating common values at all levels.

    To ilustrate, let us assume *source* is the input list:
    ::
      [
        ('John', 'parent Fred', 'old age', 'indifferent'),
        ('John', 'parent Fred', 'old age', 'unaffected'),
        ('John', 'parent Fred', 'poor health', 'broken'),
        ('John', 'parent Fred', 'poor health', 'constrained'),
        ('John', 'parent Fred', 'poor health', 'dependent'),
        ('John', 'parent Kate', 'happy soul'),
        ('John', 'parent Kate', 'very intelligent'),
        ('Mary', 'child John', 'brown eyes'),
        ('Mary', 'child John', 'red hair'),
        ('Mary', 'child Susan', 'blue eyes'),
        ('Mary', 'child Susan', 'median height'),
        ('Mary', 'sibling Joan', 'charming dude'),
        ('Mary', 'sibling Joan', 'smart girl')
     ]

    The resulting hierarquization would yield the list:
    ::
      [
        ['John',
          ['parent Fred',
            ['old age', ['indifferent', 'unaffected']],
            ['poor health', ['broken', 'constrained', 'dependent']]],
          ['parent Kate', ['happy soul', 'very intelligent']]],
        ['Mary',
          ['child John', ['brown eyes', 'red hair']],
          ['child Susan', ['blue eyes', 'median height']],
          ['sibling Joan', ['charming dude', 'smart girl']]]
      ]

    Notes:
      - the elements in *source* must not contain embedded lists or tuples
      - once an aggregation has been given a value, another aggregation cannot be added to it, such as:

        ('John', 'parent Fred', 'poor health', 'dependent'),

        ('John', 'parent Fred', 'poor health', 'constrained', 'simple'),

        ('John', 'parent Fred', 'poor health', 'constrained', 'complex'),

    :param source: the fully sorted list of tuples or list of lists to be hierarchized
    :return: the hierarchized list

    """
    def add_to_hierarchy(hierarchy: dict,
                         keys: list,
                         value: list | tuple) -> None:
        for key in keys[:-1]:
            hierarchy.setdefault(key, {})
        # if isinstance(hierarchy.get(keys[-1]), dict):
        hierarchy.setdefault(keys[-1], []).append(value)

    def convert_to_list(item: Any) -> list:
        result: list
        if isinstance(item, dict):
            result = []
            for k, v in item.items():
                if isinstance(v, dict):
                    result.append([k, *convert_to_list(item=v)])
                else:
                    result.append([k, v] if len(v) > 1 else [k, *v])
        elif isinstance(item, list):
            result = item
        else:
            result = [item]
        return result

    hierarchy: dict = defaultdict(dict)
    for item in source:
        add_to_hierarchy(hierarchy=hierarchy,
                         keys=item[:-1],
                         value=item[-1])

    return convert_to_list(item=hierarchy)
