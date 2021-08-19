from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

import time

driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.0-win64\geckodriver.exe")
driver.get("https://www.cheapflightsfares.com/")
time.sleep(2)
radio_buttn=driver.find_element_by_name("optradio") # identifying the radio button
print(radio_buttn.is_selected())# verifying if the radion button is selected.

Origin_txt=driver.find_element_by_id("froCity") # identifying the text box "fromcity"
print(Origin_txt.is_displayed()) # verifying if txt is displayed in the text box

driver.find_element_by_id("froCity").click() # clicking the from city text box
Origin_txt.send_keys("Minneapolis")# entering the txt in the text box.
#Select.select_by_index("ui-id-1")

time.sleep(3)

ToCity_txt=driver.find_element_by_id("toCity") # finding the To City element
print(ToCity_txt.is_displayed()) # if text is displayed true is shown

driver.find_element_by_id("toCity").click()# clicks the "Tocity" txt box
ToCity_txt.send_keys("Lasvegas") # Enter the destination city.
time.sleep(3)
driver.find_element_by_id("search-btn-xxx").click()





#driver.quit()