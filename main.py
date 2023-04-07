# -*- encoding: utf-8 -*-
"""
@File    : main.py
@Time    : 2023/4/5 9:35 PM
@Author  : nanjiang.xie
@Email   : xie672088678@163.com
@Software: PyCharm
"""
from app import app
import routes

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
