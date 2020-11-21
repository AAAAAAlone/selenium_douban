#!/usr/bin/python
# -*- coding: UTF-8 -*-
# from PIL import Image
# from pytesseract import *

# image = Image.open('test2.jpeg')
# text = image_to_string(image)
# print(text)

import cv2
from PIL import Image
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from string import punctuation
import os


class Code_Ocr(object):

    def __init__(self):
        self.orc_start()

    def orc_start(self):

        img = Image.open('code-douban.jpeg')
        img.show()
        # img = Image.open(
        #     r'/Users/oscar/Downloads/selenium_douban/selenium_robot/code-douban.jpeg')
        img = img.convert('RGB')
        # 二值化去除背景
        img_clear_bg = self.img_clear(img)
        # 灰度非邻降噪
        img_gray = self.noise_remove_pil(img_clear_bg, 1)
        # 二值化降噪
        img_jiangzao = self.jiangzao(img_gray)
        # orc
        text = self.pytesseract_ocr(img_jiangzao)
        self.removePunctuation(text)
        return text

    def text_ocr(self, img, k,):
        img_clear_bg = self.img_clear(img)
        img_gray = self.noise_remove_pil(img_clear_bg, 1)
        text = self.pytesseract_ocr(img_gray)

        return text

    def img_clear(self, img):
        width, height = img.size
        threshold = 20
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        for i in range(0, width):
            for j in range(0, height):
                p = img.getpixel((i, j))  # 抽取坐标（i,j）出像素点的RGB颜色值
                # print(p)#(255, 255, 255, 255)
                r = p[0]
                g = p[1]
                b = p[2]
                # a = p[3]
                # r, g, b, a = p
                if r > threshold or g > threshold or b > threshold:
                    # 设置坐标（i,j）处像素点的RGB颜色值为（255.255.255）
                    img.putpixel((i, j), WHITE)
                else:
                    img.putpixel((i, j), BLACK)
        # print('二值化去除背景色')
        img.show()
        image_name = "clear_bg.jpg"
        img.save(image_name)
        return img

    def pytesseract_ocr(self, img):
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'

        # img = Image.open('test.jpeg')
        # text = pytesseract.image_to_string(img,lang='chi_sim')
        text = pytesseract.image_to_string(img, lang='eng')

        # print('验证码是：' + text)
        return text

    def noise_remove_pil(self, img, k):  # image_name: 图片文件命名 k: 判断阈值

        def calculate_noise_count(img_obj, w, h):
            """
            计算邻域非白色的个数
            Args:
                img_obj: img obj
                w: width
                h: height
            Returns:
                count (int)
            """
            count = 0
            width, height = img_obj.size
            for _w_ in [w - 1, w, w + 1]:
                for _h_ in [h - 1, h, h + 1]:
                    if _w_ > width - 1:
                        continue
                    if _h_ > height - 1:
                        continue
                    if _w_ == w and _h_ == h:
                        continue
                    if img_obj.getpixel((_w_, _h_)) < 230:  # 这里因为是灰度图像，设置小于230为非白色
                        count += 1
            return count

        # 灰度
        gray_img = img.convert('L')

        w, h = gray_img.size
        for _w in range(w):
            for _h in range(h):
                if _w == 0 or _h == 0:
                    gray_img.putpixel((_w, _h), 255)
                    continue
                # 计算邻域非白色的个数
                pixel = gray_img.getpixel((_w, _h))
                if pixel == 255:
                    continue

                if calculate_noise_count(gray_img, _w, _h) < k or calculate_noise_count(gray_img, _w, _h) > 10:
                    gray_img.putpixel((_w, _h), 255)
        gray_img_name = 'noise_remove_pil.jpg'
        gray_img.save('noise_remove_pil.jpg')
        # print('降噪处理' + str(k))
        gray_img.show()

        return gray_img

    def jiangzao(self, gray_img):
        # 要去掉黑点，就是一个二值化降噪的过程。可以用PIL（Python Image Library）试试
        gray_img = gray_img.filter(ImageFilter.MedianFilter())
        enhancer = ImageEnhance.Contrast(gray_img)
        gray_img = enhancer.enhance(2)
        gray_img = gray_img.convert('1')
        gray_img.save('jiangzao.png')
        gray_img.show()
        return gray_img

    def removePunctuation(self, text):
        add_punc = '，。、【】“”：；（）《》‘’{}？！⑦()、%^>℃：.”“^-——=擅长于的&#@￥'  # 自定义--中文的字符
        all_punc = punctuation + add_punc
        temp = []
        for c in text:
            if c not in all_punc:
                temp.append(c)
        newText = ''.join(temp)
        print('去除标点后的验证码是：' + newText)
        return newText


if __name__ == "__main__":
    Code_Ocr()
