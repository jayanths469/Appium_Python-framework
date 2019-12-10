
import capablities
from appium import webdriver
Desiredcap = {}
Desiredcap['platformName'] = capablities.platform
Desiredcap['platformVersion'] = capablities.platfromversion
Desiredcap['deviceName'] = capablities.devicename
Desiredcap['appPackage'] = capablities.apppackage
Desiredcap['appActivity'] = capablities.appactivity
driver = webdriver.Remote('http://localhost:4723/wd/hub', Desiredcap)

driver.wait_activity("//*[@text='OK']",10)

elemnet = driver.find_element_by_xpath("//*[@text='OK']")


text = elemnet.text

print(text)