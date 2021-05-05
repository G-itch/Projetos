from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
email = "enfurtini@hotmail.com"
senha = "aventura2"
class coment:
    def __init__(self):
        chromeoptions = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chromeoptions.add_experimental_option("prefs",prefs)
        chromeoptions.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome("C:/Users/Enzo/Downloads/Programação Python-backup/Programação Python-backup/.vscode/chromedriver_win32 (4)/chromedriver.exe",chrome_options=chromeoptions) 
    def login(self):
        self.driver.get("https://www.microsoft.com/pt-br/microsoft-teams/log-in")
    def email(self):
        self.driver.find_element_by_id("email").send_keys(email)
    def senha(self):
        self.driver.find_element_by_id("pass").send_keys(senha)
    def enter(self):
        self.driver.find_element_by_id("loginbutton").send_keys(Keys.ENTER)
    def scan(self):
        # não está funcionando mais / self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        sleep(2)
        t = "kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql"
        t = t.replace(" ",".")
        comentários = self.driver.find_elements_by_class_name(t)
        for i in comentários:
            print(i.text)
        sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="u_0_19"]/div/div[2]/div[1]/div/div[1]/a/span[2]').click()
        # sleep(5)
        c = ('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l')
        c = c.replace(" ",".")
        reações = self.driver.find_elements_by_class_name(c)
        for j in reações:
            print(j.get_attribute('aria-label'))  
        sleep(2)  
        xw = ('oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 a8c37x1j p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl l9j0dhe7 abiwlrkh p8dawk7l gmql0nx0 frigt3m8 ni8dbmo4 stjgntxs')
        xw = xw.replace(" ",".")
        self.driver.find_element_by_class_name(xw).click()
        sleep(2)                           
        Actions = ActionChains(self.driver)
        # Actions.move_to_element(self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]'))
        Actions.click(self.driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]')).perform()
        for i in range(10):
            Actions.send_keys(Keys.DOWN).perform()
        sleep(2)
        r = self.driver.find_elements_by_class_name('q9uorilb')
        for f in r:
            c2 = 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p'
            c2 = c2.replace(" ",".")
            pessoas = f.find_elements_by_class_name(c2)
            for r in pessoas:       
                print(r.text)       
    def main(self):
        self.login()
        self.email()
        self.senha()
        self.enter()
        self.scan()
        sleep(1000)
coment().main()
