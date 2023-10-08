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

xMargin = 10
yMargin = 100

# 从左向右移
for i in range(5):
    pyautogui.moveTo(xMargin, yMargin, duration=2)
    pyautogui.dragTo(sizex-xMargin, yMargin, duration=6, button='left')
    #每个图片大小都是1439*860大小
    image = pyautogui.screenshot()
    cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin))) # left, upper, right, lower
    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i) + '.png')
    cropped_image.save(path)
    time.sleep(2)

#到达了整个大图的最左边，向下移一个
pyautogui.moveTo(xMargin, sizey-yMargin, duration=2)
pyautogui.dragTo(xMargin, yMargin, duration=4, button='left')
image = pyautogui.screenshot()
cropped_image = image.crop((2*xMargin, 2*yMargin, 2*(sizex-xMargin), 2*(sizey-yMargin)))
path = os.path.join(os.path.dirname(__file__), 'screenshot/', '5.png')
cropped_image.save(path)
time.sleep(2)

#拼接成大图片
image_test = Image.open(os.path.dirname(__file__) + '/screenshot/3.png')
each_width = image_test.width
total_width = each_width * 5
each_height = image_test.height
total_height = each_height * 2
print(total_width, total_height)


big_image = Image.new('RGB', (total_width, total_height))

x_offset = 0
y_offset = 0

image4 = Image.open(os.path.dirname(__file__) + '/screenshot/4.png')
big_image.paste(image4, (x_offset, 0))
x_offset += each_width

image3 = Image.open(os.path.dirname(__file__) + '/screenshot/3.png')
big_image.paste(image3, (x_offset, 0))
x_offset += each_width

image2 = Image.open(os.path.dirname(__file__) + '/screenshot/2.png')
big_image.paste(image2, (x_offset, 0))
x_offset += each_width

image1 = Image.open(os.path.dirname(__file__) + '/screenshot/1.png')
big_image.paste(image1, (x_offset, 0))
x_offset += each_width

image0 = Image.open(os.path.dirname(__file__) + '/screenshot/0.png')
big_image.paste(image0, (x_offset, 0))
x_offset += each_width


#  第二排
x_offset = 0
y_offset += each_height
image5 = Image.open(os.path.dirname(__file__) + '/screenshot/5.png')
big_image.paste(image5, (x_offset, y_offset))
x_offset += each_width

# image6 = Image.open(os.path.dirname(__file__) + '/screenshot/6.png')
# big_image.paste(image6, (x_offset, y_offset))
# x_offset += each_width

# image7 = Image.open(os.path.dirname(__file__) + '/screenshot/7.png')
# big_image.paste(image7, (x_offset, y_offset))
# x_offset += each_width

# image8 = Image.open(os.path.dirname(__file__) + '/screenshot/8.png')
# big_image.paste(image8, (x_offset, y_offset))
# x_offset += each_width

# image9 = Image.open(os.path.dirname(__file__) + '/screenshot/9.png')
# big_image.paste(image9, (x_offset, y_offset))
# x_offset += each_width



big_image.save(os.path.dirname(__file__) + '/screenshot/bigImage.png')
