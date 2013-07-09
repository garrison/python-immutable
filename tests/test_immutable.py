from pytest import raises

from immutable import immutable

def test_basic():
    @immutable
    class Something(object):
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
    @immutable
    class EmptyClass(object):
        pass

    x = EmptyClass()
    with raises(TypeError):
        del x.x

def test_old_style_class():
    from sys import version_info
    if version_info[0] == 2:
        with raises(TypeError):
            @immutable
            class OldStyle:
                pass

def test_slots():
    @immutable
    class SlottedImmutable(object):
        __slots__ = ("__immutable__", "slot1")

        def __init__(self):
            self.slot1 = 1

    x = SlottedImmutable()
    with raises(TypeError):
        x.slot1 = 4

def test_inheritance():
    @immutable
    class BaseClass(object):
        def __init__(self, x):
            self.x = x

    @immutable
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

def test_undecorated_inheritance():
    @immutable
    class BaseClass(object):
        def __init__(self, x):
            self.x = x

    @immutable # fixme: remove this line and get it to work in a sane way
    class ChildClass(BaseClass):
        def __init__(self, x, y, z):
            self.y = y
            super(ChildClass, self).__init__(x)
            self.z = z

    o = ChildClass(1, 2, 3)
