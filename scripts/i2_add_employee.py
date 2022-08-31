import app
import json
import utils
import logging
import unittest
from api.ihrm_api import ihrm_api
from checkPoint import CheckPoint
from parameterized import parameterized

class ihrm_add_employee(CheckPoint):
    #前置处理
    def setUp(self):
        self.add_employee_api = ihrm_api()
    #后置处理
    def tearDown(self):
        pass

    #添加成员
    @parameterized.expand(utils.build_data(filename="i2_add_employee.json", params_name="username, mobile, timeOfEntry, formOfEmployment, workNumber, departmentId, correctionTime, status_code, code, success, message"))
    def test001_add_employee(self, username, mobile, timeOfEntry, formOfEmployment, workNumber, departmentId, correctionTime, status_code, code, success, message):
        headers_data = app.headers_data
        add_data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": timeOfEntry,
            "formOfEmployment": formOfEmployment,
            "workNumber": workNumber,
            "departmentId": departmentId,
            "correctionTime": correctionTime
        }
        response = self.add_employee_api.add_employee(headers_data, add_data)
        print("添加成员：{}".format(response.json()))
        logging.info("添加成员：{}".format(response.json()))
        if add_data.get("mobile") == app.add_mobile and response.json().get("success") is True:
            app.test_id = response.json().get("data").get("id")
            logging.info("测试ID：{}".format(app.test_id))
        self.checkAssertEqual(status_code, response.status_code)
        self.checkAssertEqual(code, response.json().get("code"))
        self.checkAssertEqual(success, response.json().get("success"))
        self.checkAssertEqual(message, response.json().get("message"))
        self.checkTestResult()
    if __name__ == "__main__":
        unittest.main()

