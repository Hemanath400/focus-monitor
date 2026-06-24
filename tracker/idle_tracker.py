import ctypes
from ctypes import Structure, c_uint, sizeof, byref


class LASTINPUTINFO(Structure):

    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint)
    ]


def get_idle_duration():

    last_input = LASTINPUTINFO()

    last_input.cbSize = sizeof(last_input)

    ctypes.windll.user32.GetLastInputInfo(
        byref(last_input)
    )

    millis = (
        ctypes.windll.kernel32.GetTickCount()
        - last_input.dwTime
    )

    return millis / 1000