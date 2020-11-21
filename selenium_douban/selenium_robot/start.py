#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
# import selenium.webdriver.support.ui as ui
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# import requests
# import pickle
from pprint import pprint
from get_Code import *
# from PIL import Image
from config import *
from Code_Ocr import *
from UI_ele_API import *

def main():
    try:
        # 创建驱动实例
        global driver
        email = LOGIN_EMAIL1
        password = LOGIN_PWD1
        # 登陆
        driver = login(email, password)
        # 访问页面
        time.sleep(0.5)
        while True:
            # post_tiezi('https://www.douban.com/group/topic/201068579/',
            #            '哈哈哈哈哈哈哈')
            # post_tiezi('https://www.douban.com/group/topic/190341182/',
            #            '哈哈哈哈')
            # post_tiezi('https://www.douban.com/group/topic/184372269/',
            #            '哈哈哈哈哈哈哈哈哈')
            # post_tiezi('https://www.douban.com/group/topic/199951848/',
            #            '最近正在学习这个部分，大家有类似的资料整理需求欢迎加我哈哈哈')
            # post_tiezi('https://www.douban.com/group/topic/200084831/',
            #            '最近正在学习这个部分，大家有类似的资料整理需求欢迎加我哈哈哈')

            post_tiezi('https://www.douban.com/group/topic/200963909/',
                       'ddd')
            post_tiezi('https://www.douban.com/group/topic/200963021/',
                       'ddd')
            post_tiezi('https://www.douban.com/group/topic/200962757/',
                       'ddd')
            post_tiezi('https://www.douban.com/group/topic/200962474/',
                       'ddd')
            post_tiezi('https://www.douban.com/group/topic/200961519/',
                       'ddd')
            post_tiezi('https://www.douban.com/group/topic/200961200/',
                       'ddd')
            post_tiezi('https://www.douban.com/group/topic/200960316/',
                       'ddd')
            time.sleep(3600)
    except Exception as identifier:
        pass
        # pprint('任务失败')
        # time.sleep(100)
        # main()


def is_inGroup():
    try:
        Group_ck = ui.WebDriverWait(driver, 2).until(
            lambda driver: driver.find_element_by_xpath(
                '//*[@id="g-side-info"]/div[2]/div/a'))
        Group_ck.click()
    except Exception as identifier:
        try:
            Group_ck = ui.WebDriverWait(driver, 2).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="content"]/div/div[1]/div[5]/form/span[1]/input'))
            Group_ck.click()
        except Exception as identifier:
            pass
    finally:
        try:
            Group_ck = ui.WebDriverWait(driver, 1).until(
                lambda driver: driver.find_element_by_xpath(
                    '//*[@id="dui-dialog0"]/div/div[2]'))
            pprint('账号被封禁')
        except Exception as identifier:
            pprint('加入小组或已在小组中')
    return


def post_tiezi(url, context):
    time.sleep(3)
    driver.get(url)
    time.sleep(2)
    driver.get(url)
    # 如果没有加入小组，则加入小组
    is_inGroup()
    # 等待加载发帖区域xpath
    wait = ui.WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element_by_xpath(
        '//*[@id="last"]'))
    # 找到输入的文本框填入内容
    driver.find_element_by_xpath(
        '//*[@id="last"]').send_keys(context)
    time.sleep(3)
    try:
        # 保存验证码
        code_ele = driver.find_element_by_xpath(
            '//*[@id = "captcha_image"]')
        code_ele.screenshot('code-douban.jpeg')
        # code_ele.screenshot(
        #     r'/Users/oscar/Downloads/selenium_douban/selenium_robot/code-douban.jpeg')

        try:
            code_text = Code_Ocr()
            # 填入验证码输入框
            driver.find_element_by_xpath(
                '//*[@id = "captcha_field"]').send_keys(code_text)
            # 点击提交 - 直接发送即可
        except Exception as identifier:
            print('ocr识别错误，手动输入验证码')
            code_text = GetCode().show_code()

    except Exception as identifier:
        pprint('没有验证码')
        pprint(identifier)
        # 检查是否有验证码

    finally:
        # 点击发帖
        driver.find_element_by_xpath('//*[@name="submit_btn"]').click()
        # last //*[@id="last"]
        pprint('发帖成功！【' + context + '】')
        time.sleep(4)


def code_image_save():
    return


def login(email, password):
    # try:
    driver = webdriver.Chrome()
    driver.get(HOME)
    driver.switch_to.frame(0)
    # 点击切换到密码登陆框
    ui_ele = UI_ele()
    ui_ele.get_ele(driver, LOGIN_BY_PWD, 2).click()
    # 填入账号密码
    ui_ele.get_ele(driver, LOGIN_UNAME_INPUT, 1).send_keys(email)
    ui_ele.get_ele(driver, LOGIN_PWD_INPUT, 1).send_keys(password)
    # 点击登陆
    ui_ele.get_ele(driver, LOGIN_BTN, 1).click()
    time.sleep(1.3)
    # 判断是否有登录验证码，有则切换iframe并调用滑块验证
    while True:
        if ui_ele.ui_exist_byxpath(driver, LOGIN_SUCCESS_INPUT, 3, 1):
            pprint("******** 无验证码，登录成功 ******")
            break
        elif ui_ele.ui_exist_byxpath(driver, LOGIN_CAPTCHA_DIV, 3, 1):
            # if ec.frame_to_be_available_and_switch_to_it((By.ID, 'tcaptcha_iframe')):
            dr_iframe = ui_ele.switch_iframe(driver, LOGIN_CAPTCHA_IFRAME)
            # driver.switch_to.frame(LOGIN_CAPTCHA_IFRAME)
            post_hx(dr_iframe)
            pprint('*****通过验证码，登录成功！*****')
            break

    return driver

    #
    # except Exception as identifier:
    #     pprint('登录失败，10秒后重试...')
    #     time.sleep(10)
    #     login(email, password)
    # return driver


def post_hx(driver):
    # 初始减速滑块距离
    px = 28
    while True:
        ui_ele = UI_ele()
        # 选中滑块
        hk_ele = ui_ele.get_ele(driver, LOGIN_CAPTCHA_HX, 5, 1)
        # 按住和拖动
        ActionChains(driver).click_and_hold(on_element=hk_ele).perform()
        ActionChains(driver).move_to_element_with_offset(
            to_element=hk_ele, xoffset=160, yoffset=0).perform()

        tracks = get_tracks(px)
        for track in tracks:
            ActionChains(driver).move_by_offset(
                xoffset=track, yoffset=0).perform()

        time.sleep(0.8)
        # 放手
        ActionChains(driver).release().perform()

        # 如果找到发帖位置，则为登录成功
        if ui_ele.ui_exist_byxpath(driver, LOGIN_SUCCESS_INPUT, 4, 1):
            # 登录成功
            break
        else:
            pprint('验证码失败，重新登录...')
            px += 7
            # 超过一定距离后重新从小开始
            if px > 56:
                px = 21

    return


def get_tracks(distance):
    v = 1
    t = 0.2
    tracks = []
    current = 0
    mid = distance*4/5
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3

        v0 = v
        s = v0*t + 0.5*a*(t**2)
        current += s
        tracks.append(round(s))

        v = v0 + a*t

    return tracks


if __name__ == '__main__':
    main()
