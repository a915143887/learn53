import app
import json
import utils
import logging
import unittest
from api.ihrm_api import ihrm_api
from checkPoint import CheckPoint
from parameterized import parameterized

def build_data(filename, params_name):
    test_data = []
    file = app.base_Dir + "/data/" + filename
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            test_params = []
            for params in params_name.split(", "):
                test_params.append(case_data.get(params))
            test_data.append(test_params)
            print("test_params= {}".format(test_params))
        return test_data

class ihrm_delete_employee(CheckPoint):
    #前置处理
    def setUp(self):
        self.delete_employee_api = ihrm_api()
    #后置处理
    def tearDown(self):
        pass

    #删除成员
    @parameterized.expand(build_data(filename="i5_delete_employee.json", params_name="status_code, success, code, message"))
    def test001_delete_employee(self, status_code, success, code, message):
        delete_id = app.test_id
        headers_data = app.headers_data
        response = self.delete_employee_api.delete_employee(delete_id, headers_data)
        print("删除成员：{}".format(response.json()))
        logging.info("删除成员：{}".format(response.json()))
        self.checkAssertEqual(status_code, response.status_code)
        self.checkAssertEqual(success, response.json().get("success"))
        self.checkAssertEqual(code, response.json().get("code"))
        self.checkAssertEqual(message, response.json().get("message"))
        self.checkTestResult()
    if __name__ == "__main__":
        unittest.main()
