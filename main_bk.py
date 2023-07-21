# author: Viper
# time: 2020/7/2 12:03

# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class Qiangke(object):
    login_url = "https://nyit.okta.com/login/login.htm?fromURI=%2Fapp%2Fnyit_modo_1%2Fexk5x84tnsIkhW4Qp4x7%2Fsso%2Fsaml%3FSAMLRequest%3DlVLbjtowEP2VyO%252BJcyVgARJdtFqkbUsX2pX6glxnKBaxnXomLfx9Tei22xekfbJ0POcyRzNFadpOLHo62Cf40QNSdDKtRTF8zFjvrXASNQorDaAgJTaL948iT1LReUdOuZa9otxmSETwpJ1l0Wo5Y7s6LytZ5nldTVKAskrHmRpNRoVU%252B0lR52NVjOS%252BrkEWLPoCHgNzxoJQoCP2sLJI0lKA0ryI0zrOsm02FtlEVMVXFi3DNtpKGlgHog4F5%252FasKXFHkolyhsuuG5CdcY3bZRxOx%252Bo0Lsni6nh4Lj915anmiI5fdmPR4iX%252FnbPYG%252FAb8D%252B1gs9Pj%252F8czDkZTKDp%252Be7C40G8byHpDt2gw%252FH65rFU%252BBdl0fpPn%252B%252B0bbT9frvKb9chFA%252Fb7Tpef9xs2Xx60RFDNX7%252BpjgGSDYylPICTvlrren1TD6EFKvl2rVanaN7542k2yEviG7i%252FTAqyEuLGiyFItvW%252FbrzIAlmjHwPjM%252Bvlv8f4%252Fw3%26RelayState%3Dhttps%253A%252F%252Fmy.nyit.edu%252Fkurogo_login%252Freturn%252Flogin%252Fsaml%253F_kgologin_state%253D7680d2f6-4eae-4f87-94b6-478c1d59f728"  #登录页面，修改成你学校的登录地址
    home_page = "https://my.nyit.edu/default/default_home/index"#修改为登录成功后的界面
    home_page_alternative = "https://my.nyit.edu/_kgo_default/kurogo_login/index?_kgologin_auto_redirect=0"#修改为登录成功后的界面2
    student_hub_authen = "https://nyitcs.nyit.edu/sso/sso.php?link=student"
    student_hub = "https://nyitcs.nyit.edu/psc/ps/EMPLOYEE/SA/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL"
    my_registration_entry = "https://nyitcs.nyit.edu/psc/ps_12/EMPLOYEE/SA/c/SSR_STUDENT_FL.SSR_MD_SP_FL.GBL?Action=U&MD=Y&GMenu=SSR_STUDENT_FL&GComp=SSR_START_PAGE_FL&GPage=SSR_START_PAGE_FL&scname=CS_SSR_MANAGE_CLASSES_NAV&1"
    #修改为你选课的界面
    user_name = u"xxxx"  #NYIT user name
    pwd = 'xxxxx'   #NYIT password

    def __init__(self):
        print("Start")
    def login(self):
        self.driver.get(self.login_url)
        self.driver.find_element("name", "username").send_keys(self.user_name)
        self.driver.find_element("name", "password").send_keys(self.pwd)
        self. driver.find_element("id", "okta-signin-submit").click()
        sleep(2)
        self.driver.get(self.student_hub_authen)
        print("Successfully login.")

    def swap_courses(self, first_time):
        self.driver.find_element("id", "SCC_LO_FL_WRK_SCC_VIEW_BTN$IMG$6").click()
        sleep(2)
        # self.driver.find_elements("id", "TERM_LINK$1").click()
        if first_time:
            try:
                print("try to press Fall 2023")
                self.driver.find_element("id", "ACAD_CAR_TBL_DESCR$1").click()
                print("Successfully pressed Fall 2023")
                sleep(1)
                first_time = False
            except NoSuchElementException as e:
                pass
        select = Select(self.driver.find_element("id", "DERIVED_REGFRM1_DESCR50$4$"))
        select.select_by_value('3166') #Input the class number you have and want to swap (Class number is not course number)
        select = Select(self.driver.find_element("id", "DERIVED_REGFRM1_SSR_CLASSNAME_35"))
        select.select_by_value('3205') #Input the class number you want to register (Class number is not course number)
        sleep(1)
        self.driver.find_element("id", "SSR_SWAP_FL_WRK_SSR_PB_SRCH").click()
        sleep(1)
        self.driver.find_element("id", "SSR_ENRL_FL_WRK_SUBMIT_PB").click()
        sleep(1)
        self.driver.find_element("id", "#ICYes").click()


    def select_courses(self):
        print("Start to select courses")
        self.driver.find_element("id", "SCC_LO_FL_WRK_SCC_VIEW_BTN$IMG$3").click()
        print("Successfully click cart")
        sleep(4)
        self.driver.find_element("id", "DERIVED_REGFRM1_SSR_SELECT$0").click()
        self.driver.find_element("id", "DERIVED_REGFRM1_SSR_SELECT$1").click()
        self.driver.find_element("id", "DERIVED_REGFRM1_SSR_SELECT$3").click()
        self.driver.find_element("id", "DERIVED_SSR_FL_SSR_ENROLL_FL").click()
        print("Successfully submit")
        self.driver.find_element("id", "#ICYes").click()
    def registration(self):
            sleep(1)
            self.driver.get(self.my_registration_entry)
            print("Successfully go to my_registration.")

    def start(self):
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.implicitly_wait(10)  # seconds
        self.login()
        self.registration()
        # self.driver.find_element("name", "select").click()
        #
        # self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="mainFrame"]'))
        # self.driver.find_element_by_id('kcxx').send_keys(self.class_name)
        # self.driver.find_element_by_id('skls').send_keys(self.teacher_name)
        # self.driver.find_element_by_value(u"查询").click()
        #
        # cnt = 1
        first_time = True
        while True:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print("Current time:", current_time)
            try:
                sleep(2)
                self.swap_courses(first_time)
                # sleep(5)
                # self.select_courses()
            except Exception as e:
                # print(f"Unexpected exception: {e}")
                self.registration()
            if first_time:
                first_time = False

if __name__ == "__main__":
    qiangke = Qiangke()
    qiangke.start()

