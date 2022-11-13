# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://chromedino.com/")
# headlines = driver.find_elements_by_class_name("story-heading")
# for headline in headlines:
#     print(headline.text.strip())

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class GameControl():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        self.DINO_URL="https://chromedino.com/"
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_network_conditions(offline=True, latency=5, throughput=500 * 1024)
        self.actionChains = ActionChains(self.driver)
        self.driver.get(self.DINO_URL)

    def close_game(self):
        self.driver.close()

    def start_game(self):
        print("Starting game...")
        self.actionChains.send_keys(Keys.SPACE).perform()


GameControl()