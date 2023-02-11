import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_no_duplicate_pets(go_to_my_pets):
    '''Проверяем что на странице со списком питомцев пользователя нет повторяющихся питомцев'''

    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    pytest.driver.implicitly_wait(10)

    list_pet_data = []
    for i in range(len(pet_data)):
        list_data = pet_data[i].text.split("\n")
        list_pet_data.append(list_data[0])
    set_data_my_pets = set(list_pet_data)
    assert len(list_pet_data) == len(set_data_my_pets)

# python -m pytest -v --driver Chrome --driver-path \web_driver\chromedriver.exe tests/test_no_duplicat_pets.py
