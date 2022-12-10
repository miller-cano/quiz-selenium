from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.maximize_window()

driver.get("https://www.viajesexito.com/")

#lo hice para quitar los anuncios ya que a veces salen
#time.sleep(3)

#anuncio1 = driver.find_element(By.XPATH, '/html/body/div[38]/div/div/div/div[2]/a[2]')
#anuncio1.click()

#time.sleep(3)

#anuncio2 = driver.find_element(By.XPATH, '/html/body/div[36]/div/div/div[1]/button/span')
#anuncio2.click()

paquete = driver.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[2]/a')
paquete.click()

time.sleep(2)

vuelo_hotel = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div/div/div/ul/li[1]/label/input')
vuelo_hotel.click()

time.sleep(2)

ciudadOrigen = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[1]/div/div/input')
ciudadOrigen.click()
ciudadOrigen.send_keys("Bogotá, Colombia (BOG)")
time.sleep(2)

ciudadDestino = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[1]/div/div[3]/div/div/input')
ciudadDestino.click()
ciudadDestino.send_keys("Punta Cana, Republica Dominicana (PUJ)")
time.sleep(2)

fecha = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[2]/div/div[1]')
fecha.click()
time.sleep(2)

diaIda = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[3]/td[3]/a')
diaIda.click()
time.sleep(2)

diaRegreso = driver.find_element(By.XPATH, '/html/body/div[21]/div[1]/table/tbody/tr[4]/td[4]/a')
diaRegreso.click()
time.sleep(2)

habitacion = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/p')
habitacion.click()
time.sleep(1)

sumarHabitacion = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div/div[3]/div/span[2]/button/span')
sumarHabitacion.click()
time.sleep(1)

aplicar = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[3]/div[2]/div[2]/button')
aplicar.click()
time.sleep(1)

consultar = driver.find_element(By.XPATH, '/html/body/form/div[4]/article[1]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/a')
consultar.click()
time.sleep(20)
#debe ponerle bastante tiempo hasta que cargue

precio1 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[1]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio2 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[2]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio3 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[3]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio4 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[4]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio5 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[5]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio6 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[6]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio7 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[7]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio8 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[8]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio9 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[9]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
precio10 = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[5]/div[10]/div/div/div[2]/div/div[1]/div/p[1]/span[2]').text
time.sleep(5)
print("-------------------------PRIMER PAQUETE--------------------------------------")
print(precio1)
print("-------------------------SEGUNDO PAQUETE--------------------------------------")
print(precio2)
print("-------------------------TERCER PAQUETE--------------------------------------")
print(precio3)
print("-------------------------CUARTO PAQUETE--------------------------------------")
print(precio4)
print("-------------------------QUINTO PAQUETE--------------------------------------")
print(precio5)
print("-------------------------SEXTO PAQUETE--------------------------------------")
print(precio6)
print("-------------------------SEPTIMO PAQUETE--------------------------------------")
print(precio7)
print("-------------------------OCTAVO PAQUETE--------------------------------------")
print(precio8)
print("-------------------------NOVENO PAQUETE--------------------------------------")
print(precio9)
print("-------------------------DECIMO PAQUETE--------------------------------------")
print(precio10)

aerolinea = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
aerolinea.click()
aerolinea.send_keys("Avianca (AV)")
time.sleep(1)

buscar = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
buscar.click()
time.sleep(5)

driver.quit()


