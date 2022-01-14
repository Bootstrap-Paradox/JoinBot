from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time


class Bot:

    def __init__(self,) -> None:
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

    def join_meeting(self, meeting_link):
        self.driver.get(meeting_link)


if __name__ == "__main__":

    bot = Bot()
    bot.join_meeting(meeting_link="https://meet.google.com/wwn-vpwo-jvc")
