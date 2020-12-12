#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import traceback

import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from pprint import *
import re
from time import sleep
from selenium.common.exceptions import TimeoutException


class UI_ele(object):
    def __init__(self):
        self.ele = None

    # 判断某个xpath是否存在
    def ui_exist_byxpath(self, driver, xpath, wait_time=10, sleep_time=0.1):
        time.sleep(sleep_time)
        try:
            self.ele = ui.WebDriverWait(driver, wait_time).until(
                lambda driver: driver.find_element_by_xpath(xpath))
            pprint('找到目标xpath' + xpath)
            return True

        except TimeoutException as error:
            pprint("=============================")
            pprint("加载UI节点失败：" + xpath)
            # pprint(error)
            traceback.print_exc()
            return False

    # 返回xpath对应的节点
    def get_ele(self, driver, xpath, wait_time=1, sleep_time=0.1):
        if self.ui_exist_byxpath(driver, xpath, wait_time, sleep_time):
            return self.ele
        else:
            pprint("============")
            pprint("找不到目标路径的节点")
            return

    # 根据xpath 返回一组节点
    def get_ele_list(self, driver, xpath, wait_time=2, sleep_time=0.1):
        time.sleep(1.5)
        try:
            self.ele = ui.WebDriverWait(driver, wait_time).until(
                lambda driver: driver.find_elements_by_xpath(xpath))
            pprint('找到目标列表' + xpath)
            return self.ele

        except TimeoutException as error:
            pprint("=============================")
            pprint("加载UI节点失败：" + xpath)
            # pprint(error)
            traceback.print_exc()
            return False

    # 根据锚文本获取节点
    def get_ele_bylinktext(self, driver, link_text, wait_time=3, sleep_time=0.2):
        try:
            self.ele = ui.WebDriverWait(driver, wait_time).until(
                lambda driver: driver.find_element_by_link_text(link_text))
        except TimeoutException as timeout:
            pprint('找不到指定的' + link_text)
            traceback.print_exc()
            return False
        else:
            return self.ele
        return

    # 根据URL 获取节点
    # 返回一组数据，用find_elements 方法, 匹配到对应的Link
    def get_ele_bylink(self, driver, link=None, wait_time=3, sleep_time=0.2):
        try:
            self.ele = ui.WebDriverWait(driver, wait_time).until(
                lambda driver: driver.find_elements_by_xpath('//a[@href]'))
            for i in self.ele:
                if re.search(link, i.get_attribute('href')):
                    pprint(re.search(link, i.get_attribute('href')))
                    return i
            pprint('找不到link')
            traceback.print_exc()
            return False
            # pprint(i.get_attribute('href'))

        except TimeoutException as timeout:
            pprint('找不到指定的' + link)
            traceback.print_exc()
            return False
        else:
            return self.ele
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
