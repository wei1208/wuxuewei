from Common import  Request,Assert,read_excel
import allure

request = Request.Request()

assertion = Assert.Assertions()
idsList=[]
excel_list = read_excel.read_excel_list('../document/test.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url = 'http://192.168.1.137:8080/'
head = {}


@allure.feature("登录功能")
class Test_login:

    @allure.story("登录")
    def test_login(self):
        # =后面 :  request对象 调用了  post_request  方法,传入了两个参数
        # = 前面:  将方法 返回的 对象/变量  起一个名字
        login_resp = request.post_request(url=url+ 'admin/login', json={"username": "admin", "password": "123456"})


        # 响应 . text  :  就是获取 text属性的内容,这个就是 响应正文 (str 格式)
        resp_text = login_resp.text
        print(type(resp_text))

        # 响应 .json()  :  就是获取 字典格式的内容,这个就是 响应正文 (字典 格式)
        resp_dict = login_resp.json()
        print(type(resp_dict))

        # .assert_code 用来断言 状态码 第一个参数填响应的状态码 第二个参数期望值
        assertion.assert_code(login_resp.status_code,200)
        # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符 第二个参数填这个字符 是否存在第一个里面
        assertion.assert_code(login_resp.status_code, 200)
        data_dict = resp_dict['data']
        token = data_dict['token']
        tokenHead = data_dict['tokenHead']
        global head
        head = {'Authorization' : tokenHead+token}


    @allure.story("获取用户信息")

    def test_info(self):

        info_resp =request.get_request(url=url+ 'admin/info',headers=head)
        resp_dict = info_resp.json()
        assertion.assert_code(info_resp.status_code,200)
#         assertion.assert_in_text(resp_dict['message'],'成功')


from Common import  Request,Assert, read_excel
import allure
import pytest

request = Request.Request()

assertion = Assert.Assertions()

idsList=[]
excel_list = read_excel.read_excel_list('../document/test.xlsx')
length = len(excel_list)
for i in range(length):
    idsList.append(excel_list[i].pop())

url = 'http://192.168.1.137:8080/'
head = {}


@allure.feature("商品模块")
class Test_sku:
    @allure.story("登录")
    def test_login(self):
        login_resp = request.post_request(url=url + 'admin/login', json={"username": "admin", "password": "123456"})


    @allure.story("获取商品分类")
    def test_get_sku(self):
        parm = {'pagenum':'1','pageSize':'10'}
        get_sku_resp = request.get_request(url=url+'productCategory/list/0',parms=parm,headers=head)
        resp_json = get_sku_resp.json()
        assertion.assert_code(get_sku_resp.status_code,200)
        assertion.assert_in_text(resp_json['message'],'成功')

        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        sku_id = item['id']

        @allure.story("删除商品分类")
        def test_del_sku(self):
            del_sku_resp = request.post_request(url=url+'productCategory/delete/' + str(sku_id),headers=head)
            resp_json = del_sku_resp.json()
            assertion.assert_code(del_sku_resp.status_code, 200)
            assertion.assert_in_text(resp_json['message'], '成功')























































