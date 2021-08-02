# Nikmas' library

Collection of useful utils for python projects.

## Installation

```
pip install nikmas
```

## Get started

### Get all custom class attribute names

```Python
from nikmas.utils import get_custom_attribute_names


class Custom:
    a = 1
    b = 2
    c = 3


attrs_from_class_object_itself = get_custom_attribute_names(Custom)
# result -> ["a", "b", "c"]

instance = Custom()
attrs_from_class_instance = get_custom_attribute_names(instance)
# result -> ["a", "b", "c"]
```
