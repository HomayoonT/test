import os
from seleniumbase import Driver

CHROME_PROFILE_PATH = os.path.abspath("chrome_profile")


is_new_profile = not os.path.exists(CHROME_PROFILE_PATH)
if is_new_profile:
    print("🆕 New Chrome profile created.")
    os.makedirs(CHROME_PROFILE_PATH)

driver = Driver(uc=True, headless=False, incognito=False, user_data_dir=CHROME_PROFILE_PATH)
url = "https://www.browserscan.net/bot-detection"
driver.uc_open(url)
driver.sleep(300)
driver.quit()