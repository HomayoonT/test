from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://www.browserscan.net/bot-detection"
driver.uc_open(url)
driver.sleep(10000)
driver.quit()