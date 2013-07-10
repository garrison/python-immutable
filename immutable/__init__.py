_immutable_str = intern("__immutable__")

def immutable(cls):
    try:
        old_init = cls.__init__
    except AttributeError:
        raise TypeError("Class has no '__init__' attribute.  Perhaps it is a python2 old-style class?  Try inheriting from 'object'.")
    old_delattr = cls.__delattr__
    old_setattr = cls.__setattr__

    def new_init(self, *args, **kwargs):
        object.__setattr__(self, _immutable_str, False)
        old_init(self, *args, **kwargs)
        if type(self) is cls:
            self.__immutable__ = True

    def new_delattr(self, name):
        if self.__immutable__:
            raise TypeError("Immutable object")
        else:
            old_delattr(self, name)

    def new_setattr(self, name, value):
        if self.__immutable__:
            raise TypeError("Immutable object")
        else:
            old_setattr(self, name, value)

    cls.__init__ = new_init
    cls.__delattr__ = new_delattr
    cls.__setattr__ = new_setattr

    return cls
