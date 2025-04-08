from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Connect to Selenium WebDriver server exposed via ngrok
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities={'browserName': 'chrome'}
)

# Open a website and interact with it
driver.get("http://google.com")

# Keep the browser alive
time.sleep(10000)
