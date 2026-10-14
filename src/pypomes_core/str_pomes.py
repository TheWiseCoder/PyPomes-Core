import random
import re
import string
from contextlib import suppress
from datetime import date
from pathlib import Path
from typing import Any, Final

DIACRITICS_LOWER: Final[tuple[str, str]] = (
    "áàâãäéèêëíìïóòôõöúùûüç",
    "aaaaaeeeeiiiooooouuuuc"
)
DIACRITICS_UPPER: Final[tuple[str, str]] = (
    "ÁÀÂÃÄÉÈÊËÍÌÏÓÒÔÕÖÚÙÛÜÇ",
    "AAAAAEEEEIIIOOOOOUUUUC"
)
REGEX_METACHARS: Final[str] = ".^$*+?[]()|\\{}"


def str_to_hex(_s: str,
               /) -> str:
    """
    Obtain and return the hex representation of the input string.

    This is an encapsulation of the built-in methods *<str>.encode()* and *<bytes>.hex()*.

    :param _s: the input string
    :return: the hex representation of the input string
    :raises AttributeError: the input is not a string
    :raises UnicodeEncodeError:  a UTF-8 encoding error occurred
    """
    return _s.encode(encoding="utf-8").hex()


def str_from_hex(_str: str,
                 /) -> str:
    """
    Obtain and return the original string from its hex representation in the input string.

    This is an encapsulation of the built-in methods *bytes.fromhex()* and *<bytes>.decode()*

    :param _str: the hex representation of a string
    :return: the original string
    :raises ValueError: the input is not a valid hexadecimal string
    :raises TypeError: the input is not a string
    :raises UnicodeDecodeError: a UTF-8 decoding error occurred
    """
    return bytes.fromhex(_str).decode(encoding="utf-8")


def str_as_list(_str: str,
                /,
                sep: str = ",") -> list[str]:
    """
    Return the input string as a *list*, by splitting its contents separated by *sep*.

    The returned substrings are fully whitespace-trimmed. If the input string is *None*, an empty list is returned.
    If it is an empty *str*, a list containing an empty *str* is returned. If it is not a *str*,
    a list containing itself is returned.

    :param _str: the string value to be worked on
    :param sep: the separator (defaults to ",")
    :return: a list built from the contents of the input string, or containing the input itself, if it is not a string
    """
    # declare the return variable
    result: list[str]

    if isinstance(_str, str):
        result = [s.strip() for s in _str.split(sep=sep)]
    elif _str is None:
        result = []
    else:
        result = [_str]

    return result


def str_sanitize(_str: str,
                 /) -> str:
    """
    Clean the given input string.

    The sanitization is carried out by:
      - removing backslashes
      - replacing double quotes with single quotes
      - replacing newlines and tabs with whitespace
      - replacing multiple consecutive spaces with a single space

    :param _str: the string to be cleaned
    :return: the cleaned string
    """
    cleaned: str = (_str.replace("\\n", "")    # newline representation
                    .replace("\\t", "")    # tab representation
                    .replace("\\", "")
                    .replace('"', "'")
                    .replace("\n", " ")    # actual newline
                    .replace("\t", " "))   # actual tab
    return " ".join(cleaned.split())


def str_split_on_mark(_str: str,
                      /,
                      mark: str) -> list[str]:
    """
    Extract from the input string the text segments separated by *mark*, and return them in a *list*.

    The separator itself will not be in the returned list.

    :param _str: the string to be inspected
    :param mark: the separator
    :return: the list of text segments extracted
    """
    # initialize the return variable
    result: list[str] = []

    pos: int = 0
    skip: int = len(mark)
    after: int = _str.find(mark)
    while after >= 0:
        result.append(_str[pos:after])
        pos = after + skip
        after = _str.find(mark, pos)
    if pos < len(_str):
        result.append(_str[pos:])
    else:
        result.append("")

    return result


def str_find_char(_str: str,
                  /,
                  chars: str) -> int:
    """
    Locate and return the position of the first occurrence, in the input string, of a character in *chars*.

    :param _str: the string to be inspected
    :param chars: the reference characters
    :return: the position of the first character in *chars*, or *-1* if none was found
    """
    # initialize the return variable
    result: int = -1

    # search for whitespace
    for inx, char in enumerate(_str):
        if char in chars:
            result = inx
            break

    return result


def str_find_whitespace(_s: str,
                        /) -> int:
    """
    Locate and return the position of the first occurrence of a *whitespace* character in the input string.

    :param _s: the string to be inspected
    :return: the position of the first whitespace character, or *-1* if none was found
    """
    # initialize the return variable
    result: int = -1

    # search for whitespace
    for inx, char in enumerate(_s):
        if char.isspace():
            result = inx
            break

    return result


