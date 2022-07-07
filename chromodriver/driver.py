from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument("--headless")

driver = webdriver.Chrome(executable_path='/home/user/PycharmProjects/avtotest/chromedriver', options=options)