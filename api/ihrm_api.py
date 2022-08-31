import app
import requests

class ihrm_api():
    def __init__(self):
        #登录url
        self.login_url = app.base_Url + "/api/sys/login"
        #添加成员url
        self.add_employee_url = app.base_Url + "/api/sys/user"

    #登录
    def login(self, headers_data, login_data):
        return requests.post(url=self.login_url, headers=headers_data, json=login_data)

    #添加成员
    def add_employee(self, headers_data, add_data):
        return requests.post(url=self.add_employee_url, headers=headers_data, json=add_data)
