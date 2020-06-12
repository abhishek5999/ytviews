from selenium import webdriver
import time
views = int(input("enter no. of view: "))
view_time = float(input('enter time for each view: '))

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()
browser3 = webdriver.Chrome()


for i in range(views):
    browser1.get('https://youtu.be/SyaU5YJ851o')
    time.sleep(view_time)
    browser2.get('https://youtu.be/SyaU5YJ851o')
    time.sleep(view_time)
    browser3.get('https://youtu.be/SyaU5YJ851o')
    time.sleep(view_time)

browser1.close()
browser2.close()
browser3.close()
