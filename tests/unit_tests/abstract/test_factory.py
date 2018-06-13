import pytest

from abstract.factory import Factory


def test_is_factory_abstract():
    with pytest.raises(TypeError):
        Factory()