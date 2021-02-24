from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
x = input("Texto:")
chromeoptions = Options()
chromeoptions.add_argument('--headless')
chromeoptions.add_argument('--no-sandbox')
chromeoptions.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome("C:/Users/Enzo/Downloads/Programação Python-backup/Programação Python-backup/.vscode/chromedriver.exe",chrome_options=chromeoptions)
driver.get("https://seotoolscentre.com/sentence-rewriter")
sleep(0.5)
driver.find_element_by_id("data").send_keys(x)
sleep(0.4)
driver.find_element_by_id("checkButton").click()
sleep(2)
driver.find_element_by_id("finishButton").click()
sleep(0.7)
x2 = driver.find_element_by_id("textArea").get_attribute("value")
chromeoptions = Options()
chromeoptions.add_argument('--headless')
driver = webdriver.Chrome("C:/Users/Enzo/Downloads/Programação Python-backup/Programação Python-backup/.vscode/chromedriver.exe",chrome_options=chromeoptions)
driver.get("https://www.google.com/search?q=tradutor&oq=tradutor&aqs=chrome.0.69i59l2j0j0i433l3j0l2.2591j0j7&sourceid=chrome&ie=UTF-8")
driver.find_element_by_xpath('//*[@id="tw-source-text-ta"]').send_keys(x2)
sleep(1)
x3 = driver.find_element_by_xpath('//*[@id="tw-target-text"]/span').text
"""driver.find_element_by_id('tw-cpy-btn').click()"""
print(x3)                        