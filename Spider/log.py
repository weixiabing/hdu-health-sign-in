import os
import sys
import time
import logging


def printing(filename, function, lineno, e):
    current_path = os.path.abspath(__file__)
    parent_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    logName = today + "_e.log"
    if not os.path.exists("{}/logDir/toolLog/".format(parent_path)):
        os.makedirs("{}/logDir/toolLog/".format(parent_path))
    if not os.path.exists("{}/logDir/toolLog/{}/".format(parent_path, today)):
        os.makedirs("{}/logDir/toolLog/{}/".format(parent_path, today))
    if not os.path.exists("{}/logDir/toolLog/{}/{}".format(parent_path, today, logName)):
        reportFile = open("{}/logDir/toolLog/{}/{}".format(parent_path, today, logName), 'w')
        reportFile.close()
    logger = logging.getLogger()
    handler = logging.FileHandler("{}/logDir/toolLog/{}/{}".format(parent_path, today, logName), encoding='utf8')
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s')
    print(str(formatter))

    handler.setFormatter(formatter)  # 将log信息绑定到log文件上
    console.setFormatter(formatter)  # 将log信息绑定到控制台输出窗口
    logger.addHandler(handler)
    logger.addHandler(console)
    logger.setLevel(logging.INFO)  # Set log print level(设置日志打印级别)
    logging.info(filename + '   Function: ' + function + '  Line: ' + str(lineno) + '  Exception: ' + e)
    # print(e,'log.py')
