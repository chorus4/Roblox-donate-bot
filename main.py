import psutil
import win32api
import win32process

from ram import RAM
import time
import win32gui
import win32con
from pywinauto import Application
import pyautogui
import pydirectinput
import win32process as wproc
import win32api as wapi

jobId = 8737602449
timeForStart = 5
windows_accounts = []

x = 1250
y = 1405

while True:
    try:
        window = win32gui.FindWindow(None, 'Roblox')
        print(window)
        win32gui.PostMessage(window,win32con.WM_CLOSE,0,0)
        if window == 0: break
        time.sleep(1)
    except Exception:
        break


ram = RAM()
accounts = ram.getAccounts()

def press_alt_tab():
    pydirectinput.keyDown('alt')
    time.sleep(.2)
    pydirectinput.press('tab')
    time.sleep(.2)
    pydirectinput.keyUp('alt')
def move(x, y):
    win32api.SetCursorPos((x,y))

# for account in accounts:
#     ram.launchAccount(account, jobId)
#     time.sleep(timeForStart)
#     windowId = win32gui.FindWindow(None, 'Roblox')
#     # win32gui.SetForegroundWindow(windowId)
#     print(windowId)
#     windows_accounts.append({'account': account, 'windowId': windowId})

ramId = Application().connect(title="Этот компьютер")
window = ramId.window(title="Этот компьютер")
print(ramId)

ram.launchAccount(accounts[0], jobId)
time.sleep(timeForStart)
windows_accounts.append({'windowId': win32gui.FindWindow(None, 'Roblox')})
print(windows_accounts)

# for window in windows_accounts:
#     time.sleep(2)
#     win32gui.SetForegroundWindow(window['windowId'])
#     print(window['windowId'])
#     time.sleep(2)
#     win32gui.SetForegroundWindow(ramId)

time.sleep(2)
window.set_focus()
time.sleep(2)
win32gui.SetForegroundWindow(windows_accounts[0]['windowId'])
time.sleep(2)
# press_alt_tab()
move(x, y)
# pyautogui.hotkey("ctrl", "shift", "esc")
# win32gui.SendMessage(windows_accounts[0]['windowId'], win32con.WM_SYSCOMMAND, win32con.SC_MINIMIZE, 0)
# print(window['windowId'])
# win32gui.SetForegroundWindow(ramId)

# time.sleep(5)
# win32gui.SetForegroundWindow(windows_accounts[1]['windowId'])