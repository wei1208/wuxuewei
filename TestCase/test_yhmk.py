from Common import Request, Assert,Tools
import random
import string
import time



import allure
import pytest

iphone = Tools.phone_num()
username = Tools.random_123(3)+Tools.random_str_abc(3)


request = Request.Request()
assertion = Assert.Assertions()
url = 'http://192.168.1.137:1811'
head = {}

@allure.feature('用户模块')
class Test_yhmk:
    @allure.story("注册")
    def test_user_signup(self):
        post_request = request.post_request(url=url+'/user/signup',
                                            json={"phone": iphone,"pwd": "5153253wei","rePwd": "5153253wei", "userName":username})
        resp_dict = post_request.json()
        print(type(resp_dict))

        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(resp_dict['respBase'], '成功')

    @allure.story("登录11")
    def test_user_denlu(self):
        post_request = request.post_request(url=url + '/user/login',
                                            json={"pwd": "wxw10086","userName": "wei2222"})
        resp_dict = post_request.json()


        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("修改密码")
    def test_user_xiugai(self):
        post_request = request.post_request(url=url+'/user/changepwd',json={"newPwd": "wxw10086","oldPwd": "5153253we","reNewPwd": "wxw10086",
                                                                           "userName": "wei2222"})
        resp_dict = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("冻结用户")
    def test_user_dongjie(self):
        post_request = request.post_request(url=url+'/user/lock',params={'userName':'wei2222'}
                                            ,headers={'Content-Type': 'application/x-www-form-urlencoded'})
        resp_dict = post_request.json()
        assertion.assert_code(post_request.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')

    @allure.story("解冻用户")
    def test_user_jiedong(self):
        jiedong_request = request.post_request(url=url+'/user/unLock',params={'userName':'wei2222'},
                                            headers={'Content-Type': 'application/x-www-form-urlencoded' })
        resp_dict =  jiedong_request.json()
        assertion.assert_code( jiedong_request.status_code, 200)
        assertion.assert_in_text(resp_dict['respDesc'], '成功')


























