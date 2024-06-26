import logging
import os
import sys
import time

from hkws.core import env

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)
from hkws import cm_camera_adpt, config
from example import face_captured_cb

# Initialized configuration file
cnf = config.Config()
path = os.path.join('../local_config.ini')
cnf.InitConfig(path)
if env.isWindows():
    os.chdir(cnf.SDKPath)

# 初始化SDK适配器
adapter = cm_camera_adpt.CameraAdapter()
userId = adapter.common_start(cnf)
if userId < 0:
    logging.error("初始化Adapter失败")
    os._exit(0)

data = adapter.setup_alarm_chan_v31(face_captured_cb.face_alarm_call_back, userId)
print("设置回调函数结果", data)
# 布防
alarm_result = adapter.setup_alarm_chan_v41(userId)
print("设置人脸v41布防结果", alarm_result)

time.sleep(60)
adapter.close_alarm(alarm_result)

adapter.logout(userId)
adapter.sdk_clean()
