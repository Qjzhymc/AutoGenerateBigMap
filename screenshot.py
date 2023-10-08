import pyautogui
from PIL import Image
import os
import time
# Size(width=1440, height=900)
# 左上角是（0，0），向右是x轴ui，向下是y轴
sizex, sizey = pyautogui.size() 
#获取鼠标当前位置
b = pyautogui.position()
print(b)
#1.运行后先等待5秒，进入地图gui
time.sleep(3)
#2.鼠标移动到左上角

# 从左向右移
for i in range(10):
    pyautogui.moveTo(1, 40, duration=2)
    pyautogui.dragTo(1440, 40, duration=6, button='left')
    #每个图片大小都是1439*860大小
    image = pyautogui.screenshot('1.png',region=(1,40,1439,860))
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i) + '.png')
    image.save(path)
    time.sleep(2)

#到达了整个大图的最左边，向下移一个

pyautogui.moveTo(500, 898, duration=2)
pyautogui.dragTo(500, 40, duration=4, button='left')
image = pyautogui.screenshot('1.png',region=(1,40,1439,860))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '10.png')
image.save(path)
time.sleep(2)

# 从右向左移
for i in range(9):
    pyautogui.moveTo(1438, 40, duration=2)
    pyautogui.dragTo(1, 40, duration=6, button='left')
    #每个图片大小都是1439*860大小
    image = pyautogui.screenshot('1.png',region=(1,40,1439,860))
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i+11) + '.png')
    image.save(path)
    time.sleep(2)




