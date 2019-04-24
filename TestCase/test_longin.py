from Common import Request,Assert
import allure


request = Request.Request()
assertion = Assert.Assertions()

@allure.feature("登陆成功")
class Test_longin:

    @allure.story("登录")
    def test_longin(self):

        login_resq = request.post_request(url='http://qa.guoyasoft.com:8099/admin/login',json={"username": "admin", "password": "123456"})

        resp_text = login_resq.text


        print(type(resp_text))

        resp_dict = login_resq.json()

        print(type(resp_dict))

        assertion.assert_code(login_resq.status_code,200)

        assertion.assert_in_text(resp_dict['message'],'成功')





