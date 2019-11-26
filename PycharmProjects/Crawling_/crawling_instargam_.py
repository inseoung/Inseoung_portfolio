from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from time import sleep

driver_path = './chromedriver'
serach = input("crawling할 해시 태그를 입력하세요 : ")
url = 'https://www.instagram.com/explore/tags/'+ serach

browser = webdriver.Chrome(executable_path = driver_path)
browser.implicitly_wait(10) # browser를 전부 읽을 수 있도록 3초동안 기다린다. sleep(3)과의 차이 알기
browser.get(url)

'''
간단 메모!! 

단일게시물 긁어오기/// for 문으로 처리하자 // xpath로는 한계가있는거 같은데 그냥 태그 찾아서 진행
xpath_1 = browser.find_element_by_xpath\
    ('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[2]/a/div[1]/div[2]').click()
xpath_2 = browser.find_elements_by_class_name('C4VMK')[0]
print(type(xpath_2))
xpath_3 = xpath_2.find_elements_by_tag_name('span')[0]
print(type(xpath_3))
print(xpath_3.text)'''

'''scroll_down_code'''
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


'''slenium_check_tage'''
count_tag = len(browser.find_elements_by_class_name('_9AhH0'))

print(count_tag)

for i in range(0,count_tag):
    browser.find_elements_by_class_name('_9AhH0')[i].click()
    print(i, "번째 게시물")
    # sleep(2)
    browser.find_element_by_class_name('ckWGn').click()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
count_tag_2 = len(browser.find_elements_by_class_name('_9AhH0'))


for j in range(count_tag,count_tag_2):
    browser.find_elements_by_class_name('_9AhH0')[j].click()
    print(j, "번째 게시물")
    # sleep(2)
    browser.find_element_by_class_name('ckWGn').click()

browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
print(count_tag)
print(count_tag_2)
count_tag_3 = len(browser.find_elements_by_class_name('_9AhH0'))
print(count_tag_3)

for z in range(count_tag_2,count_tag_3):
    browser.find_elements_by_class_name('_9AhH0')[z].click()
    print(z, "번째 게시물")
    # sleep(2)
    browser.find_element_by_class_name('ckWGn').click()


print('완료')




browser.close()