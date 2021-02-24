from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

email = "enfurtini@hotmail.com"
senha = "aventura2"
class bot():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome(".vscode/drivers/chromedriver.exe",chrome_options=chrome_options) 
    def login(self):
        self.driver.get("https://www.facebook.com/lorenzo.bellato.1/posts/2733021310259884")
    def email(self):
        self.driver.find_element_by_id("email").send_keys(email)
    def senha(self):
        self.driver.find_element_by_id("pass").send_keys(senha)
    def enter(self):
        self.driver.find_element_by_id("loginbutton").send_keys(Keys.ENTER)
    def write(self):
        self.driver.find_element_by_name("xhpc_message").send_keys("oi")
    def coment(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)
        comentário = self.driver.find_element_by_class_name("_7c-t")
        comentário.click()
        time.sleep(2)
    def comentar(self):
        self.driver.find_element_by_xpath('//*[@id="u_0_17"]/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div').send_keys("o",Keys.ENTER)
    def main(self):
        self.login()
        self.email()
        self.senha()
        self.enter()
        time.sleep(2)
        self.coment()
        # for i in range(1000):
            # self.comentar()
            # self.driver.find_element_by_xpath('//*[@id="facebook"]/body/div[10]/div[2]/div/div/div/div/div[1]/div/div[2]/div/button').click()
        
bot().main()


        
    
       