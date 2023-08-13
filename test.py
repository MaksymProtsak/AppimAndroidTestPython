import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
        #if self.driver:
        #    self.driver.quit()
        pass

    def test_ajax(self) -> None:
        self.driver.implicitly_wait(5)
        self.driver.find_element(AppiumBy.ID, "com.ajaxsystems:id/authHelloLogin").click()
        self.driver.implicitly_wait(2)

        self.driver.find_element(AppiumBy.ID, 'com.ajaxsystems:id/authLoginEmail').click()
        self.driver.implicitly_wait(2)

        self.driver.execute_script("mobile: performEditorAction", {"action": "qa.ajax.app."})
        self.driver.implicitly_wait(2)

        self.driver.execute_script("mobile: performEditorAction", {"action": "automation@gmail.com"})
        self.driver.implicitly_wait(2)

        self.driver.find_element(AppiumBy.ID,'com.ajaxsystems:id/authLoginPassword').click()
        self.driver.implicitly_wait(2)

        self.driver.execute_script("mobile: performEditorAction", {"action": "qa_automation"})
        self.driver.implicitly_wait(2)
        self.driver.execute_script("mobile: performEditorAction", {"action": "_password"})
        self.driver.implicitly_wait(2)

        self.driver.find_element(AppiumBy.ID,'com.ajaxsystems:id/bottomContent').click()
        self.driver.implicitly_wait(5)


        

if __name__ == '__main__':
    unittest.main()