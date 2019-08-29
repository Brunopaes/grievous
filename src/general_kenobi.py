from selenium.webdriver.common.keys import Keys
from selenium import webdriver

import time

class GeneralKenobi:
    def __init__(self):
        self.path = r'/Users/brunopaes/Desktop/grievous/data/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, options=self.options)
        self.url = 'https://web.whatsapp.com'

    def access_page(self):
        self.driver.get(self.url)

        input()

        chat = self.driver.find_element_by_xpath('//span[contains(text(),"Caralhos")]')
        chat.click()

        for i in range(10000):
            input_box = self.driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys('but the women and children too')
            input_box.send_keys(Keys.ENTER)
            time.sleep(2)

    def __call__(self, *args, **kwargs):
        self.access_page()


if __name__ == '__main__':
    GeneralKenobi().__call__()