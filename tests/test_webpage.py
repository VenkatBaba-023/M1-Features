import unittest
from selenium import webdriver

class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_display_greeting(self):
        self.driver.get('file:///workspaces/.run-run-51b17e1213af4098/index.html')
        self.assertIn('Hello, welcome to Goai', self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()