def str_between(_str: str,
                /,
                from_str: str,
                to_str: str) -> str:
    """
    Extract and return the *substring* in the input string located between the delimiters *from_str* and *to_str*.

    :param _str: the string to be inspected
    :param from_str: the initial delimiter
    :param to_str: the final delimiter
    :return: the extracted substring, or *None* if no substring was obtained
    """
    # initialize the return variable
    result: str | None = None

    pos1: int = _str.find(from_str)
    if pos1 >= 0:
        pos1 += len(from_str)
        pos2: int = _str.find(to_str, pos1)
        if pos2 >= pos1:
            result = _str[pos1:pos2]

    return result


def str_random(size: int,
               chars: str | list[str] = None) -> str:
    """
    Generate and return a random string containing *len* characters.

    If *chars* is  provided, either as a string or as a list of characters, the characters
    therein will be used in the construction of the random string. Otherwise, a concatenation of
    *string.ascii_letters*, *string.digits*, and *string.punctuation* will provide the base characters.

    :param size: the length of the target random string
    :param chars: optional characters to build the random string from (a string or a list of characters)
    :return: the random string
    """
    # establish the base characters
    if not chars:
        chars: str = string.ascii_letters + string.digits + string.punctuation
    elif isinstance(chars, list):
        chars: str = "".join(chars)

    # generate and return the random string
    # ruff: noqa: S311 - Standard pseudo-random generators are not suitable for cryptographic purposes
    return "".join(random.choice(seq=chars) for _ in range(size))


def str_rreplace(_str: str,
                 /,
                 old: str,
                 new: str,
                 count: int = 1) -> str:
    """
    Replace at most *count* occurrences of substring *old* with string *new* in the input string, in reverse order.

    :param _str: the string to have a substring replaced
    :param old: the substring to replace
    :param new: the string replacement
    :param count: the maximum number of replacements (defaults to 1)
    :return: the modified string
    """
    return _str[::-1].replace(old[::-1], new[::-1], count)[::-1]


def str_splice(_str: str,
               /,
               seps: tuple[str, ...]) -> tuple[str, ...]:
    """
    Splice the input string into segments delimited by the ordered list of separators *seps*.

    The number of segments returned is always the number of separators in *seps*, plus 1.
    An individual segment returned can be null or an empty string. If no separators are found,
    the returned tuple will contain the input string as its last element, and *None* as the remaining elements.
    Separators will not be part of their respective segments.

    Separators in *seps* can not be *None* or empty strings. If no separators are provided
    (*seps* itself is an empty list), then the returned tuple will contain the input string as its only element.
    If the input string starts with the separator, then the return tuple's first element will be an empty string.
    If the input string ends with the separator, then the return tuple's last element will be an empty string.

    These examples illustrate the various possibilities (input is 'My string to be spliced'):
      - () ===> ('My string to be spliced',)
      - ('My') ===> ('',  'string to be spliced')
      - ('tri') ===> ('My s', 'ng to be spliced')
      - ('iced') ===> ('My string to be spl', '')
      - ('X', 'B') ===> (None, None, 'My string to be spliced')
      - ('M', 'd') ===> ('', 'y string to be splice', '')
      - ('s', 's', 'd') ===> ('My ', 'tring to be ', 'plice', '')
      - ('X', 'ri', 'be') ===> (None, 'My st', 'ng to ', ' spliced')

    :param _str: the source string
    :param seps: the ordered list of separators
    :return: tuple with the segments obtained, or *None* if the input is not a string

    """
    # initialize the return variable
    result: tuple[str, ...] | None = None

    if isinstance(_str, str) and None not in seps and "" not in seps:
        segments: list[str | None] = []
        for sep in seps:
            pos: int = _str.find(sep)
            if pos < 0:
                segments.append(None)
            else:
                segments.append(_str[:pos])
                _str = _str[pos + len(sep):]
                if not _str:
                    break

        segments.append(_str)
        segments.extend([None] * (len(seps) - len(segments)))
        result = tuple(segments)

    return result


def str_purge_leading_chars(_str: str,
                            /,
                            ch: str) -> str:
    """
    Remove leading occurrences of *ch* from the input string, and return the result.

    If the input is not string a string, or *ch* is not a leading character therein, then input is itself returned.

    :param _str: the string to remove leading characters from
    :param ch: leading character to remove
    :return: the input string with leading *chr*s removed
    """
    # declare the return variable
    result: str

    if isinstance(_str, str) and len(_str) > 0:
        result = ""
        for c in _str:
            if len(result) > 0 or c != ch:
                result += c
    else:
        result = _str

    return result


