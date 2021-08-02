from selenium import webdriver

netNaija_Drive = webdriver.Chrome (executable_path= 'C:/Users/Kelechi Divine/Downloads/chromedriver_win32'
                                                    '/chromedriver.exe')
netNaija_Drive.get('https://www.thenetnaija.com/videos/movies')