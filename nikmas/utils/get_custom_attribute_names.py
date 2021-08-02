from typing import Any
import inspect


def get_custom_attribute_names(class_: Any) -> list[str]:
    """
    Retrieves custom attribute names from the given class. Works properly only with custom classes, not built-in types.

    :param class_: Any instance or class object itself.
    :return: List of attribute names.
    """
    attribute_names = []

    for i in inspect.getmembers(class_):
        if not i[0].startswith('_'):
            if not inspect.ismethod(i[1]):
                attribute_names.append(i[0])

    return attribute_names
