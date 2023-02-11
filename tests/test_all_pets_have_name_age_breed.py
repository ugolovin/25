import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_there_is_a_name_age_and_gender(go_to_my_pets):
   '''Проверяем что на странице со списком питомцев пользователя, у всех питомцев есть имя, возраст и порода'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   wait = WebDriverWait(pytest.driver, 5)

   for i in range(len(pet_data)):
      assert wait.until(EC.visibility_of(pet_data[i]))

   name_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[1]')
   for i in range(len(name_pets)):
      assert wait.until(EC.visibility_of(name_pets[i]))

   type_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[2]')
   for i in range(len(type_pets)):
      assert wait.until(EC.visibility_of(type_pets[i]))

   age_pets = pytest.driver.find_elements(By.XPATH, '//tbody/tr/td[3]')
   for i in range(len(age_pets)):
      assert wait.until(EC.visibility_of(age_pets[i]))

# python -m pytest -v --driver Chrome --driver-path \web_driver\chromedriver.exe tests/test_all_pets_have_name_age_breed.py