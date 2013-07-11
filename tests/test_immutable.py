from pytest import raises

from immutable import immutable_object, immutable_type

def test_basic():
    class Something(immutable_object):
        def __init__(self):
            self.x = 3

    o = Something()
    assert o.x == 3
    with raises(TypeError):
        o.x = 4
    with raises(TypeError):
        o.y = 5
    with raises(TypeError):
        del o.x

def test_empty_class():
    class EmptyClass(immutable_object):
        pass

    x = EmptyClass()
    with raises(TypeError):
        del x.x

def test_slots():
    class SlottedImmutable(immutable_object):
        __slots__ = ("__immutable__", "slot1")

        def __init__(self):
            self.slot1 = 1

    x = SlottedImmutable()
    with raises(TypeError):
        x.slot1 = 4

def test_inheritance():
    class BaseClass(immutable_object):
        def __init__(self, x):
            self.x = x

    class ChildClass(BaseClass):
        def __init__(self, x, y, z):
            self.y = y
            super(ChildClass, self).__init__(x)
            self.z = z

    o = ChildClass(1, 2, 3)
    with raises(TypeError):
        o.x = 10
    with raises(TypeError):
        o.y = 10
    with raises(TypeError):
        o.z = 10

def test_six_metaclass():
    from six import with_metaclass

    class Something(with_metaclass(immutable_type)):
        pass

    o = Something()
    with raises(TypeError):
        o.x = 20

def test_six_custom_metaclass():
    from six import with_metaclass

    class CustomMetaclass(immutable_type):
        pass

    class Something(with_metaclass(CustomMetaclass)):
        pass

    o = Something()
    with raises(TypeError):
        o.x = 20
