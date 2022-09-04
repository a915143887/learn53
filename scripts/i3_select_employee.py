import app
import json
import utils
import logging
import unittest
from api.ihrm_api import ihrm_api
from checkPoint import CheckPoint
from parameterized import parameterized

class ihrm_select_employee(CheckPoint):
    #前置处理
    def setUp(self):
        self.select_employee_api = ihrm_api()
    #后置处理
    def tearDown(self):
        pass

    #查询成员
    @parameterized.expand(utils.build_data(filename="i3_select_employee.json", params_name="t, status_code, code, success, message"))
    def test001_select_employee(self, t, status_code, code, success, message):
        type = t
        if type == "accurate":
            self.select_id = app.test_id
            logging.info("精确查询ID：{}".format(self.select_id))
        elif type == "fuzzy":
            self.select_id = fuzzy_id = app.test_id[0:18]
            logging.info("模糊查询ID：{}".format(fuzzy_id))

        headers_data = app.headers_data
        response = self.select_employee_api.select_employee(self.select_id, headers_data)
        print("查询成员：{}".format(response.json()))
        logging.info("查询成员：{}".format(response.json()))
        self.checkAssertEqual(status_code, response.status_code)
        self.checkAssertEqual(code, response.json().get("code"))
        self.checkAssertEqual(success, response.json().get("success"))
        self.checkAssertEqual(message, response.json().get("message"))
        self.checkTestResult()
    if __name__ == "__main__":
        unittest.main()


