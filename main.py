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
time.sleep(5)


xMargin = 10
yMargin = 100

moveTime = 1
xDragTime = 6
yDragTime = 4

# 第一行 0-9 
for i in range(10):
    pyautogui.moveTo(xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(sizex-xMargin, yMargin, duration=xDragTime, button='left')
    image = pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin))) # left, upper, right, lower
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i) + '.png')
    cropped_image.save(path)
    time.sleep(1)


# 10
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '10.png')
cropped_image.save(path)


# 第二行 11-19
for i in range(9):
    pyautogui.moveTo(sizex-xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(xMargin, yMargin, duration=xDragTime, button='left')
    image =  pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i+11) + '.png')
    cropped_image.save(path)
    time.sleep(1)

#20
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '20.png')
cropped_image.save(path)

# 第三行 21-29
for i in range(9):
    pyautogui.moveTo(xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(sizex-xMargin, yMargin, duration=xDragTime, button='left')
    #每个图片大小都是1439*860大小
    image = pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin))) # left, upper, right, lower
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i + 21) + '.png')
    cropped_image.save(path)
    time.sleep(1)

#30
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '30.png')
cropped_image.save(path)

#第四行 31-39
for i in range(9):
    pyautogui.moveTo(sizex-xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(xMargin, yMargin, duration=xDragTime, button='left')
    image =  pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i+31) + '.png')
    cropped_image.save(path)
    time.sleep(1)
#40
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '40.png')
cropped_image.save(path)

#第五行 41-49
for i in range(9):
    pyautogui.moveTo(xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(sizex-xMargin, yMargin, duration=xDragTime, button='left')
    #每个图片大小都是1439*860大小
    image = pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin))) # left, upper, right, lower
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i + 41) + '.png')
    cropped_image.save(path)
    time.sleep(1)

# 50
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '50.png')
cropped_image.save(path)

#第六行 51-59
for i in range(9):
    pyautogui.moveTo(sizex-xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(xMargin, yMargin, duration=xDragTime, button='left')
    image =  pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i+51) + '.png')
    cropped_image.save(path)
    time.sleep(1)
# 60
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '60.png')
cropped_image.save(path)

#第七行 61-69
for i in range(9):
    pyautogui.moveTo(xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(sizex-xMargin, yMargin, duration=xDragTime, button='left')
    #每个图片大小都是1439*860大小
    image = pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin))) # left, upper, right, lower
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i + 61) + '.png')
    cropped_image.save(path)
    time.sleep(1)

#70
pyautogui.moveTo(xMargin, sizey-yMargin, duration=moveTime)
pyautogui.dragTo(xMargin, yMargin, duration=yDragTime, button='left')
image =  pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '70.png')
cropped_image.save(path)

# 第八行 71-79
for i in range(9):
    pyautogui.moveTo(sizex-xMargin, yMargin, duration=moveTime)
    pyautogui.dragTo(xMargin, yMargin, duration=xDragTime, button='left')
    image =  pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i+71) + '.png')
    cropped_image.save(path)
    time.sleep(1)

#拼接成大图片
image_test = Image.open(os.path.dirname(__file__) + '/screenshot/0.png')
each_width = image_test.width
total_width = each_width * 10
each_height = image_test.height
total_height = each_height * 8
print(total_width, total_height)


big_image = Image.new('RGB', (total_width, total_height))

x_offset = 0
y_offset = 0

for i in range(8):
    if i % 2 == 0:
        for j in range(10):
            image = Image.open(os.path.dirname(__file__) + '/screenshot/' + str(i*10 + 9 - j) + '.png')
            big_image.paste(image, (x_offset, y_offset))
            x_offset += each_width
        y_offset += each_height
        x_offset = 0
    else:
        for j in range(10):
            image = Image.open(os.path.dirname(__file__) + '/screenshot/' + str(i*10 + j) + '.png')
            big_image.paste(image, (x_offset, y_offset))
            x_offset += each_width
        y_offset += each_height
        x_offset = 0

big_image.save(os.path.dirname(__file__) + '/screenshot/bigImage.png')
