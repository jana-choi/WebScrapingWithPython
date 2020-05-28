from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")

# 도움말 > Chrome 정보 > 크롬 버전 확인 가능
# https://chromedriver.chromium.org/downloads 에서 다운 받은 chromedriver.exe 파일을 지정한 폴더에 넣은 후 실행
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)

url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
driver.get(url)
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()
