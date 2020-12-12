#!/usr/bin/python
# -*- coding: UTF-8 -*-
import traceback
from pprint import pprint

from selenium.webdriver import ActionChains
from selenium import webdriver
from threading import Timer
from time import sleep
from UI_ele_API import *
import config
import random
from threading import Timer


class AcctGrowth(object):
    def __init__(self, driver=None):
        self.scroll_speed = 2.5
        self.view_level = 5
        self.view = True
        if driver is None:
            self.driver = webdriver.Chrome()
            self.window = []
        # self.ac = ActionChains(self.driver) 如果申明私有ac，会导致动作链无法清除
        self.driver = driver
        self.driver.get('https://www.douban.com/group/684795/')
        self.ui = UI_ele()
        self.test()

    def test(self):
        # ele = self.driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/form/button')
        # # self.mouse_move_to(500, 500)
        # self.mouse_move_to(None, None, ele)
        # ele.click()
        # ele = self.ui.get_ele_bylink(self.driver, 'https://www.douban.com/group/explore')
        # ele = self.ui.get_ele_bylinktext(self.driver, '精选')
        # self.mouse_move_to(None, None, ele, True)

        click_task_list = [self.ran_get_url, self.ran_get_url, self.ran_get_url, self.ran_get_url,
                           self.get_nav, self.get_nav, self.get_ran_window(), self.close_windows()]
        view_list = [self.view_time]
        #  random.choice([a,b])() 从列表中随机选择函数对象：
        while True:
            try:
                vtime_random = random.randint(self.view_level * 1, 20 + self.view_level * 10)
                if random.choice(click_task_list)() is False:
                    pprint('==========任务失败，3秒后重新加载首页============')
                    sleep(3)
                    self.driver.get(config.HOME)
                else:
                    sleep(2)
                    random.choice(view_list)(vtime_random)
                    pprint('==========执行下一个任务===============')
            except Exception as e:
                pprint('============主程序报错了==============')
                traceback.print_exc()

    # 检查当前页面，如果内容太少则重新访问某个页面
    '''TODO'''

    # 随机加载一个页面URL
    def ran_get_url(self, click=True):
        windows_num = self.driver.window_handles
        ele_list = self.ui.get_ele_list(self.driver, config.RANDOM_URL)
        if ele_list:
            # 抽取链接检查是否下载链接，如果是下载链接，则重新随机一个
            while True:
                ran_num = random.randint(0, (len(ele_list) - 1))
                ele = ele_list[ran_num]
                # 随机的链接不包含下载地址等排出链接
                if ele.get_attribute('href').find('download') == -1:
                    if click:
                        try:
                            ac = ActionChains(self.driver)
                            ac.click(ele).perform()
                            pprint('鼠标点击进入url成功')
                        except Exception:
                            pprint('点击失败，直接get 访问目标路径页面')
                            self.driver.get(ele.get_attribute('href'))
                            return
                        else:
                            # 只有模拟点击才可能会生成新窗口，判断是否新窗口
                            windows_num_new = self.driver.window_handles
                            if windows_num_new == windows_num:
                                pprint('没有页面变化')
                                return
                            else:
                                try:
                                    pprint('切换新窗口')
                                    self.switch_new_windows()
                                except Exception:
                                    pprint('切换新窗口失败')
                                finally:
                                    return
                    else:
                        self.driver.get(ele.get_attribute('href'))
                        return
                else:
                    # 可以增加排除的链接
                    pprint('=============链接包含download,进入循环重新随机===========')
                    pprint(ele.get_attribute('href'))
        else:
            pprint('返回的节点为空')
            return False

    # 切换到最近的窗口
    def switch_new_windows(self):
        try:
            all_hand = self.driver.window_handles
            self.driver.switch_to.window(all_hand[-1])
        except Exception:
            pprint('切换最近窗口错误')
        finally:
            return

    # 检测浏览器窗口数量，关闭其他窗口
    def close_windows(self):
        self.window = self.driver.window_handles
        while len(self.window) > 7:
            self.driver.close()
            self.window = self.driver.window_handles
            self.driver.switch_to.window(random.choice(self.window))
        pprint('剩下唯一的窗口')
        return

    # 按照时间浏览
    def view_time(self, v_time):
        ran_min = -1500
        ran_max = 4700
        i = 0
        while i < v_time:
            ran_scroll = random.randint(ran_min*0.8, ran_max*0.8)
            Timer(2, self.scroll, (ran_scroll,)).start()
            sleep(2)
            i += 4
        pprint('浏览了' + str(v_time) + '秒')
        return

    # 点击页面上的指定url 或锚文本
    def get_target_url(self, text=None, url=None):
        # 检查窗口数量，数量变化则需要切换到新窗口
        windows_num = self.driver.window_handles
        pprint('当前窗口数' + windows_num)
        if text:
            ele = self.ui.get_ele_bylinktext(self.driver, text)
            try:
                ac = ActionChains(self.driver)
                ac.click(ele).perform()
            except Exception:
                pprint('点击指定锚文本失败')
                return False
            else:
                windows_num_new = self.driver.window_handles
                if windows_num_new == windows_num:
                    pprint('没有页面变化')
                    return
                else:
                    try:
                        self.switch_new_windows()
                        return
                    except Exception:
                        pprint('切换新窗口失败')
                    return False
        elif url:
            ele = self.ui.get_ele_bylink(self.driver, url)
            try:
                ac = ActionChains(self.driver)
                ac.click(ele).perform()
            except Exception:
                pprint('点击指定url失败')
                '''加入get访问'''
                return False
            else:
                windows_num_new = self.driver.window_handles
                if windows_num_new == windows_num:
                    # 没有页面变化
                    return
                else:
                    try:
                        self.switch_new_windows()
                    except Exception:
                        pprint('切换新窗口失败')
                return

    # 随机切换tab
    def get_ran_window(self):
        self.window = self.driver.window_handles
        self.driver.switch_to.window(random.choice(self.window))
        self.view_time(5)
        return

    # 随机打开导航
    def get_nav(self, nav=config.DOUBAN_TOP_NAV, tab_num=3):
        windows_num = self.driver.window_handles
        for i in range(tab_num):
            ele_list = self.ui.get_ele_list(self.driver, nav)
            if ele_list:
                ran_num = random.randint(0, (len(ele_list) - 1))
                print(ran_num)
                ele = ele_list[ran_num]
                # self.mouse_move_to(None, None, ele)
                # sleep(0.8)
                self.mouse_move_to(None, None, ele, True)
                windows_num_new = self.driver.window_handles
                if windows_num_new == windows_num:
                    pprint('没有页面变化')
                else:
                    try:
                        pprint('切换新窗口')
                        self.switch_new_windows()
                    except Exception:
                        pprint('切换新窗口失败')
                sleep(1.5)
            else:
                return False
        return

    # 屏幕平滑滚动, 使用window.scrollBy({top:100, left:0,behavior: 'smooth'})
    def scroll(self, scroll_px):
        js = 'window.scrollBy({top:' + str(scroll_px) + ', left:0,behavior: \'smooth\'})'
        if scroll_px == 'top':
            scroll_to_top = 'window.scrollTo({top:0, left:0,behavior: \'smooth\'})'
            self.driver.execute_script(scroll_to_top)
            sleep(1)
            pprint('滚动到头部')
        elif scroll_px == 'bottom':
            scroll_to_bottom = 'window.scrollTo({top:document.body.scrollHeight, left:0,behavior: ' \
                               '\'smooth\'}) '
            self.driver.execute_script(scroll_to_bottom)
            sleep(1)
            pprint('滚动到底部')
        else:
            self.driver.execute_script(js)
            sleep(self.scroll_speed)
            # pprint('滚动距离为' + str(scroll_px))
        pprint('滚动完毕')
        return

    # 鼠标点击节点
    # def mouse_click(self, ele):
    #     ac = ActionChains(self.driver)
    #     ac.click(ele).perform()
    #     return

    # 鼠标移动或点击,
    def mouse_move_to(self, x=None, y=None, ele=None, click=False):
        ac = ActionChains(self.driver)
        print('mouse_move_to()')
        try:
            if click:
                ac.click(ele).perform()
                pprint('移动并点击目标节点')
                return
            elif ele is None:
                ac.move_by_offset(x, y).perform()
                pprint('鼠标移动【X:' + str(x) + '】【Y：' + str(y) + '】')
                return
            elif x and y:
                ac.move_to_element_with_offset(ele, x, y).perform()
                pprint('鼠标移动到节点上，并额外移动【X:' + str(x) + '】【Y：' + str(y) + '】')
                return
            elif x is None and y is None:
                ac.move_to_element(ele).perform()
                pprint('鼠标移动到节点上, 不点击')
                return
        except Exception:
            traceback.print_exc()
            return False

    # 键盘操作打字
    # 按照关键词搜索浏览
    # 按照话题搜索浏览
    # 列表翻页
    # 随机点击导航，进入列表页


if __name__ == '__main__':
    AcctGrowth()
