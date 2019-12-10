""""Appium framework for Android and IOS"""

import capablities
from appium import webdriver
Desiredcap = {}
Desiredcap['platformName'] = capablities.platform
Desiredcap['platformVersion'] = capablities.platfromversion
Desiredcap['deviceName'] = capablities.devicename
Desiredcap['appPackage'] = capablities.apppackage
Desiredcap['appActivity'] = capablities.appactivity
driver = webdriver.Remote('http://localhost:4723/wd/hub', Desiredcap)


tfile = open("testing.txt",'r')
line = tfile.readlines()

for val in line:
    sample = val.split('\t')
    Action = sample[0]
    Locatortype = sample[1]
    Locator = sample[2]
    Userinput = sample[3]
    #print(Action)
    #print(Locatortype)
    #print(Locator)
    try:
        if Action == "Tap" and Locatortype == "ID":
            driver.wait_activity(Locator, 120)
            driver.find_element_by_id(Locator).click()
        elif Action == "Tap" and Locatortype == "Xpath":
            driver.wait_activity(Locator, 10)
            driver.find_element_by_xpath(Locator).click()
        elif Action == "Tap" and Locatortype == "Class":
            driver.implicitly_wait(30)
            driver.find_element_by_class_name(Locator).click()
        elif Action == "Sendkeys" and Locatortype == "Xpath":
            driver.wait_activity(Locator, 10)
            driver.find_element_by_xpath(Locator).send_keys(Userinput)
            driver.hide_keyboard()

    except Exception as e:
        print(e)

