import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\\Users\\snaagthe\\Documents\\selenium\\chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
driver.implicitly_wait(5)
driver.find_element_by_class_name('login').click()
email= driver.find_element_by_name('email_create')
email.send_keys('testing1234@yahoo.com')
driver.find_element_by_id('SubmitCreate').click()

driver.find_element_by_css_selector('input#id_gender2').click()
first_name= driver.find_element_by_xpath('//input[@id="customer_firstname"]')
first_name.send_keys('saania')
time.sleep(3)

last_name = driver.find_element_by_xpath('//input[@id="customer_lastname"]')
last_name.send_keys('Amaan')
time.sleep(3)

password= driver.find_element_by_xpath('//input[@name="passwd"]')
password.send_keys('Abc12345')
time.sleep(3)

select_day = Select(driver.find_element_by_id('days'))
select_day.select_by_value("3")
time.sleep(3)

select_month = Select(driver.find_element_by_id('months'))
select_month.select_by_value("6")
time.sleep(3)

select_year = Select(driver.find_element_by_id('years'))
select_year.select_by_value("2013")
time.sleep(3)

driver.find_element_by_id("newsletter").click()
time.sleep(3)
driver.find_element_by_id("uniform-optin").click()
time.sleep(3)

Address_Firstname=driver.find_element_by_xpath('//input[@name="firstname"]')
Address_Firstname.send_keys('Amaan')
time.sleep(3)

Address_lastname= driver.find_element_by_xpath('//input[@name="lastname"]')
Address_lastname.send_keys('Naagthe')
time.sleep(3)

company = driver.find_element_by_xpath('//input[@id="company"]')
company.send_keys('xyz')
time.sleep(3)

Address1 = driver.find_element_by_xpath('//input[@name="address1"]')
Address1.send_keys('Crandon road')
time.sleep(3)

city= driver.find_element_by_xpath('//input[@name="city"]')
city.send_keys('Sydney')
time.sleep(3)

select_state = Select(driver.find_element_by_id('id_state'))
select_state.select_by_visible_text("Florida")
time.sleep(3)

zip = driver.find_element_by_xpath('//input[@name="postcode"]')
zip.send_keys('2121')
time.sleep(3)

Mobile = driver.find_element_by_id("phone_mobile")
Mobile.send_keys('1234567888')
time.sleep(3)

alternate_address=driver.find_element_by_xpath('//input[@value="My address"]')
alternate_address.send_keys('crandon Road,2121')
time.sleep(3)

driver.find_element_by_xpath('//button[@id="submitAccount"]').click()













