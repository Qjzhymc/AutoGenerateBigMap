import pyautogui
from PIL import Image
import os
import time

# 将所有图片拼成一个大图片


image_test = Image.open(os.path.dirname(__file__) + '/screenshot/4.png')
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

image6 = Image.open(os.path.dirname(__file__) + '/screenshot/6.png')
big_image.paste(image6, (x_offset, y_offset))
x_offset += each_width

image7 = Image.open(os.path.dirname(__file__) + '/screenshot/7.png')
big_image.paste(image7, (x_offset, y_offset))
x_offset += each_width

image8 = Image.open(os.path.dirname(__file__) + '/screenshot/8.png')
big_image.paste(image8, (x_offset, y_offset))
x_offset += each_width

image9 = Image.open(os.path.dirname(__file__) + '/screenshot/9.png')
big_image.paste(image9, (x_offset, y_offset))
x_offset += each_width



big_image.save(os.path.dirname(__file__) + '/screenshot/bigImage.png')
