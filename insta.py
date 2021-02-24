from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
email = "enfurtini@hotmail.com"
senha = "aventura2"
senha_bot = "ashsbk" 
class botinsta:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default-content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs",prefs)
        chrome_options.add_argument("'--proxy-server:213.96.26.189:8080")
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument('--proxy-server=177.205.31.146')
        self.driver = webdriver.Chrome(".vscode/drivers/chromedriver.exe",chrome_options=chrome_options)
    def login(self):
        self.driver.get("https://www.instagram.com/?hl=pt-br")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
        time.sleep(0.5)
        # self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys("oi")
        time.sleep(2)
        self.driver.execute_script("window.open('https://www.fakemail.net/')")
        time.sleep(4)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(0.5)
        vh = self.driver.find_element_by_id('email').text
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(vh)
        time.sleep(0.5)
        self.driver.find_element_by_name("username").click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/div/div/div/button').click() 
        nu = self.driver.find_element_by_name("username").get_attribute("value")
        print(nu)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input').send_keys(nu)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input').send_keys(senha_bot)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/div/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[19]').click()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/div[5]/div[2]/button').click()
        """self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[6]/button/span[2]').click()
        time.sleep(1)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("pass").send_keys(senha)
        self.driver.find_element_by_name("login").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()"""
        time.sleep(100)
botinsta().login()