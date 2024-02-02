
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



options = webdriver.ChromeOptions()
#options.add_argument("--headless")

# Создание экземпляра веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)


# Переход на веб-страницу
driver.get("https://rhsolutions.ru/home/")

cookis = (By.XPATH, '//button[text()="Принимаю "]')
wait.until(EC.visibility_of_element_located(cookis))
driver.find_element(*cookis).click()

"""

#ФОС хедер

btn__name = (By.XPATH, '/html/body/div/div[1]/header/div/div[2]/div/div/button')
wait.until(EC.element_to_be_clickable(btn__name))
driver.find_element(*btn__name).click()

input__name = driver.find_element(By.XPATH, '//*[@id="full_name"]').send_keys("Test")

input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(11111111111)

check_box = driver.find_element(By.XPATH, '//*[@id="app-container"]/header/div/div[2]/div/div/div/div/div/div[2]/div/div/form/div[1]/div[3]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '//*[@id="app-container"]/header/div/div[2]/div/div/div/div/div/div[2]/div/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '//*[@id="app-container"]/header/div/div[2]/div/div/div/div/div/div[2]/div/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#ФОС Ответ на 10

img = driver.find_element(By.XPATH, '//*[@id="question_1"]/ul/li[1]/img').click()
button = driver.find_element(By.XPATH, '//*[@id="question_1"]/div/button').click()

img = driver.find_element(By.XPATH, '//*[@id="question_2"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_2"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_3"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_3"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_4"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_4"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_5"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_5"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_6"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_6"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_7"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_7"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_8"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_8"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_9"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_9"]/div/button[2]').click()

input = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/div[5]/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/input').send_keys(11111111111)

check_box = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[5]/div[2]/div/div[2]/div/div/form/div[1]/div[4]/label').click()

btn = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[5]/div[2]/div/div[2]/div/div/form/div[2]/button')
driver.refresh()

#ФОС

input = (By.XPATH, '/html/body/div/div[1]/main/div/div[6]/div/form/div[1]/div[2]/div/input')
wait.until(EC.visibility_of_element_located(input))
driver.find_element(*input).send_keys('11111111111')

check_box = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/div[6]/div/form/div[1]/div[3]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/div[6]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div[1]/main/div/div[6]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#ФОС футер

btn__name = (By.XPATH, '/html/body/div/div[1]/footer/div[3]/div/div[3]/div[2]/button')
wait.until(EC.visibility_of_element_located(btn__name ))
driver.find_element(*btn__name ).click()

input = driver.find_element(By.XPATH, '/html/body/div/div[1]/footer/div[3]/div/div[3]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[2]/div/input').send_keys("11111111111")

check_box = driver.find_element(By.XPATH, '/html/body/div/div[1]/footer/div[3]/div/div[3]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[3]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/footer/div[3]/div/div[3]/div[2]/div/div/div/div[2]/div/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div[1]/footer/div[3]/div/div[3]/div[2]/div/div/div/div[2]/div/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))

#Кухни деталка

driver.get("https://rhsolutions.ru/home/collections/glance/")

#ФОС 1
btn__name = (By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[1]/div/button')
wait.until(EC.visibility_of_element_located(btn__name ))
driver.find_element(*btn__name ).click()

input = (By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[1]/div/div/div/div/div[2]/div/div/form/div[1]/div[2]/div[1]/div/div/input')
wait.until(EC.visibility_of_element_located(input))
driver.find_element(*input).send_keys('11111111111')

check_box = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[1]/div/div/div/div/div[2]/div/div/form/div[1]/div[3]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '//html/body/div/div[1]/main/div/aside/div/ul/li[1]/div/div/div/div/div[2]/div/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '//*[@id="app-container"]/main/div/aside/div/ul/li[1]/div/div/div/div/div[2]/div/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#ФОС 2

btn__name = (By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[2]/div/button')
wait.until(EC.visibility_of_element_located(btn__name ))
driver.find_element(*btn__name ).click()

input = (By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[2]/div/div/div/div/div[2]/div/div/form/div[1]/div[2]/div[1]/div/div/input')
wait.until(EC.visibility_of_element_located(input))
driver.find_element(*input).send_keys('11111111111')

check_box = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[2]/div/div/div/div/div[2]/div/div/form/div[1]/div[4]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[2]/div/div/div/div/div[2]/div/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div[1]/main/div/aside/div/ul/li[2]/div/div/div/div/div[2]/div/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))

#Фос заказать мебель

driver.get("https://rhsolutions.ru/home/form-ask/")

input = (By.XPATH, '/html/body/div/div/main/div/div/div/form/div[1]/div[2]/div/input')
wait.until(EC.visibility_of_element_located(input))
driver.find_element(*input).send_keys('11111111111')

check_box = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div/div/form/div[1]/div[3]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '//*[@id="app-container"]/main/div/div/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
"""
driver.get("https://rhsolutions.ru/home/quiz/")
#ФОС Ответ на 10

img = driver.find_element(By.XPATH, '//*[@id="question_1"]/ul/li[1]/img').click()
button = driver.find_element(By.XPATH, '//*[@id="question_1"]/div/button').click()

img = driver.find_element(By.XPATH, '//*[@id="question_2"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_2"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_3"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_3"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_4"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_4"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_5"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_5"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_6"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_6"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_7"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_7"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_8"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_8"]/div/button[2]').click()

img = driver.find_element(By.XPATH, '//*[@id="question_9"]/ul/li[1]/img').click()

button = driver.find_element(By.XPATH, '//*[@id="question_9"]/div/button[2]').click()

input = driver.find_element(By.XPATH, '/html/body/div/div[1]/main/div/div[5]/div[2]/div/div[2]/div/div/form/div[1]/div[2]/div/input').send_keys(11111111111)

check_box = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[5]/div[2]/div/div[2]/div/div/form/div[1]/div[4]/label').click()

btn = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[5]/div[2]/div/div[2]/div/div/form/div[2]/button')
driver.refresh()


