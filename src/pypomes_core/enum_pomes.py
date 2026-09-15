from enum import Enum, IntEnum, StrEnum
from typing import Any, Self, TypeVar

# define a TypeVar constrained to IntEnum/StrEnum
IntStrEnum = TypeVar("IntStrEnum", bound=IntEnum | StrEnum)


class EnumUseName(Enum):
    """
    A marker indicating that the attribute *name* should be used in lieu of *value*, when locating an
    instance of this class by looking for a *str* holding its name in lower case. The usual procedure
    would be to look for an occurrence of the enum's *value*. Examples of such usage may be found
    in the *env_pomes* module.
    """


class EnumUseAny(Enum):
    """
    A marker indicating that the attribute *anyval* should be used in lieu of *value*, when locating an
    instance of this class by looking for a *str* holding that attribute's value. The usual procedure
    would be to look for an occurrence of the enum's *value*. Examples of such usage may be found
    in the *env_pomes* module. Note that this marker is restricted to subclasses of *EnumAny*,
    and should not be used simultaneously with marker *EnumUseName*.
    """


class EnumAny(Enum):
    """
    Adds the attribute *anyval*, of type *Any*, to subclasses of *Enum*.
    """

    def __new__(cls: type[Self],
                value: Any,
                anyval: Any) -> Self:
        """
        Allow for the creation of subclasses of *Enum* having the extra *anyval* attribute.

        The following are examples of creating the class *MyArgument* with 3 instances:
        ::
            statically:
            class MyArgument(EnumAny):
                DEF_INT = (0, int)
                DEF_STR = ("", str)
                DEF_LIST = ([], list)

            dynamically:
            MyArgument = StrEnumAny("MyArgument", {
                                    "DEF_INT": (0, int),
                                    "DEF_STR": ("", str),
                                    "DEF_LIST": ([], list)
                                    })

        :param value: value to be assigned to the instance
        :param anyval: extra information to be assigned to the instance
        """
        result: Self = object.__new__(cls)
        result._value_ = value
        result.anyval: Any = anyval

        return result

    @classmethod
    def from_name(cls: type[Self],
                  v: str,
                  /) -> EnumAny | None:
        """
        Retrieve the instance having its *name* attribute equal to *v*.

        This is a convenience alternative to *enum-class[v]*, preventing the runtime error "KeyError: '<v>'".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        return cls[v] if v in [member.name for member in cls] else None

    @classmethod
    def from_value(cls: type[Self],
                   v: Any,
                   /) -> EnumAny | None:
        """
        Retrieve the instance having its *value* attribute equal to *v*.

        This is a convenience alternative to *enum-class(v)*, using a perfect comparison operation,
        and preventing the runtime error "'<v>' is not a valid <EnumAny>".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: EnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.value) is type(v)) and (member.value == v):
                result = member
                break

        return result

    @classmethod
    def from_anyval(cls: type[Self],
                    v: Any,
                    /) -> EnumAny | None:
        """
        Retrieve the instance having the attribute *anyval* equal to *v*.

        :param v: the value to search for
        :return: the instance whose *anyval* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: EnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.anyval) is type(v)) and (member.anyval == v):
                result = member
                break

        return result


class IntEnumAny(IntEnum):
    """
     Adds the attribute *anyval*, of type *Any*, to subclasses of *IntEnum*.
    """

    def __new__(cls: type[Self],
                value: int,
                anyval: Any) -> Self:
        """
        Allow for the creation of subclasses of *IntEnum* having the extra *anyval* attribute.

        The following are examples of creating the class *Status* with 3 instances:
        ::
            statically:
            class Status(IntEnumAny):
                ACTIVE = (1, "C1")
                INACTIVE = (0, "C2")
                DELETED = (-1, "C3")

            dynamically:
            Status = IntEnumAny("Status", {
                                 "ACTIVE": (1, "C1"),
                                 "INACTIVE": (0, "C2"),
                                 "DELETED": (-1, "C3")
                                 })

        :param value: value to be assigned to the instance
        :param anyval: extra information to be assigned to the instance
        """
        result: Self = int.__new__(cls,
                                   value)
        result._value_ = value
        result.anyval: Any = anyval

        return result

    @classmethod
    def from_name(cls: type[Self],
                  v: str,
                  /) -> IntEnumAny | None:
        """
        Retrieve the instance having its *name* attribute equal to *v*.

        This is a convenience alternative to *enum-class[v]*, preventing the runtime error "KeyError: '<v>'".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        return cls[v] if v in [member.name for member in cls] else None

    @classmethod
    def from_value(cls: type[Self],
                   v: Any,
                   /) -> IntEnumAny | None:
        """
        Retrieve the instance having its *value* attribute equal to *v*.

        This is a convenience alternative to *enum-class(v)*, using a perfect comparison operation,
        and preventing the runtime error "'<v>' is not a valid <EnumAny>".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: EnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.value) is type(v)) and (member.value == v):
                result = member
                break

        return result

    @classmethod
    def from_anyval(cls: type[Self],
                    v: Any,
                    /) -> IntEnumAny | None:
        """
        Retrieve the instance having the attribute *anyval* equal to *v*.

        :param v: the value to search for
        :return: the instance whose *anyval* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: IntEnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.anyval) is type(v)) and (member.anyval == v):
                result = member
                break

        return result


