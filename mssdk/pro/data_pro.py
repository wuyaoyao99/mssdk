# -*- coding:utf-8 -*-
# /usr/bin/env python
"""
Author: qhsdk
Date: 2019/11/10 22:52
Desc: 数据接口初始化
"""
from mssdk.pro import client
from mssdk.utils import token_process


def pro_api(token=''):
    """
    初始化 pro API,第一次可以通过qh.set_token('your token')来记录自己的token凭证，临时token可以通过本参数传入
    """
    if token == '' or token is None:
        token = token_process.get_token()
    if token is not None and token != '':
        pro = client.DataApi(token)
        return pro
    else:
        raise Exception('api init error.')


if __name__ == '__main__':
    pro_test = pro_api(token="")

