import platform

osname = platform.system()
if osname == 'Darwin':
    from screeninfo import get_monitors
    for m in get_monitors():
        print(str(m))
    #self.listWData.setFont(font)
elif osname == 'Windows':
    import ctypes
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
