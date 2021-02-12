from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# ID = 'turtle_with_rabbit' #인스타그램 ID
# PW = '**' #인스타그램 PW

#화면 띄우기
# browser = webdriver.Chrome('D:\\devEnvironment')

browser = webdriver.Chrome("D:\\devEnvironment\\chromedriver.exe")
browser.get("https://instagram.com")

# browser = webdriver.Firefox("D:\devEnvironment"); #geckodriver.exe 가 있는 경로
#
# browser.get("https://instagram.com")

#로딩하는 시간 기다리기
# time.sleep(2)
#
# #Login ID 속성값 찾고 입력하기
# login_id = browser.find_element_by_name('username')
# login_id.send_keys(ID)
#
# #Login PW 속성값 찾기 입력하기
# login_pw = browser.find_element_by_name('password')
# login_pw.send_keys(PW)
# login_pw.send_keys(Keys.RETURN)
#
# time.sleep(5)
#
#Created by CoinPipe