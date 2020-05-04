from selenium import webdriver

us='gopivenkataajay@gmail.com'
pa='123456789'
url='https://www.facebook.com/'
dr=webdriver.Chrome("/Users/gopi varma/Downloads/chromedriver")
dr.get(url)
dr.find_element_by_id('email').send_keys(us)
dr.find_element_by_id('pass').send_keys(pa)
dr.find_element_by_id('loginbutton').click()
