from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
x = input("Texto:")
chromeoptions = Options()
"""chromeoptions.add_argument('--headless')
chromeoptions.add_argument('--no-sandbox')
chromeoptions.add_argument('--disable-dev-shm-usage')"""
driver = webdriver.Chrome("C:/Users/Enzo/Downloads/Programação Python-backup/Programação Python-backup/.vscode/chromedriver.exe",chrome_options=chromeoptions)
driver.get("https://www.prepostseo.com/article-rewriter?rewriter=advanced")
sleep(0.5)
driver.find_element_by_id('input-content').send_keys(x)
sleep(1)
driver.find_element_by_id('checkB').click()
                            