class IntEnumDesc(IntEnum):
    """
     Adds the attribute *desc*, of type *str*, to subclasses of *IntEnum*.
    """

    def __new__(cls: type[Self],
                value: int,
                desc: str) -> Self:
        """
        Allow for the creation of subclasses of *IntEnum* having the extra *desc* attribute.

        The following are examples of creating the class *Status* with 3 instances:
        ::
            statically:
            class Status(IntEnumDesc):
                ACTIVE = (1, "Item is currently active")
                INACTIVE = (0, "Item is currently inactive")
                DELETED = (-1, "Item has been removed")

            dynamically:
            Status = IntEnumDesc("Status", {
                                 "ACTIVE": (1, "Item is currently active"),
                                 "INACTIVE": (0, "Item is currently inactive"),
                                 "DELETED": (-1, "Item has been removed")
                                 })

        :param value: value to be assigned to the instance
        :param desc: description to be assigned to the instance
        """
        result: Self = int.__new__(cls,
                                   value)
        result._value_ = value
        result.desc: str = desc

        return result

    @classmethod
    def from_name(cls: type[Self],
                  v: str,
                  /) -> IntEnumDesc | None:
        """
        Retrieve the instance having its *name* attribute equal to *v*.

        This is a convenience alternative to *enum-class[v]*, preventing the runtime error "KeyError: '<v>'".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        return cls[v] if v in [member.name for member in cls] else None

    @classmethod
    def from_value(cls: type[Self],
                   v: Any,
                   /) -> IntEnumDesc | None:
        """
        Retrieve the instance having its *value* attribute equal to *v*.

        This is a convenience alternative to *enum-class(v)*, using a perfect comparison operation,
        and preventing the runtime error "'<v>' is not a valid <EnumAny>".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: EnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.value) is type(v)) and (member.value == v):
                result = member
                break

        return result

    @classmethod
    def from_desc(cls: type[Self],
                  v: str,
                  /) -> IntEnumDesc | None:
        """
        Retrieve the instance having the attribute *desc* equal to *v*.

        :param v: the value to search for
        :return: the instance whose *desc* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: IntEnumDesc | None = None

        # traverse the class
        for member in cls:
            if member.desc == v:
                result = member
                break

        return result


class IntEnumDescAny(IntEnumDesc, IntEnumAny):
    """
     Adds the attributes *desc* and *anyval*, respectively of types *str* and *Any*, to subclasses of *IntEnum*.
    """

    def __new__(cls: type[Self],
                value: int,
                desc: str,
                anyval: Any) -> Self:
        """
        Allow for the creation of subclasses of *IntEnum* having the extra *desc* and *anyval* attributes.

        The following are examples of creating the class *Status* with 3 instances:
        ::
            statically:
            class Status(IntEnumDescAny):
                ACTIVE = (1, "Item is currently active", "C1")
                INACTIVE = (0, "Item is currently inactive", "C2")
                DELETED = (-1, "Item has been removed", "C3")

            dynamically:
            Status = IntEnumDescAny("Status", {
                                    "ACTIVE": (1, "Item is currently active", "C1"),
                                    "INACTIVE": (0, "Item is currently inactive", "C2"),
                                    "DELETED": (-1, "Item has been removed", "C3")
                                   })

        :param value: value to be assigned to the instance
        :param desc: description to be assigned to the instance
        :param anyval: extra information to be assigned to the instance
        """
        result: Self = int.__new__(cls,
                                   value)
        result._value_ = value
        result.desc: str = desc
        result.anyval: Any = anyval

        return result

    @classmethod
    def from_anyval(cls: type[Self],
                    v: Any,
                    /) -> IntEnumDescAny | None:
        """
        Retrieve the instance having the attribute *anyval* equal to *v*.

        :param v: the value to search for
        :return: the instance whose *anyval* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: IntEnumDescAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.anyval) is type(v)) and (member.anyval == v):
                result = member
                break

        return result


