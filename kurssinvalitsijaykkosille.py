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

selectbutton = driver.find_element(By.ID, "tray-selection-on-first-click") #löydetään pikavalintanäppäin
selectbutton.click()#painetaan sitä

firstbutton = driver.find_element(By.PARTIAL_LINK_TEXT, "3. periodi lv 2024-2025")#löydetään 3. perioidin kurssin nappi
firstbutton.click()#painetaan nappia

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "ensimmäinen kurssi joka pitää valita (xpath) ")) #odotetaan kurssin nappia
)

courseone = driver.find_element(By.XPATH, "1. valittavan kurssin xpath")#löydetään 1. rivin kurssi
courseone.click()#painetaan sitä

coursetwo = driver.find_element(By.XPATH, "2. valittavan kurssin xpath")#löydetään 2. rivin kurssi
coursetwo.click()#painetaan sitä


coursethree = driver.find_element(By.XPATH, "3. valittavan kurssin xpath")#löydetään 3. rivin kurssi
coursethree.click()#painetaan sitä

coursefour = driver.find_element(By.XPATH, "4. valittavan kurssin xpath")#löydetään 4. rivin kurssi
coursefour.click()#painetaan sitä

coursefive = driver.find_element(By.XPATH, "5. valittavan kurssin xpath")#löydetään 5. rivin kurssi
coursefive.click()#painetaan sitä

coursesix = driver.find_element(By.XPATH, "6. valittavan kurssin xpath")#löydetään 6. rivin kurssi
coursesix.click()#painetaan sitä

courseseven = driver.find_element(By.XPATH, "7. valittavan kurssin xpath")#löydetään 7. rivin kurssi
courseseven.click()#painetaan sitä

firstbutton.click()#suljetaan 3 periodin kurssit

firstbutton2 = driver.find_element(By.PARTIAL_LINK_TEXT, "4. periodi lv 2024-2025")#löydetään 4. perioidin kurssin nappi
firstbutton2.click()#painetaan nappia

courseone2 = driver.find_element(By.XPATH, "1. valittavan kurssin xpath")#löydetään 1. rivin kurssi
courseone2.click()#painetaan sitä

coursetwo2 = driver.find_element(By.XPATH, "2. valittavan kurssin xpath")#löydetään 2. rivin kurssi
coursetwo2.click()#painetaan sitä


coursethree2 = driver.find_element(By.XPATH, "3. valittavan kurssin xpath")#löydetään 3. rivin kurssi
coursethree2.click()#painetaan sitä

coursefour2 = driver.find_element(By.XPATH, "4. valittavan kurssin xpath")#löydetään 4. rivin kurssi
coursefour2.click()#painetaan sitä

coursefive2 = driver.find_element(By.XPATH, "5. valittavan kurssin xpath")#löydetään 5. rivin kurssi
coursefive2.click()#painetaan sitä

coursesix2 = driver.find_element(By.XPATH, "6. valittavan kurssin xpath")#löydetään 6. rivin kurssi
coursesix2.click()#painetaan sitä

courseseven2 = driver.find_element(By.XPATH, "7. valittavan kurssin xpath")#löydetään 7. rivin kurssi
courseseven2.click()#painetaan sitä

firstbutton2.click()#suljetaan 4 periodin kurssit

firstbutton3 = driver.find_element(By.PARTIAL_LINK_TEXT, "5. periodi lv 2024-2025")#löydetään 5. perioidin kurssin nappi
firstbutton3.click()#painetaan nappia

courseone3 = driver.find_element(By.XPATH, "1. valittavan kurssin xpath")#löydetään 1. rivin kurssi
courseone3.click()#painetaan sitä

coursetwo3 = driver.find_element(By.XPATH, "2. valittavan kurssin xpath")#löydetään 2. rivin kurssi
coursetwo3.click()#painetaan sitä


coursethree3 = driver.find_element(By.XPATH, "3. valittavan kurssin xpath")#löydetään 3. rivin kurssi
coursethree3.click()#painetaan sitä

coursefour3 = driver.find_element(By.XPATH, "4. valittavan kurssin xpath")#löydetään 4. rivin kurssi
coursefour3.click()#painetaan sitä

coursefive3 = driver.find_element(By.XPATH, "5. valittavan kurssin xpath")#löydetään 5. rivin kurssi
coursefive3.click()#painetaan sitä

coursesix3 = driver.find_element(By.XPATH, "6. valittavan kurssin xpath")#löydetään 6. rivin kurssi
coursesix3.click()#painetaan sitä

courseseven3 = driver.find_element(By.XPATH, "7. valittavan kurssin xpath")#löydetään 7. rivin kurssi
courseseven3.click()#painetaan sitä



time.sleep(10)

driver.quit()

