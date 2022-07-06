#Name: Andy Yang
#Organization: Bluebonnet Data
#Coding Language: Python

##Imported Libraries
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import time

##Loading Chromedriver and Retrieving Document from the listed URL.
driver = webdriver.Chrome()

driver.get("https://www.sterling-heights.net/formcenter/temporary-short-term-signs-registration-form-18/short-term-temporary-sign-registration-67")

### Current Date ###
today = date.today()
d1 = today.strftime("%m/%d/%Y")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_4_date"]'))).send_keys(d1)

### Name ###
full_name = "Aisha Farooqi for State Representative"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_6"]'))).send_keys(full_name)

### Email ###
full_email = "info@farooqifor57.com"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_17"]'))).send_keys(full_email)

### Address ###
full_address = "P.O. Box #7 Sterling Heights, MI 48311"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_15"]'))).send_keys(full_address)

### Phone Number ###
full_phone = "734-544-5494"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_36"]'))).send_keys(full_phone)

### Sign Type Element (Radio Button) ###
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_9_1"]'))).click()

### Size (Square Footage) of Sign ###
full_sqft = "2' x 4'"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_16"]'))).send_keys(full_sqft)

### Description/Identification of Sign ###
full_description = 'Aisha Farooqi for State Representative in Blue and Pink'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_41"]'))).send_keys(full_description)

### Occupancy Status (Radio Buttons) ###
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_18_1"]'))).click()

### Begin Sign Registration - Immediately (Radio Buttons) ###
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_50_0"]'))).click()

### Signature of Person ###
full_signature = 'Shania Chehab'
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="e_55"]'))).send_keys(full_signature)
