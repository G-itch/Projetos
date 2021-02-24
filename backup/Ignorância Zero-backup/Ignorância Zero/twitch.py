from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
user = "ka0zs"
class bot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(".vscode/drivers/chromedriver.exe",chrome_options=chrome_options) 
    def login(self):
        self.driver.get("https://www.twitch.tv/dougdougw")
    def entrar(self):
        self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button').click()
    def senha(self):
        sleep(7)
        self.driver.find_element_by_id("login-username").send_keys(user)
    def enter(self):
        self.driver.find_element_by_id("password-input").send_keys("aventura2")
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/button').send_keys(Keys.ENTER)
        self.driver.execute_script("window.open('https://outlook.live.com/mail/0/inbox')")
        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_xpath('/html/body/header/div/aside/div/nav/ul/li[2]/a').click()
        try:
            self.driver.switch_to_window(self.driver.window_handles[2])
        except:
            pass
        sleep(5)
        self.driver.find_element_by_id('i0116').send_keys("enfurtini@hotmail.com")
        self.driver.find_element_by_id('idSIButton9').click()
        self.driver.find_element_by_id("i0118").send_keys("aventura2")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        sleep(4)
        self.driver.find_element_by_id('Pivot33-Tab1').click

"""bot = bot()

bot.login()
bot.entrar()
bot.senha()
bot.enter()"""
 