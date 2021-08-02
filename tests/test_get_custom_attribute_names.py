from nikmas.utils import get_custom_attribute_names


class Custom:
    def __init__(self):
        self.a = 1
        self.b = "b"
        self.c = ["a", 2]


class TestGetCustomAttributeNames:
    def test_with_custom_class_itself(self):
        assert get_custom_attribute_names(Custom).sort() == ["a", "b", "c"].sort()

    def test_with_custom_class_instance(self):
        assert get_custom_attribute_names(Custom()).sort() == ["a", "b", "c"].sort()
