#haetaan kaikki kirjastot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#haetaan chromedriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

time.sleep(10) #sovellus odottaa hetken googlen avautumisen jälkeen

driver.get("https://helsinki.inschool.fi/!02716814/selection/view?") #avataan sivusto

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-frontdoor"))
)
#odotetaan sähköpostiosoite kenttää

input_element = driver.find_element(By.ID, "login-frontdoor") #löydetään sähköposti kenttä
input_element.clear()
input_element.send_keys("wilman sähköposti" + Keys.ENTER) #laitetaan sinne sähköposti ja painetaan ENTER

input_password = driver.find_element(By.ID, "password")
input_password.clear()
input_password.send_keys("wilman salasana" + Keys.ENTER)
 #tehdään sama asia salasanalle

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "3. periodi lv 2024-2025")) #odotetaan nappia
)

firstbutton = driver.find_element(By.PARTIAL_LINK_TEXT, "3. periodi lv 2024-2025")#löydetään 3. perioidin kurssin nappi
firstbutton.click()#painetaan nappia

selectbutton = driver.find_element(By.ID, "tray-selection-on-first-click") #löydetään pikavalintanäppäin
selectbutton.click()#painetaan sitä

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "ensimmäinen kurssi joka pitää valita (xpath) ")) #odotetaan kurssin nappia
)

coursetwo = driver.find_element(By.XPATH, "2. valittavan kurssin xpath")#löydetään 2. rivin kurssi
coursetwo.click()#painetaan sitä


coursethree = driver.find_element(By.XPATH, "3. valittavan kurssin xpath")#löydetään 3. rivin kurssi
coursethree.click()#painetaan sitä

coursefour = driver.find_element(By.XPATH, "4. valittavan kurssin xpath")#löydetään 4. rivin kurssi
coursefour.click()#painetaan sitä


time.sleep(10)

driver.quit()