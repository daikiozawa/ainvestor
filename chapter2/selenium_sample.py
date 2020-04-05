from selenium import webdriver
import chromedriver_binary

driver = webdriver.Chrome()
driver.get('http://jp.kabumap.com/servlets/kabumap/Action?SRC=basic/top/base&codetext=4755')
unit = driver.find_element_by_css_selector('#minUnit').text
print(unit)