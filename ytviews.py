from selenium import webdriver
import time
views = int(input("enter no. of view: "))
view_time = float(input('enter time for each view: '))

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()
browser3 = webdriver.Chrome()

# put video link in ''
for i in range(views):
    browser1.get('')
    time.sleep(view_time)
    browser2.get('')
    time.sleep(view_time)
    browser3.get('')
    time.sleep(view_time)

browser1.close()
browser2.close()
browser3.close()
# script by abhishek5999
