import pyautogui
from PIL import Image
import os
import time


#对每张图片截掉最上面的一块区域

for i in range(1, 11):

    path = os.path.join(os.path.dirname(__file__), 'screenshot/', str(i) + '.png')
    image = Image.open(path)
    width, height = image.size
    cropped_image = image.crop((0, 80, width, height))
    cropped_image.save(os.path.join(os.path.dirname(__file__), 'screenshot/', str(i) + '.png'))