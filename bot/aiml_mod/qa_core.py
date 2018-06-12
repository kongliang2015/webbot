# -*- coding: utf-8 -*-
import aiml
import os
from django.conf import settings


class BotCore(object):


    def __init__(self, path):

        self.path = path
        # 切换到语料库所在工作目录
        os.chdir(self.path)
        print("<<<Bot Loading>>>")
        self.bot = aiml.Kernel()
        self.bot.learn("std-startup.xml")
        self.bot.respond('load aiml b')
        print("<<<Done>>>")

    def get_answer(self,question):

        return self.bot.respond(question)

# TODO  增加选择语聊数据库的参数
def query_function(question):

    # 创建bot
    test_bot = BotCore(settings.XML_DIR)

    # TODO 对原始query做标准化变换处理
    # my_query =
    my_query = question

    # 如果查询内容非空
    if my_query is not None:

        # 执行查询
        # result = 查询
        # value = 查询结果状态
        result = test_bot.get_answer(question)

        if result == "":
            return '抱歉，并没有该问题的答案'
        else:
            return result

    else:
        # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
        return '抱歉，无法理解你的问题'


# import warnings

def main():

    test_bot = BotCore("./xml")

    # warnings.filterwarnings('error',category = MySQLdb.Warning)

    while True:

        result = test_bot.get_answer(input("输入问题 >> "))

        if result == "":
            print('抱歉，并没有该问题的答案')
        else:
            print(result)

if __name__ == '__main__':

    main()
