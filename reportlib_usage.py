"""using reportlib framework"""

import reportlib
import unittest
import sys

class MyTestcase(unittest.TestCase):

    def setUp(self):
        self.report = reportlib.GenerateReport("myfilename.html")

    def test_mymethod(self):
        self.report.writeTableHeader("This is my sample testcase")
        self.report.writeToTable("This is my report body")
        self.report.writeTableFooter("This is end of sample testcase")

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromModule( sys.modules[__name__] )
  unittest.TextTestRunner(verbosity=3).run( suite )
