from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from datetime import datetime
import time
from os import environ


class Bot:

    def __init__(self, email: str = None, password: str = None) -> None:

        self.email = email
        self.password = password

        self.options = Options()
        self.options.add_argument(
            '--disable-blink-features=AutomationControlled')
        self.options.add_argument('--start-maximized')
        self.options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 0,
            "profile.default_content_setting_values.notifications": 1
        })

        self.driver = webdriver.Chrome(options=self.options)

    def join_meeting(self, meeting_link=None):

        self.google_login(email=self.email, password=self.password)
        self.driver.get(meeting_link)
        # self.turn_off_mic_cam()
        self.join_now()
        # self.ask_to_join()

    def turn_off_mic_cam(self):

        # Microphone
        time.sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
        self.driver.implicitly_wait(3000)

        # Camera
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
        self.driver.implicitly_wait(3000)

    def join_now(self):

        time.sleep(10)
        self.driver.implicitly_wait(2000)
        # self.driver.find_element_by_css_selector(
        #     "div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt").click()
        # print(datetime.now().strftime("%H:%M:%S"))
        self.driver.find_element_by_xpath(
            "//div[@role='button']//span[contains(text(), 'Ask to join')]").click()

        # print()
        # print("button Pressed")
        # print(datetime.now().strftime("%H:%M:%S"))

    def ask_to_join(self):
        time.sleep(10)
        self.driver.implicitly_wait(2000)
        self.driver.find_element_by_css_selector(
            'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

    def google_login(self, email, password):

        # Username Field
        self.driver.get(
            'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

        self.driver.find_element_by_id("identifierId").send_keys(email)
        self.driver.find_element_by_id("identifierNext").click()
        self.driver.implicitly_wait(1000)

        # Password Field
        self.driver.find_element_by_xpath(
            '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("passwordNext").click()
        self.driver.implicitly_wait(10)

        # Try Google Home page
        self.driver.get("https://google.com/")
        self.driver.implicitly_wait(100)


if __name__ == "__main__":

    bot = Bot(email='appl11217@sanjayghodawatuniversity.ac.in',
              password=environ.get("UNI_EMAIL_PASS"))
    bot.join_meeting(meeting_link="https://meet.google.com/wwn-vpwo-jvc")
