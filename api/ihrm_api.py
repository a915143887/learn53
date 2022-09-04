import app
import requests

class ihrm_api():
    def __init__(self):
        #登录url
        self.login_url = app.base_Url + "/api/sys/login"
        #添加成员url
        self.add_employee_url = app.base_Url + "/api/sys/user"
        #查询成员url
        self.select_employee_url = app.base_Url + "/api/sys/user/{}"
        #修改成员url
        self.update_employee_url = app.base_Url + "/api/sys/user/{}"
        #删除成员url
        self.delete_employee_url = app.base_Url + "/api/sys/user/{}"


    #登录
    def login(self, headers_data, login_data):
        return requests.post(url=self.login_url, headers=headers_data, json=login_data)

    #添加成员
    def add_employee(self, headers_data, add_data):
        return requests.post(url=self.add_employee_url, headers=headers_data, json=add_data)

    #查询成员
    def select_employee(self, select_id, headers_data):
        self.select_employee_url = self.select_employee_url.format(select_id)
        return requests.get(url=self.select_employee_url, headers=headers_data)

    #修改成员
    def update_employee(self, update_id, headers_data, update_data):
        self.update_employee_url = self.update_employee_url.format(update_id)
        return requests.put(url=self.update_employee_url, headers=headers_data, json=update_data)

    #删除成员
    def delete_employee(self, delete_id, headers_data):
        self.delete_employee_url = self.delete_employee_url.format(delete_id)
        return requests.delete(url=self.delete_employee_url, headers=headers_data)
