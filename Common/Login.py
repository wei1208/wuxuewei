import pytest

from Common import Shell


from Common import Request,Assert,read_excel
import allure
import  pytest
request = Request.Request()
assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('./document/test.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())
url = 'http://192.168.1.137:8080/'
head ={}


@allure.feature("登录功能")
class Test_lodin:

    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url+'admin/login',
                                                  json={"username": "admin", "password": "123456"})

        resp_text = login_resp.text
        print(type(resp_text))

        resp_dict = login_resp.json()
        print(type(resp_dict))

        assertion.assert_code(login_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['message'], '成功')

        data_dict =resp_dict['data']

        token = data_dict['token']
        tokenhead = data_dict['tokenHead']
        global head
        head = {'Authorization':tokenhead+token}

    @allure.story("获取用户信息")
    def test_info(self):

        info_resp = request.get_request(url=url+'admin/info',headers=head)
        resp_dict = info_resp.json()
        assertion.assert_code(info_resp.status_code, 200)
        assertion.assert_in_text(resp_dict['message'], '成功')

    @allure.story("测试登录")
    @pytest.mark.parametrize("username,password,msg",
                             [['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误'],
                              ['admin', '123456', '成功'], ['admin1', '123456', '错误'], ['admin', '123456a', '错误']],
                             ids=['登录成功', '用户名错误', '密码错误', '登录成功1', '用户名错误1', '密码错误1'])
    def test_loginl1(self,username,password,msg):
        login_resp = request.post_request(url=url + 'admin/login',
                                          json={"username": username, "password": password})
        resp_text = login_resp.text
        print(type(resp_text))