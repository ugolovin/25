import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_have_different_names(go_to_my_pets):
   '''Проверяем что на странице со списком питомцев пользователя, у всех питомцев разные имена'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   pytest.driver.implicitly_wait(10)

   list_name_pets = []
   for i in range(len(pet_data)):
       list_name_pets.append(pet_data[i].text)
   set_pet_data = set(list_name_pets)
   assert len(list_name_pets) == len(set_pet_data)

# python -m pytest -v --driver Chrome --driver-path \web_driver\chromedriver.exe tests/test_all_pets_have_different_name.py