class StrEnumAny(StrEnum):
    """
    Adds the attribute *anyval*, of type *Any*, to subclasses of *StrEnum*.
    """

    def __new__(cls: type[Self],
                value: str,
                anyval: Any) -> Self:
        """
        Allow for the creation of subclasses of *StrEnum* having the extra *anyval* attribute.

        The following are examples of creating the class *Status* with 3 instances:
        ::
            statically:
            class Status(StrEnumAny):
                ACTIVE = ("active", "C1")
                INACTIVE = ("inactive", "C2")
                DELETED = ("deleted", "C3")

            dynamically:
            Status = StrEnumAny("Status", {
                                 "ACTIVE": ("active", "C1"),
                                 "INACTIVE": ("inactive", "C2"),
                                 "DELETED": ("deleted", "C3")
                                 })

        :param value: value to be assigned to the instance
        :param anyval: extra information to be assigned to the instance
        """
        result: Self = str.__new__(cls,
                                   object=value)
        result._value_ = value
        result.anyval: Any = anyval

        return result

    @classmethod
    def from_name(cls: type[Self],
                  v: str,
                  /) -> StrEnumAny | None:
        """
        Retrieve the instance having its *name* attribute equal to *v*.

        This is a convenience alternative to *enum-class[v]*, preventing the runtime error "KeyError: '<v>'".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        return cls[v] if v in [member.name for member in cls] else None

    @classmethod
    def from_value(cls: type[Self],
                   v: Any,
                   /) -> StrEnumAny | None:
        """
        Retrieve the instance having its *value* attribute equal to *v*.

        This is a convenience alternative to *enum-class(v)*, using a perfect comparison operation,
        and preventing the runtime error "'<v>' is not a valid <EnumAny>".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: EnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.value) is type(v)) and (member.value == v):
                result = member
                break

        return result

    @classmethod
    def from_anyval(cls: type[Self],
                    v: Any,
                    /) -> StrEnumAny | None:
        """
        Retrieve the instance having the attribute *anyval* equal to *v*.

        :param v: the value to search for
        :return: the instance whose *anyval* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: StrEnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.anyval) is type(v)) and (member.anyval == v):
                result = member
                break

        return result


class StrEnumDesc(StrEnum):
    """
     Adds the attribute *desc*, of type *str*, to subclasses of *StrEnum*.
    """

    def __new__(cls: type[Self],
                value: str,
                desc: str) -> Self:
        """
        Allow for the creation of subclasses of *StrEnum* having the extra *desc* attribute.

        The following are examples of creating the class *Status* with 3 instances:
        ::
            statically:
            class Status(StrEnumDesc):
                ACTIVE = ("active", "Item is currently active")
                INACTIVE = ("inactive", "Item is currently inactive")
                DELETED = ("deleted", "Item has been removed")

            dynamically:
            Status = StrEnumDesc("Status", {
                                 "ACTIVE": ("active", "Item is currently active"),
                                 "INACTIVE": ("inactive", "Item is currently inactive"),
                                 "DELETED": ("deleted", "Item has been removed")
                                 })

        :param value: value to be assigned to the instance
        :param desc: description to be assigned to the instance
        """
        result: Self = str.__new__(cls,
                                   object=value)
        result._value_ = value
        result.desc: str = desc

        return result

    @classmethod
    def from_name(cls: type[Self],
                  v: str,
                  /) -> StrEnumDesc | None:
        """
        Retrieve the instance having its *name* attribute equal to *v*.

        This is a convenience alternative to *enum-class[v]*, preventing the runtime error "KeyError: '<v>'".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        return cls[v] if v in [member.name for member in cls] else None

    @classmethod
    def from_value(cls: type[Self],
                   v: Any,
                   /) -> StrEnumDesc | None:
        """
        Retrieve the instance having its *value* attribute equal to *v*.

        This is a convenience alternative to *enum-class(v)*, using a perfect comparison operation,
        and preventing the runtime error "'<v>' is not a valid <EnumAny>".

        :param v: the value to search for
        :return: the instance whose *name* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: EnumAny | None = None

        # traverse the class
        for member in cls:
            if (type(member.value) is type(v)) and (member.value == v):
                result = member
                break

        return result

    @classmethod
    def from_desc(cls: type[Self],
                  v: str,
                  /) -> StrEnumDesc | None:
        """
        Retrieve the instance having the attribute *desc* equal to *v*.

        :param v: the value to search for
        :return: the instance whose *desc* attribute matches *v*, or *None* if not found
        """
        # initialize the return variable
        result: StrEnumDesc | None = None

        # traverse the class
        for member in cls:
            if member.desc == v:
                result = member
                break

        return result


class StrEnumDescAny(StrEnumDesc, StrEnumAny):
    """
    Adds the attributes *desc* and *anyval* (of types *str* and *Any*, respectively), to subclasses of *StrEnum*.
    """

    def __new__(cls: type[Self],
                value: str,
                desc: str,
                anyval: Any) -> Self:
        """
        Allow for the creation of subclasses of *StrEnum* having the extra *desc* and *anyval* attributes
        (respectively of types *str* and *Any*),.

        The following are examples of creating the class *Status* with 3 instances:
        ::
            statically:
            class Status(StrEnumDescAny):
                ACTIVE = ("active", "Item is currently active", "C1")
                INACTIVE = ("inactive", "Item is currently inactive", "C2")
                DELETED = ("deleted", "Item has been removed", "C3")

            dynamically:
            Status = StrEnumDescAny("Status", {
                                    "ACTIVE": ("active", "Item is currently active", "C1"),
                                    "INACTIVE": ("inactive", "Item is currently inactive", "C2"),
                                    "DELETED": ("deleted", "Item has been removed", "C3")
                                    })

        :param value: value to be assigned to the instance
        :param desc: description to be assigned to the instance
        :param anyval: extra information to be assigned to the instance
        """
        result: Self = str.__new__(cls,
                                   object=value)
        result._value_ = value
        result.desc: str = desc
        result.anyval: Any = anyval

        return result
