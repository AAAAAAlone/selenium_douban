#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import selenium.webdriver.support.ui as ui
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from pprint import *
from time import sleep


class UI_ele(object):
    def __init__(self):
        self.ele = None

    # 判断某个xpath是否存在
    def ui_exist_byxpath(self, driver, position, wait_time=10, sleep_time=0.1):
        time.sleep(sleep_time)
        try:
            self.ele = ui.WebDriverWait(driver, wait_time).until(
                lambda driver: driver.find_element_by_xpath(position))
            pprint('找到目标xpath' + position)
            return True

        except Exception as error:
            pprint("=============================")
            pprint("加载UI节点失败：" + position)
            # pprint(error)
            return False

    # 返回xpath对应的节点
    def get_ele(self, driver, position, wait_time=1, sleep_time=0.1):
        if self.ui_exist_byxpath(driver, position, wait_time, sleep_time):
            return self.ele
        else:
            pprint("============")
            pprint("找不到目标路径的节点")
            return

    # 尝试切换到指定的iframe

    def switch_iframe(self, driver, position, wait_time=1, sleep_time=0.1):
        try:
            iframe = self.get_ele(driver, position, wait_time, sleep_time)
        except Exception as e:
            pprint('找不到iframe')
            return
        else:
            driver.switch_to.frame(iframe)
            pprint('进入iframe')
            return driver
