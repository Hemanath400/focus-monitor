import win32gui


def get_active_window_title():
    """
    Returns title of currently active window
    """
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)