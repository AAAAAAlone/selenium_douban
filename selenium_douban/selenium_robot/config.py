#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# COOKIES_FILE = 'logs/cookies.txt'
# LOG_FILE = 'logs/doubanrobot.log'

# 伊丽莎白吃白喝 账号
# LOGIN_EMAIL1 = 'marost@163.com'
# LOGIN_PWD1 = 'hoge1234'
# 测试账号
LOGIN_EMAIL1 = '18711824424'
LOGIN_PWD1 = 'abc123cba'

# XPATH 元素路径，2020.11.20
HOME = "https://www.douban.com/"
LOGIN_BY_PWD = '/html/body/div[1]/div[1]/ul[1]/li[2]'
LOGIN_UNAME_INPUT = '//*[@id="username"]'
LOGIN_PWD_INPUT = '//*[@id="password"]'
LOGIN_BTN = '/html/body/div[1]/div[2]/div[1]/div[5]/a'
LOGIN_CAPTCHA_DIV = '//*[@id="dui-dialog0"]'
LOGIN_CAPTCHA_IFRAME = '//*[@id="tcaptcha_iframe"]'
LOGIN_CAPTCHA_HX = '//*[@id="tcaptcha_drag_thumb"]'

LOGIN_SUCCESS_INPUT = '//*[@id="isay-label"]'
# endpoints
# people
# DOUBAN_HOME = "https://www.douban.com/"
# DOUBAN_ACCOUNT_LOGIN = "https://accounts.douban.com/j/mobile/login/basic"
# DOUBAN_MY = "https://www.douban.com/people/{accout_id}/"
# DOUBAN_EDIT_INTRO = "https://www.douban.com/j/people/{accout_id}/edit_intro"
# DOUBAN_DOUMAIL = "https://www.douban.com/doumail/"
# DOUBAN_DOUMAIL_WRITE = "https://www.douban.com/doumail/write"
# DOUBAN_DOUMAIL_REPLY = "https://www.douban.com/j/doumail/send"
# DOUBAN_DOUMAIL_CHAT = "https://www.douban.com/doumail/{receive_id}"
# DOUBAN_CONTACTS_LIST = "https://www.douban.com/contacts/list"
# DOUBAN_CONTACTS_RLIST = "https://www.douban.com/contacts/rlist"
# DOUBAN_REMOVE_CONTACT = "https://www.douban.com/j/contact/removecontact"
# DOUBAN_ADD_CONTACT = "https://www.douban.com/j/contact/addcontact"
# DOUBAN_BLACKLIST = "https://www.douban.com/contacts/blacklist"
# DOUBAN_ADD_BLACKLIST = "https://www.douban.com/j/contact/addtoblacklist"
# DOUBAN_REMOVE_BLACKLIST = "https://www.douban.com/contacts/blacklist?remove={douban_id}&ck={ck}"
# DOUBAN_UPLOAD_IMAGE = "https://www.douban.com/j/upload"
#
# # group
# DOUBAN_GROUP = "https://www.douban.com/group/"
# DOUBAN_GROUP_HOME = "https://www.douban.com/group/{group_id}/"
# DOUBAN_GROUP_LIST_JOINED_GROUPS = 'https://www.douban.com/group/people/{accout_id}/joins'
# DOUBAN_GROUP_QUIT_GROUP = "https://www.douban.com/group/{group_id}/?action=quit&ck={ck}"
# DOUBAN_GROUP_MY_PUBLISH = "https://www.douban.com/group/people/{accout_id}/publish"
# DOUBAN_GROUP_MY_REPLY = "https://www.douban.com/group/people/{accout_id}/reply"
# DOUBAN_TOPICS = "https://www.douban.com/group/{group_id}/"
# DOUBAN_NEW_TOPIC = "https://www.douban.com/group/{group_id}/new_topic"
# DOUBAN_TOPIC = "https://www.douban.com/group/topic/{topic_id}/"
# DOUBAN_REMOVE_TOPIC = "https://www.douban.com/group/topic/{topic_id}/remove"
# DOUBAN_ADD_COMMENT = "https://www.douban.com/group/topic/{topic_id}/add_comment"
# DOUBAN_REMOVE_COMMENT = "https://www.douban.com/j/group/topic/{topic_id}/remove_comment"
# DOUBAN_ADMIN_REMOVE_COMMENT = "https://www.douban.com/group/topic/{topic_id}/remove_comment/?cid={cid}"
# DOUBAN_REACT = "https://m.douban.com/rexxar/api/v2/group/topic/"
# DOUBAN_DOULIST = "https://www.douban.com/j/doulist/"
#
# DEBUG = True
#
# if __name__ == '__main__':
#     MY = "https://www.douban.com/people/{accout_id}"
#     print(MY.format(accout_id="6333"))
