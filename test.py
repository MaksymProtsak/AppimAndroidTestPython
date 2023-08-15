import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy



capabilities = dict(
    autoGrantPermissions = True,
    newCommandTimeout= 500,
    noSign = True,
    resetKeyboard = True,
    # systemPort = 8301,
    takesScreenshot= True,
    udid = 'BV9100EEA00042406',
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.ajaxsystems',
    appActivity='com.ajaxsystems.ui.activity.LauncherActivity',
    # language='en',
    # locale='US'
    
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        # if self.driver:
        #    self.driver.quit()
        pass

    def testLogIn(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(AppiumBy.ID, "com.ajaxsystems:id/authHelloLogin").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(AppiumBy.ID, 'com.ajaxsystems:id/authLoginEmail').click()
        self.driver.implicitly_wait(2)

        self.driver.execute_script("mobile: performEditorAction", {"action": "qa.ajax.app."})
        self.driver.implicitly_wait(2)

        self.driver.execute_script("mobile: performEditorAction", {"action": "automation@gmail.com"})
        self.driver.implicitly_wait(2)

        # Python
        # from appium.webdriver.common.touch_action import TouchAction
        # actions = TouchAction(self.driver)
        # actions.long_press(self.driver.find_element(AppiumBy.ID, 'com.ajaxsystems:id/authLoginEmail'), duration=2000)
        # self.driver.implicitly_wait(5)

        # actions.perform()

        from selenium.webdriver.common.action_chains import ActionChains
        from selenium.webdriver.common.keys import Keys
        action = ActionChains(self.driver)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').perform()
        ActionChains(self.driver).key_down(Keys.DELETE).perform()
        ActionChains(self.driver).send_keys('qa.ajax.app.automation@gmail.com').perform()



        self.driver.implicitly_wait(5)





        # self.driver.find_element(AppiumBy.ID,'com.ajaxsystems:id/authLoginPassword').click()
        # self.driver.implicitly_wait(2)

        # self.driver.execute_script("mobile: performEditorAction", {"action": "qa_automation"})
        # self.driver.implicitly_wait(2)
        # self.driver.execute_script("mobile: performEditorAction", {"action": "_password"})
        # self.driver.implicitly_wait(5)

        # self.driver.find_element(AppiumBy.ID,'com.ajaxsystems:id/bottomContent').click()

        # screenSize=self.driver.get_window_size()
        # print(screenSize)

        # self.driver.implicitly_wait(20)
        # try:
        #     self.assertIsNotNone(self.driver.find_element(AppiumBy.ID, 'com.ajaxsystems:id/menuDrawer'))
        #     print('com.ajaxsystems:id/menuDrawer','<<< finded')  
        # except:
        #     print('com.ajaxsystems:id/menuDrawer','<<< not foud')  
        #     return False
        # self.driver.swipe(0,screenSize['height']/2,screenSize['width']/2,screenSize['height']/2,200)
if __name__ == '__main__':
    unittest.main()