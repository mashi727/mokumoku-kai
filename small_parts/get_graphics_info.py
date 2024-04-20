import platform



osname = platform.system()

def get_screensize():
    if osname == 'Darwin':
        from screeninfo import get_monitors
        for monitor in get_monitors():
            width = monitor.width
            height = monitor.height
        return width, height
    elif osname == 'Windows':
        import ctypes
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        return screensize[0], screensize[1])

print(get_screensize())
