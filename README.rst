python-immutable
================

Immutable objects in python.

Rationale
---------

(coming soon)

Usage
-----

    from immutable import immutable_object

    class MyClass(immutable_object):
        def __init__(self, x):
            self.x = x

    mc = MyClass(3)
    print(mc.x)

    mc.x = 2  # raises TypeError
    del mc.x  # raises TypeError
    mc.y = 3  # raises TypeError
