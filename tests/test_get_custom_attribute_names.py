from nikmas.utils import get_custom_attribute_names


class Custom:
    a = 1
    b = "b"
    c = ["a", 2]


class TestGetCustomAttributeNames:
    def test_with_custom_class_itself(self):
        assert sorted(get_custom_attribute_names(Custom)) == ["a", "b", "c"]

    def test_with_custom_class_instance(self):
        assert sorted(get_custom_attribute_names(Custom())) == ["a", "b", "c"]
