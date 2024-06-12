import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import re


def download_image(url, save_directory, img_no):
    # Send a GET request to download the image
    response = requests.get(url)
    
    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)
    
    # Extract the image name from the URL
    image_name = f"{img_no + 1}.png"
    img_no += 1
    
    # Save the image to the specified directory
    image_path = os.path.join(save_directory, image_name)
    with open(image_path, 'wb') as image_file:
        image_file.write(response.content)
    
    return image_path


url = 'https://bim.easyaccessmaterials.com/?level=12.00'
url2 = 'https://bim.easyaccessmaterials.com/?level=12.00&p=0'
path = "/home/punit/Downloads/geckodriver"

options = webdriver.FirefoxOptions()
service = Service(path)
driver = webdriver.Firefox(options=options, service=service)
driver.get(url)
time.sleep(5)


choose_program = driver.find_element(By.ID, 'location_user')
select = Select(choose_program)
select.select_by_value('cchs')

goto_button = driver.find_element(By.ID, 'goto_selected')
goto_button.click()

geometry_book_image = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/a[1]/img[1]')
geometry_book_image.click()

driver.get(url2)
time.sleep(2)

unique_images_array = []

i = 0
img_no = 104

for i in range(100, 629):
    url = f"https://bim.easyaccessmaterials.com/?level=11.00&p={i}"
    driver.get(url)
    images = driver.find_elements(By.TAG_NAME, 'img')
    for img in images:
        src = img.get_attribute('src')
        if src.startswith('https://bim.easyaccessmaterials.com/protected/content'):
            if src not in unique_images_array:
                unique_images_array.append(src)
                print(src)
                download_image(src, './algebra_1', img_no)
                img_no += 1

            
driver.quit()
