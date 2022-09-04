import app
import json
import utils
import logging
import unittest
from api.ihrm_api import ihrm_api
from checkPoint import CheckPoint
from parameterized import parameterized

class ihrm_update_employee(CheckPoint):
    #前置处理
    def setUp(self):
        self.update_employee_api = ihrm_api()
    #后置处理
    def tearDown(self):
        pass

    #修改成员
    @parameterized.expand(utils.build_data(filename="i4_update_employee.json", params_name="username, status_code, success, code, message"))
    def test001_update_employee(self, username, status_code, success, code, message):
        update_id = app.test_id
        headers_data = app.headers_data
        update_data = {
            "username": username
        }
        response = self.update_employee_api.update_employee(update_id, headers_data, update_data)
        print("修改成员：{}".format(response.json()))
        logging.info("修改成员：{}".format(response.json()))
        self.checkAssertEqual(status_code, response.status_code)
        self.checkAssertEqual(success, response.json().get("success"))
        self.checkAssertEqual(code, response.json().get("code"))
        self.checkAssertEqual(message, response.json().get("message"))
        self.checkTestResult()
    if __name__ == "__main__":
        unittest.main()
