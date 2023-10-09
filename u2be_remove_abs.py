import cv2
import pyautogui
import pygetwindow
import time
from PIL import Image
import numpy as np
import pyscreenshot as ImageGrab

def 切換至目標視窗():
    # 視窗標題或部分標題（不區分大小寫），用來指定特定視窗
    target_window_title = "chrome"

    # 取得符合標題的視窗
    target_window = pygetwindow.getWindowsWithTitle(target_window_title)

    # 如果找到了目標視窗
    if target_window:
        target_window = target_window[0]  # 取得第一個符合標題的視窗
        target_window.activate()  # 切換至目標視窗

    else:
        print(f"找不到標題包含 '{target_window_title}' 的視窗。")

def removeAdsBar():

    # 定义怪物图像文件的路径
    bar_path = Image.open('ads_pass_286x106px.png')
    # 定義模糊比對參數
    confidence_threshold = 0.6
    # 搜索廣告按扭图像
    bar_a_location = pyautogui.locateOnScreen(bar_path, grayscale=True, confidence=confidence_threshold)
    print(f"廣告按扭 at ", bar_a_location)
    # 如果找到廣告按扭

    if bar_a_location is not None:
        # 点击廣告按扭图像
        a_x, a_y = pyautogui.center(bar_a_location)
        pyautogui.moveTo(a_x, a_y, 1, pyautogui.easeInOutQuad)
        pyautogui.mouseDown()
        time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题
        pyautogui.mouseUp()
        # print(f"廣告按扭。pressed", a_x, a_y)
        print(f"廣告按扭。pressed", a_x, a_y )
        time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题
    else:
        print(f"找不到廣告按扭。")

# 停止程序报错；
pyautogui.FAILSAFE =False
# 切換至目標視窗()
print(f"显示器的分辨率", pyautogui.size())   # 返回所用显示器的分辨率； 输出：Size(width=1920, height=1080)
pyautogui.PAUSE = 3
while True:
    #  当前鼠标的坐标
    print(f"当前鼠标的坐标", pyautogui.position())
    # 切換至目標視窗()
    removeAdsBar()
    pyautogui.PAUSE = 1