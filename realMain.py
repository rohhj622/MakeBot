from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randint

random_wait_min = 3
random_wait_max = 10

random_next_min = 1
random_next_max = 5


def nextFeed():
    time.sleep(1)
    nextFeed = browser.find_element_by_css_selector(
        'body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
    nextFeed.click()


ID = "diamond_diealmond"
PW = "1xlaheodnl!"

browser = webdriver.Chrome("D:\\devEnvironment\\chromedriver.exe")
browser.get("https://instagram.com")

time.sleep(2)

login_id = browser.find_element_by_name('username')
login_id.send_keys(ID)

login_pw = browser.find_element_by_name('password')
login_pw.send_keys(PW)
login_pw.send_keys(Keys.RETURN)

time.sleep(5)

# popup = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
# popup.send_keys(Keys.ENTER)

time.sleep(2)


popup = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
popup.send_keys(Keys.ENTER)


# 태그 검색 하기
search = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('#맛스타그램')


# 최상위 검색 결과로 진입하기 Enter 두번으로 수행
search.send_keys(Keys.RETURN) #최상위 검색결과로 Focus 이동
search.send_keys(Keys.RETURN) #검색결과 새로운 창으로 이동]
search.send_keys(Keys.RETURN) #최상위 검색결과로 Focus 이동
search.send_keys(Keys.RETURN) #검색결과 새로운 창으로 이동]
# 첫번쨰 게시물 선택하기
time.sleep(3)
#feed = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')

feed = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[3]/div[3]/a')
feed.send_keys(Keys.ENTER)

# 좋아요 누르기
time.sleep(3)
like_list = browser.find_elements_by_xpath('//article//section/span/button')
like_list[0].click() #list 중 0번째 버튼을 선택

nextFeed()
#After
for a in range(10):
    # 좋아요 누르기
    time.sleep(3)
    like_list = browser.find_elements_by_xpath('//article//section/span/button')
    like_list[0].click() #list 중 0번째 버튼을 선택

    # 다음 피드로 이동하기
    nextFeed()