from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from time import sleep



driver_path = './chromedriver'
serach = input("crawling할 해시 태그를 입력하세요: ")
ID = input('ID: ')
password = input('password: ')

url = 'https://www.instagram.com/'
browser = webdriver.Chrome(executable_path = driver_path)
browser.implicitly_wait(10) # browser를 전부 읽을 수 있도록 3초동안 기다린다. sleep(3)과의 차이 알기
browser.get(url)

############### Login_Go ###############
t1 = browser.find_element_by_class_name("izU2O")
t2 = t1.find_element_by_tag_name("a")
t2.send_keys('\n')

browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(ID)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
sleep(5)
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

############### Search_Hashtag ###############
try :
    t3 = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
except FileNotFoundError:
    pass

t4 = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
t4.send_keys(serach)
sleep(10)
t4.send_keys('\n')
t4.send_keys(Keys.RETURN)
sleep(10)


############### Crawling_Go ###############
'''
count_tag = len(browser.find_elements_by_class_name('_9AhH0'))
print(count_tag)

for i in range(0,count_tag):
    browser.find_elements_by_class_name('_9AhH0')[i].click()
    print(i, "번째 게시물")
    sleep(2)
    browser.find_element_by_class_name('ckWGn').click()

print('완료')
'''

top_tag = browser.find_element_by_class_name('_9AhH0')
top_tag.click()

# cawling_게시글, 댓글, 해시태그, 아이디, url
# cawling_게시글, 댓글, 해시태그, 아이디, url
# cawling_게시글, 댓글, 해시태그, 아이디, url

tag = browser.find_element_by_class_name('D1AKJ')
tag_next = tag.find_element_by_tag_name('a')
tag_next.send_keys('\n')

count = 1
while count < 100000000:
    try:
        tag = browser.find_element_by_class_name('D1AKJ')

        # cawling_게시글, 댓글, 해시태그, 아이디, url
        # cawling_게시글, 댓글, 해시태그, 아이디, url
        # cawling_게시글, 댓글, 해시태그, 아이디, url

        tag_next = tag.find_elements_by_tag_name('a')[1]
        tag_next.send_keys('\n')
        count = count +1
    except FileNotFoundError:
        break




# <a class="HBoOv coreSpriteRightPaginationArrow"
# tabindex="0" href="/p/2135337168399182635/">다음</a>





#
# '''
# 간단 메모!!
# xpath로는 한계가있는거 같은데 그냥 태그 찾아서 진행
# xpath_1 = browser.find_element_by_xpath\
#     ('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div[1]/div[2]').click()
# xpath_2 = browser.find_elements_by_class_name('C4VMK')[0]
# print(type(xpath_2))
# xpath_3 = xpath_2.find_elements_by_tag_name('span')[0]
# print(type(xpath_3))
# print(xpath_3.text)'''
#
#
# '''scroll_down_code'''
# SCROLL_PAUSE_TIME = 3
#
# # Get scroll height
# last_height = browser.execute_script("return document.body.scrollHeight")
#
# while True:
#     # Scroll down to bottom
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = browser.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height
#
#
# '''slenium_check_tage'''
# count_tag = len(browser.find_elements_by_class_name('_9AhH0'))
# print(count_tag)
#
# for i in range(0,count_tag):
#     browser.find_elements_by_class_name('_9AhH0')[i].click()
#     print(i, "번째 게시물")
#     # sleep(2)
#     # browser.find_element_by_class_name('ckWGn').click()
#
#
# # if
# # browser.find_element_by_class_name('dCJp8 afkep xqRnw').click()
#
#
#
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sleep(3)
# count_tag_2 = len(browser.find_elements_by_class_name('_9AhH0'))
# print(count_tag_2)
#
# for j in range(count_tag,count_tag_2):
#     browser.find_elements_by_class_name('_9AhH0')[j].click()
#     print(j, "번째 게시물")
#     # sleep(2)
#     browser.find_element_by_class_name('ckWGn').click()
#
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# sleep(3)
# count_tag_3 = len(browser.find_elements_by_class_name('_9AhH0'))
# print(count_tag_3)
#
# for z in range(count_tag_2,count_tag_3):
#     browser.find_elements_by_class_name('_9AhH0')[z].click()
#     print(z, "번째 게시물")
#     # sleep(2)
#     browser.find_element_by_class_name('ckWGn').click()
#
#
# print('완료')
#
#
#
#
# browser.close()