def str_to_lower(_str: str,
                 /) -> str:
    """
    Safely convert the input string to lower-case.

    If the input is not a string, then it is itself returned.

    :param _str: the string to convert to lower-case
    :return: the input string in lower-case, or itself, if is not a string
    """
    return _str.lower() if isinstance(_str, str) else _str


def str_to_upper(_str: str,
                 /) -> str:
    """
    Safely convert the input string to upper-case.

    If the input is not a string, then it is itself returned.

    :param _str: the string to convert to upper-case
    :return: the input string in upper-case, or the input itself, if it is not a string
    """
    return _str.upper() if isinstance(_str, str) else _str


def str_from_any(_str: Any,
                 /) -> str:
    """
    Convert the input string to its string representation.

    These are the string representations returned:
      - *None*: the string 'None'
      - *bool*: the string 'True' of 'False'
      - *str* : the source string itself
      - *bytes*: its hex representation
      - *date*: the date in ISO format (*datetime* is a *date* subtype)
      - *Path*: its POSIX form
      - all other types: their *str()* representation

    :param _str: the data to be converted to string.
    :return: the string representation of the source data
    """
    # declare the return variable
    result: str

    # obtain the string representation
    if isinstance(_str, bytes):
        result = _str.hex()
    elif isinstance(_str, date):
        result = _str.isoformat()
    elif isinstance(_str, Path):
        result = _str.as_posix()
    else:
        result = str(_str)

    return result


def str_to_bool(_str: str,
                /) -> bool | None:
    """
    Obtain and return the *bool* value encoded in the input string.

    These are the criteria:
      - case is disregarded
      - the string values accepted to stand for *True* are *1*, *t*, or *true*
      - the string values accepted to stand for *False* are *0*, *f*, or *false*
      - all other values causes *None* to be returned

    :param _str: the encoded bool value
    :return: the decoded bool value, or *None* if the input string fails the encoding criteria
    """
    # initialize the return variable
    result: bool | None = None

    if _str in ["1", "t", "true"]:
        result = True
    elif _str in ["0", "f", "false"]:
        result = False

    return result


def str_to_int(_str: str,
               /) -> int | None:
    """
    Silently obtain and return the *int* value encoded in the input string.

    :param _str: the encoded int value
    :return: the decoded *int* value, or *None* on error
    """
    # noinspection PyUnusedLocal
    result: int | None = None
    with suppress(Exception):
        result = int(_str)

    return result


def str_in_regex(_str: str,
                 /,
                 regexs: list[str]) -> bool:
    """
    Determine whether the input string matches any of the regular expressions in *regexs*.

    :param _str: the value to match
    :param regexs: list of regular expressions to match
    :return: *True* if a match has been found, *False* otherwise
    """
    # initialize the return variable
    result: bool = False

    if _str and regexs:
        for exp in regexs:
            if re.search(pattern=exp,
                         string=_str):
                result = True
                break

    return result


def str_to_float(_str: str,
                 /) -> float | None:
    """
    Silently obtain and return the *float* value encoded in the input string.

    :param _str: the encoded float value
    :return: the decoded *float* value, or *None* on error
    """
    # noinspection PyUnusedLocal
    result: float | None = None
    with suppress(Exception):
        result = float(_str)

    return result


def str_is_int(_str: str,
               /) -> bool:
    """
    Determine whether the input string encodes a valid positive or negative integer.

    :param _str: the encoded value
    :return: *True* if the input string encodes a valid integer, *False* otherwise
    """
    # declare the return variable
    result: bool

    try:
        int(_str)
        result = True
    except (TypeError, ValueError):
        result = False

    return result


def str_is_float(_str: str,
                 /) -> bool:
    """
    Determine whether the input string encodes a valid positive or negative floating-point number.

    :param _str: the encoded value
    :return: *True* if the input string encodes a valid floating-point number, *False* otherwise
    """
    # declare the return variable
    result: bool

    try:
        float(_str)
        result = True
    except (TypeError, ValueError):
        result = False

    return result


def str_is_hex(_str: str,
               /) -> bool:
    """
    Determine whether the input string encodes a valid hexadecimal integer.

    :param _str: the encoded value
    :return: *True* if the input string encodes a valid hexadecimal number, *False* otherwise
    """
    # declare the return variable
    result: bool

    #  remove the prefix
    if _str.startswith(("0x", "0X")):
        _str = _str[2:]
    try:
        int(_str)
        result = True
    except (TypeError, ValueError):
        result = False

    return result
