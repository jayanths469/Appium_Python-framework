""""Appium framework for Android and IOS"""
import capablities
from appium import webdriver
import AppiumReportMethod
import unittest
import sys
import xlwt
Desiredcap = {}
Desiredcap['platformName'] = capablities.platform
Desiredcap['platformVersion'] = capablities.platfromversion
Desiredcap['deviceName'] = capablities.devicename
Desiredcap['appPackage'] = capablities.apppackage
Desiredcap['appActivity'] = capablities.appactivity
driver = webdriver.Remote('http://localhost:4723/wd/hub', Desiredcap)

##if capablities.platform == "IOS":
    ##driver = webdriver.Remote('http://localhost:4723/wd/hub', Desiredcap)

tfile = open("Mobile Object rep.txt",'r')
line = tfile.readlines()

TextReport = open("TestResult.txt",'a')
TextReport.truncate(0)
TextReport.writelines("Locatorname" + '\t' + "Action" + '\t' + "Status" + '\t' + "Locator" + '\t' + "ReadText" + '\n')

report = AppiumReportMethod.GenerateReport("Testreport.html")
report.writeTableHeader("Test Report Starting")

for val in line[1:]:
    sample = val.split('\t')
    Locatorname = sample[0]
    Action = sample[1]
    Userinput = sample[2]
    Xpath = sample[3]
    ID = sample[4]
    Elclass = sample[5]
    Accessibility = sample[6]
    css = sample[7]
    Standardwait = sample[8]

    try:
        if Action == "Tap":
            if Xpath != "":
                driver.wait_activity(Xpath, 10)
                driver.find_element_by_xpath(Xpath).click()
                report.writeToTable("Taped on" + Xpath + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Xpath + '\n')

            elif ID != "":
                driver.wait_activity(ID, 10)
                driver.find_element_by_id(ID).click()
                report.writeToTable("Taped on" + ID + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + ID + '\n')

            elif Elclass != "":
                driver.wait_activity(Elclass, 10)
                driver.find_element_by_class_name(Elclass).click()
                report.writeToTable("Taped on" + Elclass + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Elclass + '\n')
            elif Accessibility != "":
                driver.wait_activity(Accessibility, 10)
                driver.find_element_by_accessibility_id(Accessibility).click()
                report.writeToTable("Taped on" + Accessibility + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Accessibility + '\n')
            elif css != "":
                driver.wait_activity(css,10)
                driver.find_element_by_css_selector(css).click()
                report.writeToTable("Taped on" + css + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + css + '\n')
        if Action == "Sendkeys":
            if Xpath != "":
                driver.wait_activity(Xpath, 10)
                driver.find_element_by_xpath(Xpath).clear()
                driver.find_element_by_xpath(Xpath).send_keys(Userinput)
                driver.hide_keyboard()
                report.writeToTable("Enter the user defined text which is on :" + Xpath + "User defined text : " + Userinput + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Xpath + '\n')

            elif ID != "":
                driver.wait_activity(ID, 10)
                driver.find_element_by_id(ID).clear()
                driver.find_element_by_id(ID).send_keys(Userinput)
                driver.hide_keyboard()
                report.writeToTable("Enter the user defined text which is :" + ID + + "User defined text : " + Userinput + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + ID + '\n')
            elif Elclass != "":
                driver.wait_activity(Elclass, 10)
                driver.find_element_by_class_name(Elclass).clear()
                driver.find_element_by_class_name(Elclass).send_keys(Userinput)
                driver.hide_keyboard()
                report.writeToTable("Enter the user defined text which is :" + Elclass +  "User defined text : " + Userinput + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Elclass + '\n')
            elif Accessibility != "":
                driver.wait_activity(Accessibility, 10)
                driver.find_element_by_accessibility_id(Accessibility).clear()
                driver.find_element_by_accessibility_id(Accessibility).send_keys(Userinput)
                driver.hide_keyboard()
                report.writeToTable("Enter the user defined text which is :" + Accessibility + "User defined text : " + Userinput + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Accessibility + '\n')
            elif css != "":
                driver.wait_activity(css,10)
                driver.find_element_by_css_selector(css).clear()
                driver.find_element_by_css_selector(css).send_keys(Userinput)
                driver.hide_keyboard()
                report.writeToTable("Enter the user defined text which is :" + css + "User defined text : " + Userinput + ": Status : Pass")
                #report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + css + '\n')
        if Action == "Standardwait":
            implictwait = Standardwait
            driver.implicitly_wait(implictwait)
           # Implicitwait = Standardwait
            #print(Standardwait)
            report.writeToTable("Waited for user defined time ")
            TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Waited user defined time" + '\t' + css + '\n')

        if Action == "GetText":
            if Xpath != "":
                driver.wait_activity(Xpath, 10)
                Readvalue = driver.find_element_by_xpath(Xpath)
                Readtext = Readvalue.tex
                #report.Statusreport(Locatorname + ": Pass")

                if Readtext == Userinput:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Xpath + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + Xpath + ": Status : Pass" + " Text: " + Readtext)
                else:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Fail" + '\t' + Xpath + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + Xpath + ": Status : Fail --  Expected is not equal to Actual text"  + " Text: " + Readtext)
            elif ID != "":
                driver.wait_activity(ID, 10)
                Readvalue = driver.find_element_by_id(ID)
                Readtext = Readvalue.text

                # report.Statusreport(Locatorname + ": Pass")
                if Readtext == Userinput:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + ID + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + ID + ": Status : Pass" + " Text: " + Readtext)
                else:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Fail" + '\t' + ID + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + ID + ": Status : Fail --  Expected is not equal to Actual text" + " Text: " + Readtext)

            elif Elclass != "":
                driver.wait_activity(Elclass, 10)
                Readvalue = driver.find_element_by_id(Elclass)
                Readtext = Readvalue.text()

                # report.Statusreport(Locatorname + ": Pass")
                if Readtext == Userinput:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Elclass + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + Elclass + ": Status : Pass" + " Text: " + Readtext)
                else:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Fail" + '\t' + Elclass + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + Elclass + ": Status : Fail --  Expected is not equal to Actual text" + " Text: " + Readtext)

            elif Accessibility != "":
                driver.wait_activity(Accessibility, 10)
                Readvalue = driver.find_element_by_id(Accessibility)
                Readtext = Readvalue.text()

                # report.Statusreport(Locatorname + ": Pass")
                if Readtext == Userinput:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + Accessibility + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + Accessibility + ": Status : Pass" + " Text: " + Readtext)
                else:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Fail" + '\t' + Accessibility + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + Accessibility + ": Status : Fail --  Expected is not equal to Actual text" + "Text: " + Readtext)
            elif css != "":
                driver.wait_activity(css, 10)
                Readvalue = driver.find_element_by_id(css)
                Readtext = Readvalue.text()

                # report.Statusreport(Locatorname + ": Pass")
                if Readtext == Userinput:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Pass" + '\t' + css + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + css + ": Status : Pass" + "Text: " + Readtext)
                else:
                    TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Fail" + '\t' + css + '\t' + Readtext + '\n')
                    report.writeToTable("Taped on" + css + ": Status : Fail --  Expected is not equal to Actual text" + " Text: " + Readtext)
        if Action == "closeDriver":
            driver.close()
        if Action == "Screenshot":
            driver.save_screenshot(Userinput + ".png")
            #driver.save_screenshot('' + Userinput + ".png")
        if Action == "Scroll":
            if Xpath != "":
                el = driver.find_element_by_xpath(Xpath)
                driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
                report.writeToTable("Scrolled" + Xpath + ": Status : Pass")
                # report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Scrolled" + '\t' + Xpath + '\n')
            if ID != "":
                el = driver.find_element_by_id(ID)
                driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
                report.writeToTable("Scrolled" + ID + ": Status : Pass")
                # report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Scrolled" + '\t' + ID + '\n')
            if Elclass != "":
                el = driver.find_element_by_class_name(Elclass)
                driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
                report.writeToTable("Scrolled" + Elclass + ": Status : Pass")
                # report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Scrolled" + '\t' + Elclass + '\n')
            if Accessibility != "":
                el = driver.find_element_by_accessibility_id(Accessibility)
                driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
                report.writeToTable("Scrolled" + Accessibility + ": Status : Pass")
                # report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Scrolled" + '\t' + Accessibility + '\n')
            if css != "":
                el = driver.find_element_by_css_selector(css)
                driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
                report.writeToTable("Scrolled" + css + ": Status : Pass")
                # report.Statusreport(Locatorname + ": Pass")
                TextReport.writelines(Locatorname + '\t' + Action + '\t' + "Scrolled" + '\t' + css + '\n')

    except Exception as error:
        failreason = str(error)
        report.writeToTable("Script failed with exception" + failreason)
        TextReport.writelines("" + '\t' + "" + '\t' + "Script failed with exception" + failreason + '\t' + "" + '\t' + "" + '\n')

TextReport.close()
book = xlwt.Workbook()
ws = book.add_sheet('First Sheet')  # Add a sheet

excelfile = open("TestResult.txt", 'r+')

data = excelfile.readlines() # read all lines at once
for i in range(len(data)):
  row = data[i].split()

  for j in range(len(row)):
    ws.write(i, j, row[j])  # Write to cell i, j

book.save('TestResult' + '.xls')
excelfile.close()

report.writeTableFooter("###### End of Test Execution #########")





