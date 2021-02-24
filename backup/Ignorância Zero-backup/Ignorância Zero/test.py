from selenium import webdriver

driver = webdriver.Chrome(".vscode/drivers/chromedriver.exe")
driver.set_page_load_timeout(5)
driver.get()
driver.find_element_by_name()