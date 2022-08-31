import app
import json
import utils
import logging
import unittest
from api.ihrm_api import ihrm_api
from checkPoint import CheckPoint
from parameterized import parameterized

class ihrm_login(CheckPoint):
    #前置处理
    def setUp(self):
        self.login_api = ihrm_api()
    #后置处理
    def tearDown(self):
        pass

    #登录
    @parameterized.expand(utils.build_data(filename="i1_login.json", params_name="mobile, password, status_code, code, success, message"))
    def test001_and_004_login(self, mobile, password, status_code, code, success, message):
        headers_data = {
            "Content-Type": "application/json"
        }
        login_data = {
            "mobile": mobile,
            "password": password,
        }
        response = self.login_api.login(headers_data, login_data)
        print("登录：{}".format(response.json()))
        logging.info("登录：{}".format(response.json()))
        if login_data.get("mobile") == app.login_mobile and response.json().get("success") is True:
            app.Authorization = "Bearer " + response.json().get("data")
            app.headers_data["Authorization"] = app.Authorization
            logging.info("响应头：{}".format(app.headers_data))
        self.checkAssertEqual(status_code, response.status_code)
        self.checkAssertEqual(code, response.json().get("code"))
        self.checkAssertEqual(success, response.json().get("success"))
        self.checkAssertEqual(message, response.json().get("message"))
        self.checkTestResult()
    if __name__ == "__main__":
        unittest.main()
