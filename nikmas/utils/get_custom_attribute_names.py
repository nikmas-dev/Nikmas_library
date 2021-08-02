from typing import Any
import inspect


def get_custom_attribute_names(class_: Any) -> list[str]:
    """
    Retrieves custom class attribute names from the given class.
    Works properly only with custom classes with class attributes.

    :param class_: Any instance or class object itself.
    :return: List of attribute names.
    """
    attribute_names = []

    for i in dir(class_):
        if not i.startswith("_"):
            if not inspect.ismethod(i):
                attribute_names.append(i)

    return attribute_names
