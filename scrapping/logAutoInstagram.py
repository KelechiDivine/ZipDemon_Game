# import webscrapping
from selenium import webdriver

chrome_path= 'C:/Users/Kelechi Divine/Downloads/chromedriver_win32'
driver= webdriver.Chrome(executable_path= chrome_path)
driver.get('https://instagram.com/account/login')


# from selenium import webdriver
#
# drive = webdriver.Chrome(executable_path='C:/Users/Kelechi Divine/Downloads/chromedriver_win32 (1)')
# drive.get('https://oxylabs.io/blog')