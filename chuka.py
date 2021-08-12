
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("https://chykalophia.com/capabilities/")
driver.implicitly_wait(20)
driver.maximize_window()
#linkedin
driver.get("https://www.linkedin.com/company/2329060")
driver.implicitly_wait(20)
#Facebook
driver.get("https://www.facebook.com/chykalophia/")
driver.implicitly_wait(20)
driver.maximize_window()
#Twiter
driver.get("https://twitter.com/chykalophia/")
driver.implicitly_wait(10)
driver.maximize_window()
#Youtube
driver.get("https://www.youtube.com/user/cklphgroup")
driver.implicitly_wait(15)
driver.maximize_window()
#instagram
driver.get("https://instagram.com/chykalophia/")


driver.quit()
