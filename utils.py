#日志函数
import app
import time
import logging
from logging import handlers

def init_logging():
    #创建日志器
    logger = logging.getLogger()
    #设置日志等级
    logger.setLevel(logging.INFO)
    #创建控制台处理器
    ch = logging.StreamHandler()
    #创建文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(app.base_Dir + "/log/ihrm-{}.log".format(time.strftime("%Y%m%d-%H%M%S")),
                                                   when='h',
                                                   interval=1,
                                                   backupCount=5,
                                                   encoding="utf-8")
    #设置格式化器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt)
    #将格式化器添加到处理器
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    #将处理器添加到日志器
    logger.addHandler(ch)
    logger.addHandler(fh)

#init_logging()
#logging.info("测试")

#统一参数化读取方法
import json

def build_data(filename, params_name):
    test_data = []
    file = app.base_Dir + "/data/" + filename
    with open(file, encoding="utf-8") as f:
        json_data =json.load(f)
        for case_data in json_data:
            test_params = []
            for params in params_name.split(", "):
                test_params.append(case_data.get(params))
            test_data.append(test_params)
            print("test_params= {}".format(test_params))
        return test_data