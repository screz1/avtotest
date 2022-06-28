from selenium import webdriver
import time


url = "https://lucesposa.com/"
driver = webdriver.Chrome(executable_path="C:\\Users\\WellDone\\PycharmProjects\\Selenium\\chromodriver\\chromodriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()