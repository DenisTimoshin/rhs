
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
#options.add_argument("--headless")

# Создание экземпляра веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)


# Переход на веб-страницу
driver.get("https://rhsolutions.develop.kokoc.tech/form/")

cookis = (By.XPATH, '//button[text()="Принимаю "]')
wait.until(EC.visibility_of_element_located(cookis))
driver.find_element(*cookis).click()



#reviewForm

input__name = driver.find_element(By.XPATH, '//*[@id="full_name"]').send_keys("Test")

input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(11111111111)

input__review = driver.find_element(By.XPATH, '//*[@id="review"]').send_keys('отзыв')

check__phone = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/form/div[1]/div[5]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '//*[@id="app-container"]/main/div/div[1]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#Продуктовая форма

input__phone = (By.XPATH, '/html/body/div/div/main/div/div[3]/div/form/div[1]/div[2]/div[1]/div/div/input')
wait.until(EC.element_to_be_clickable(input__phone))
driver.find_element(*input__phone).send_keys(11111111111)

check__box = driver.find_element(By.XPATH, '//*[@id="app-container"]/main/div/div[3]/div/form/div[1]/div[4]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[3]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[3]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()


#Инженерная форма revit-form

input__name  = (By.XPATH, '/html/body/div/div/main/div/div[4]/div/form/div[1]/div[1]/div/input')
wait.until(EC.element_to_be_clickable(input__name ))
driver.find_element(*input__name ).send_keys("Test")

input__phone = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[4]/div/form/div[1]/div[3]/div[1]/div/div/input').send_keys(11111111111)

input__email = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[4]/div/form/div[1]/div[3]/div[2]/div/div/input').send_keys("test@test.test")

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[4]/div/form/div[1]/div[6]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[4]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[4]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()


#Мебельная форма

input__phone = (By.XPATH, '/html/body/div/div/main/div/div[5]/div/form/div[1]/div[2]/div[1]/div/div/input')
wait.until(EC.element_to_be_clickable(input__phone))
driver.find_element(*input__phone).send_keys(11111111111)

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[5]/div/form/div[1]/div[3]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[5]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[5]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()



#Форма с почтовым адресом

input__phone = (By.XPATH, '/html/body/div/div/main/div/div[6]/div/form/div[1]/div[5]/div[1]/div/div/input')
wait.until(EC.element_to_be_clickable(input__phone))
driver.find_element(*input__phone).send_keys(11111111111)

input__email = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[6]/div/form/div[1]/div[5]/div[2]/div/div/input').send_keys("test@test.test")

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[6]/div/form/div[1]/div[7]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[6]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[6]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()


#Форма задать вопрос

input__email = (By.XPATH, '/html/body/div/div/main/div/div[7]/div/form/div[1]/div[2]/div[2]/div/div/input')
wait.until(EC.element_to_be_clickable(input__email))
driver.find_element(*input__email).send_keys("test@test.test")

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[7]/div/form/div[1]/div[5]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[7]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '//*[@id="app-container"]/main/div/div[7]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#Форма контакты
input__select = (By.XPATH, '/html/body/div/div/main/div/div[8]/div/form/div[1]/div[1]/div/div[2]/span')
wait.until(EC.element_to_be_clickable(input__select))
driver.find_element(*input__select).click()

input__li = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[8]/div/form/div[1]/div[1]/div/div[3]/ul/li[2]').click()

input__email = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[8]/div/form/div[1]/div[3]/div[2]/div/div/input').send_keys("test@test.test")

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[8]/div/form/div[1]/div[6]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[8]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[8]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#Форма запись на семинар

input__name  = (By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[1]/div[1]/div/input')
wait.until(EC.element_to_be_clickable(input__name ))
driver.find_element(*input__name ).send_keys("Test")


input__data = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[1]/div[3]/div/div/input').send_keys("11.11.2011")

input__phone = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[1]/div[4]/div[1]/div/div/input').send_keys(11111111111)

input__email = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[1]/div[4]/div[2]/div/div/input').send_keys("test@test.test")


check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[1]/div[6]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[9]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#Продуктовая форма 2

input__phone = (By.XPATH, '/html/body/div/div/main/div/div[10]/div/form/div[1]/div[2]/div[1]/div/div/input')
wait.until(EC.element_to_be_clickable(input__phone))
driver.find_element(*input__phone).send_keys(11111111111)

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[10]/div/form/div[1]/div[4]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[10]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[10]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()


#revit form

input__name  = (By.XPATH, '/html/body/div/div/main/div/div[11]/div/form/div[1]/div[1]/div/input')
wait.until(EC.element_to_be_clickable(input__name ))
driver.find_element(*input__name ).send_keys("Test")

input__phone = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[11]/div/form/div[1]/div[3]/div[1]/div/div/input').send_keys(11111111111)

input__email = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[11]/div/form/div[1]/div[3]/div[2]/div/div/input').send_keys("test@test.test")

check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[11]/div/form/div[1]/div[6]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[11]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[11]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()

#Тест форма

input__name  = (By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[1]/div[1]/div/input')
wait.until(EC.element_to_be_clickable(input__name ))
driver.find_element(*input__name ).send_keys("Test")

input__data = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[1]/div[3]/div/div/input').send_keys("11.11.2011")

input__phone = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[1]/div[4]/div[1]/div/div/input').send_keys(11111111111)

input__email = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[1]/div[4]/div[2]/div/div/input').send_keys("test@test.test")


check__box = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[1]/div[6]/label/span[1]').click()

btn = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[2]/button').click()

appearance_of_the_component = (By.XPATH, '/html/body/div/div/main/div/div[12]/div/form/div[2]/b')
wait.until(EC.visibility_of_element_located(appearance_of_the_component))
driver.refresh()






