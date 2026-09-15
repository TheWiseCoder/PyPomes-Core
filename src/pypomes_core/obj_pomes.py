import json
import os
from contextlib import suppress
from types import TracebackType
from typing import Any


def obj_is_serializable(obj: Any) -> bool:
    """
    Determine if *obj* is serializable.

    :param obj: the reference object
    :return: *True* if serializable, *False* otherwise
    """
    # initialize the return variable
    result: bool = True

    # verify the object
    try:
        json.dumps(obj)
    except (TypeError, OverflowError):
        result = False

    return result


def obj_to_dict(obj: Any,
                omit_private: bool = True) -> dict[str, Any] | list[Any] | Any:
    """
    Convert the generic object *obj* to a *dict*.

    The conversion is done recursively. Attributes for which exceptions are raised on attempt
    to access them are silently omitted.

    :param obj: the object to be converted
    :param omit_private: whether to omit private attributes (defaults to *True*)
    :return: the dict obtained from *obj*
    """
    # declare the return variable
    result: dict[str, Any] | list[Any] | Any

    if isinstance(obj, dict):
        result = {str(k): obj_to_dict(obj=v,
                                      omit_private=omit_private) for k, v in obj.items()}
    elif isinstance(obj, list | tuple | set):
        result = [obj_to_dict(obj=item,
                              omit_private=omit_private) for item in obj]
    elif hasattr(obj, "__dict__") or not isinstance(obj, str | int | float | bool | type(None)):
        result = {}
        for attr in dir(obj):
            if not (omit_private and attr.startswith("_")):
                value: Any = getattr(obj,
                                     attr,
                                     None)
                if value is not None and not callable(value):
                    result[attr] = obj_to_dict(obj=value,
                                               omit_private=omit_private)
    else:
        result = obj

    return result


def obj_positional(o: Any,
                   /,
                   keys: tuple[Any, ...],
                   values: tuple[Any, ...],
                   def_value: Any = None) -> Any:
    """
    Locate the position of *o* within *keys*, and return the element in the same position in *values*.

    :param o: the source object
    :param keys: the tuple holding the keys to be inspected
    :param values: the tuple holding the positionally corresponding values
    :param def_value: the value to return, if not found (defaults to *None*)
    :return: the value positionally corresponding to the source object, or *def_value* if not found
    """
    # initialize the return variable
    result: Any = def_value

    with suppress(Exception):
        pos: int = keys.index(o)
        result = values[pos]

    return result


def exc_format(exc: Exception,
               exc_info: tuple[type[BaseException], BaseException, TracebackType]) -> str:
    """
    Format the error message resulting from the exception raised in execution time.

    The format to use: <python_module>, <line_number>: <exc_class> - <exc_text>

    :param exc: the exception raised
    :param exc_info: information associated with the exception
    :return: the formatted message
    """
    tback: TracebackType = exc_info[2]
    cls: str = str(exc.__class__)

    # retrieve the execution point where the exception was raised (bottom of the stack)
    tlast: TracebackType = tback
    while tlast.tb_next:
        tlast = tlast.tb_next

    # retrieve the module name and the line number within the module
    try:
        fname: str = os.path.split(p=tlast.tb_frame.f_code.co_filename)[1]
    except Exception:  # noqa: # noinspection PyBroadException
        fname: str = "<unknow module>"
    fline: int = tlast.tb_lineno

    return f"{fname}, {fline}, {cls[8:-2]} - {exc}"
