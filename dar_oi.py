from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains 
from webdriver_manager.chrome import ChromeDriverManager
email ="enzo.furtini@etec.sp.gov.br"
senha ="R92JNtT'yiL#wDV"
class paganóis:
    def __init__(self):
        chromeoptions = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chromeoptions.add_experimental_option("prefs",prefs)
        chromeoptions.add_argument("--start-maximized")
        # chromeoptions.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chromeoptions)
    def entrar(self):
        self.driver.get("https://www.microsoft.com/pt-br/microsoft-teams/log-in")
        sleep(0.3)
        self.driver.find_element_by_class_name('c-button.f-primary.ow-slide-in.ow-slide-in-2.xs-ow-mr-0.ow-mt-25.ow-txt-trans-upper').click()
        self.driver.switch_to_window(self.driver.window_handles[1])
        sleep(2)
        self.driver.find_element_by_id('i0116').send_keys(email)
        sleep(0.5)
        self.driver.find_element_by_id('idSIButton9').click()
        sleep(2)
        self.driver.find_element_by_id('i0118').send_keys(senha)
        sleep(1)
        self.driver.find_element_by_id('idSIButton9').click()
        sleep(15)
        # self.driver.find_element_by_id('app-bar-86fcd49b-61a2-4701-b771-54728cd291fb').click()
        # sleep(2)
        # self.driver.find_element_by_class_name('cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders').send_keys("oi")
        # sleep(1)
        # self.driver.find_element_by_id('send-message-button').click()
        self.driver.find_element_by_xpath('//*[@id="favorite-teams-panel"]/div/div[1]/div[4]/div[2]/div/ng-include/div').click()
        sleep(2)
        self.driver.find_element_by_id('new-post-button').click()
        sleep(1)
        self.driver.find_element_by_class_name('cke_wysiwyg_div.cke_reset.cke_enable_context_menu.cke_editable.cke_editable_themed.cke_contents_ltr.cke_show_borders').send_keys("oi")
    def main(self):                     
        self.entrar()
        sleep(1000)
paganóis().main()