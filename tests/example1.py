from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service=ChromeService(ChromeDriverManager().install())
browser=webdriver.Chrome(service=service)


browser.get("https://alhymrecords.com/")
