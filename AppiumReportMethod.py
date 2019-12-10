"""Reporting class for usage."""

class GenerateReport:

    def __init__(self, filename):
        self.logto_report = open(filename, 'w')
        self.logto_report.write(self.addPreTextToReport())

    def addPreTextToReport(self):
        text = '''<html lang="en">
        <head><title>Automation Report
        </title></head>
        <body>
        <div align="center">
        Automation Testing Report.
        </div>
        '''
        return text

    def writeTableHeader(self, msg):
        text = '<table width="100%" border="1"><tr><th border="1"> ' + msg +' </th></tr>'
        self.logto_report.write(text)
        text = '<tr><td><b>Description</b></td></tr>'
        self.logto_report.write(text)


    def writeTableFooter(self, msg):
        text = '<tr><td><b>' + msg +' </b></td></tr></table>'
        self.logto_report.write(text)


    def writeToTable(self, msg):
        text = '<tr><td >' + msg + '</td></tr>'
        self.logto_report.write(text)
    def Statusreport(self,msg):
        text = '<col><td >' + msg + '</td></col>'
        self.logto_report.write(text)

if __name__ == "__main__":
    log_report = GenerateReport("sample_report.html")
    log_report.writeTableHeader("XXX Test case")
    log_report.writeToTable("XX step running.")
    log_report.writeTableFooter("End of XXX Test case ")
    log_report.Statusreport("xxx testing new now")

