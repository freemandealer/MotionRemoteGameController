# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _vXboxInterface
else:
    import _vXboxInterface

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def isVBusExists():
    return _vXboxInterface.isVBusExists()

def GetNumEmptyBusSlots(nSlots):
    return _vXboxInterface.GetNumEmptyBusSlots(nSlots)

def isControllerExists(UserIndex):
    return _vXboxInterface.isControllerExists(UserIndex)

def isControllerOwned(UserIndex):
    return _vXboxInterface.isControllerOwned(UserIndex)

def PlugIn(UserIndex):
    return _vXboxInterface.PlugIn(UserIndex)

def UnPlug(UserIndex):
    return _vXboxInterface.UnPlug(UserIndex)

def UnPlugForce(UserIndex):
    return _vXboxInterface.UnPlugForce(UserIndex)

def SetBtnA(UserIndex, Press):
    return _vXboxInterface.SetBtnA(UserIndex, Press)

def SetBtnB(UserIndex, Press):
    return _vXboxInterface.SetBtnB(UserIndex, Press)

def SetBtnX(UserIndex, Press):
    return _vXboxInterface.SetBtnX(UserIndex, Press)

def SetBtnY(UserIndex, Press):
    return _vXboxInterface.SetBtnY(UserIndex, Press)

def SetBtnStart(UserIndex, Press):
    return _vXboxInterface.SetBtnStart(UserIndex, Press)

def SetBtnBack(UserIndex, Press):
    return _vXboxInterface.SetBtnBack(UserIndex, Press)

def SetBtnLT(UserIndex, Press):
    return _vXboxInterface.SetBtnLT(UserIndex, Press)

def SetBtnRT(UserIndex, Press):
    return _vXboxInterface.SetBtnRT(UserIndex, Press)

def SetBtnLB(UserIndex, Press):
    return _vXboxInterface.SetBtnLB(UserIndex, Press)

def SetBtnRB(UserIndex, Press):
    return _vXboxInterface.SetBtnRB(UserIndex, Press)

def SetBtnGD(UserIndex, Press):
    return _vXboxInterface.SetBtnGD(UserIndex, Press)

def SetTriggerL(UserIndex, Value):
    return _vXboxInterface.SetTriggerL(UserIndex, Value)

def SetTriggerR(UserIndex, Value):
    return _vXboxInterface.SetTriggerR(UserIndex, Value)

def SetAxisX(UserIndex, Value):
    return _vXboxInterface.SetAxisX(UserIndex, Value)

def SetAxisY(UserIndex, Value):
    return _vXboxInterface.SetAxisY(UserIndex, Value)

def SetAxisRx(UserIndex, Value):
    return _vXboxInterface.SetAxisRx(UserIndex, Value)

def SetAxisRy(UserIndex, Value):
    return _vXboxInterface.SetAxisRy(UserIndex, Value)

def SetDpadUp(UserIndex):
    return _vXboxInterface.SetDpadUp(UserIndex)

def SetDpadRight(UserIndex):
    return _vXboxInterface.SetDpadRight(UserIndex)

def SetDpadDown(UserIndex):
    return _vXboxInterface.SetDpadDown(UserIndex)

def SetDpadLeft(UserIndex):
    return _vXboxInterface.SetDpadLeft(UserIndex)

def SetDpadOff(UserIndex):
    return _vXboxInterface.SetDpadOff(UserIndex)

def SetDpad(UserIndex, Value):
    return _vXboxInterface.SetDpad(UserIndex, Value)


