import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_photo_availability(go_to_my_pets):
   '''Проверяем что на странице со списком питомцев пользователя хотя бы у половины питомцев есть фото'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   stat = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   number_of_pets = stat[0].text.split('\n')
   number_of_pets = number_of_pets[1].split(' ')
   number_of_pets = int(number_of_pets[1])

   half = number_of_pets // 2

   pytest.driver.implicitly_wait(10)

   number_of_photos = 0
   for i in range(len(images)):

      if images[i].get_attribute('src') != '':
         number_of_photos += 1

   assert number_of_photos >= half

# python -m pytest -v --driver Chrome --driver-path \web_driver\chromedriver.exe tests/test_half_of_the_pets_have_a_photo.py