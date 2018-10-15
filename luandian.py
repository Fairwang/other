#!/user/bin/python
#-*-coding:utf-8-*-
#!/user/bin/python
#-*-coding:utf-8-*-
from appium import webdriver
# from selenium import webdriver
import unittest
from jiandian01 import chaxunshujuku, swipefengzhuang
import time
from decimal import *
import random

class LoginTestjiandian(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platfromVersion']='7.1.1'
        desired_caps['deviceName']='33d04c7c'
        desired_caps['appPackage']='site.weide.shopmanage'
        desired_caps['automationName'] = 'uiautomator2'##############
        desired_caps['appActivity']='site.weide.shopmanage.Activity.GuideActivity'
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(3)

    def test_login(self):
# 测试登录成功并退出APP
        driver = self.driver
        # try:
        self.driver.implicitly_wait(10)
        swipefengzhuang.swipeRight(self, 1000)
        self.driver.implicitly_wait(10)
        swipefengzhuang.swipeRight(self, 1000)
        self.driver.implicitly_wait(10)
        swipefengzhuang.swipeRight(self, 1000)
        self.driver.implicitly_wait(10)
        # swipefengzhuang.swipeRight(self, 1000)
        self.driver.implicitly_wait(10)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        driver.find_element_by_id('site.weide.shopmanage:id/editText_login_usermobile').send_keys('15868314566')  # 输入手机号
        driver.find_element_by_id('site.weide.shopmanage:id/editText_login_userpass').send_keys('123456')  # 输入密码
        driver.find_element_by_id('site.weide.shopmanage:id/button_login_login').click()  # 点击登录
        self.driver.implicitly_wait(10)
        # try:
        #     text=driver.find_element_by_id('site.weide.shopmanage:id/shop_name').text
        #     assert u'15868314566测试' in text
        #     print 'loginUser is right'
        # except AssertionError as e:
        #     print 'loginUser is Error'
        # self.driver.implicitly_wait(5)

        driver.find_element_by_id('site.weide.shopmanage:id/activity_base_tab3_group').click()#进入单据页面
        time.sleep(3)
#判断订单详情页面部分数据是否与数据库一致

        #driver.find_element_by_xpath('//android.widget.TextView[@id="site.weide.shopmanage:id/textView_Tab3Main_Title"/following-sibling::android.support.v7.widget.RecyclerView/android.widget.LinearLayout[0]').click()
        driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        time.sleep(2)
        #driver.find_element_by_xpath("//android.widget.LinearLayout[@index='0']").click()#进入详情界面
        #判断详情页面和数据库是否一致
        text=driver.find_element_by_id('site.weide.shopmanage:id/order_number').text
        print text
        sql="select price,ispay,pay_way,pay_type from t_pay_order where order_id="+"'"+text+"'"
        print sql
        dingdan= chaxunshujuku.shujuku(sql)
        print dingdan
        print dingdan[0],dingdan[1],dingdan[2],dingdan [3]
#交易价格
        apprice=driver.find_element_by_id('site.weide.shopmanage:id/order_price').text
        print "apprice type%s" %type(apprice)
        price=Decimal(apprice[2:])
        print price,dingdan[0]
        print type(price),type(dingdan[0])

        assert dingdan[0]==price
#交易进程
        ispay=driver.find_element_by_id('site.weide.shopmanage:id/bill_states').text
        print  "yixiadaying "
        print  dingdan[1],ispay
        if dingdan==1 and ispay==u"已完成":
            print u"订单交易进程正确"
        else:
            print u"订单交易进程错误"
        # assert dingdan[1]==ispay
#交易类型、判断主扫和被扫
        payway=driver.find_element_by_id('site.weide.shopmanage:id/transaction_mode').text
        if payway==u'微信支付':
            payway='micropay'
        if payway==u'支付宝支付':
            payway='torepay'
        print dingdan[2],payway
        assert dingdan[2]==payway
#支付类型、交易方式
        paytype=driver.find_element_by_id('site.weide.shopmanage:id/transaction_type').text
        if paytype==u'扫码支付':
            paytype=1
        elif paytype==u'外卖订单'or paytype==u'堂食订单'or paytype==u'会员充值':
            paytype=2
        else:
            paytype=3
        assert dingdan[3]==paytype

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(LoginTestjiandian('test_login'))
    # filename = 'D:\\app.html'
    # fb=file(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title=u'简店登录注册测试', description=u'简店登录注册测试')
    # runner.run(suite)
    # fb.close()
    unittest.main()



def auto_interact(driver):
    activity = driver.current_activity
    # 一定的机率滑动，返回键，点击
    rate = random.random()
    if rate < 0.1:
        print activity + ' Scroll Down'
        appium_ecloud.test_scroll_down(driver)
    elif rate < 0.2:
        print activity + ' Scroll Up'
        appium_ecloud.test_scroll_up(driver)
    elif rate < 0.3:
        print activity + ' Key Back'
        driver.press_keycode(4)
    else:
        btn_list = driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        if (len(btn_list) > 0):
            index = random.randint(0, len(btn_list) - 1)
            print activity + ' Click Button index = %d' % (index,)
            btn_list[index].click()


def main():
    driver = None
    try:
        driver = appium_ecloud.install_app()
        time.sleep(appium_ecloud.LONG_WAIT_TIME)
        appium_ecloud.agree_document(driver)
        appium_ecloud.quick_login(driver)
        step = 0
        while step < 100:
            if (driver.current_activity.endswith('LoginActivity')):
                appium_ecloud.test_login(driver)
            elif (driver.current_activity.endswith('.Launcher')):
                driver.background_app(1)
                driver.launch_app()
            else:
                auto_interact(driver)
                time.sleep(appium_ecloud.CLICK_WAIT_TIME)
            step += 1
        # 正常退出
        driver.quit()

    except Exception, e:
        print Exception, ":", e
        traceback.print_exc()
        # 异常退出
        if (driver != None):
            driver.quit()


if __name__ == '__main__':
    for i in range(2000):
        try:
            main()
        except Exception, e:
            print Exception, ":", e
            traceback.print_exc()