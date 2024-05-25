import win32gui

def foreground():
    hwnd = win32gui.FindWindow(None, 'Roblox')
    # windwo = win32gui.FindWindowEx(None, 'Этот компьютер')
    print(hwnd)
    # print(windwo)
    win32gui.SetForegroundWindow(hwnd)

foreground()