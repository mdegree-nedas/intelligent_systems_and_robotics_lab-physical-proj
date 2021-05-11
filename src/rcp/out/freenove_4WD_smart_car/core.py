# rcp: CORE MODULE
# rcp: auto-generated ros foreign interface file
# rcp: do not edit this file

from types import FunctionType


class Freenove_4wd_smart_car:
    def __init__(self):
        self.sensors = _Sensors()
        self.actuators = _Actuators()


class _Sensors:
    def __init__(self):
        self.topic = "sensors_topic"
        self.ultrasound = _Ultrasound()
        self.lightsensor = _Lightsensor()
        self.linetracker = _Linetracker()


class _Ultrasound:
    def __init__(self):
        self.id = None
        self.type = None
        self.address = None
        self.data = None

    def read(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()


class _Lightsensor:
    def __init__(self):
        self.id = None
        self.type = None
        self.address = None
        self.data = None

    def read(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()


class _Linetracker:
    def __init__(self):
        self.id = None
        self.type = None
        self.address = None
        self.data = None

    def read(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()


class _Actuators:
    def __init__(self):
        self.topic = "actuators_topic"
        self.motion = _Motion()
        self.led = _Led()


class _Motion:
    def __init__(self):
        self.id = None
        self.address = None
        self.commands = _MotionCommands()


class _MotionCommands:
    def go_forward(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def go_backward(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def turn_left(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def turn_right(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def action_atomic(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def action_indefinite(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def action_durative_no_data(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def action_durative(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()


class _Led:
    def __init__(self):
        self.id = None
        self.address = None
        self.commands = _LedCommands()


class _LedCommands:
    def switch_on(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()

    def switch_off(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()
