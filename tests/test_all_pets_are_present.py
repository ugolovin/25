import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
   '''Проверяем что на странице со списком питомцев пользователя присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   stat= pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets_cards = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   number_of_pets = stat[0].text.split('\n')
   number_of_pets = number_of_pets[1].split(' ')
   number_of_pets = int(number_of_pets[1])

   number_of_cards = len(pets_cards)

   pytest.driver.implicitly_wait(10)

   assert number_of_pets == number_of_cards

# python -m pytest -v --driver Chrome --driver-path \web_driver\chromedriver.exe tests/test_all_pets_are_present.py