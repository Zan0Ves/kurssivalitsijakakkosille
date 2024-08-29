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

time.sleep(3) #sovellus odottaa hetken googlen avautumisen jälkeen

driver.get("https://helsinki.inschool.fi/!02716814/selection/view?") #avataan sivusto

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login-frontdoor"))
)
#odotetaan sähköpostiosoite kenttää

input_element = driver.find_element(By.ID, "login-frontdoor") #löydetään sähköpostin kenttä
input_element.clear()
input_element.send_keys("Wilman sähköposti" + Keys.ENTER) #laitetaan sinne sähköposti ja painetaan ENTER

input_password = driver.find_element(By.ID, "password") #löydetään salasanan kenttä
input_password.clear()
input_password.send_keys("Wilman salasana" + Keys.ENTER) #laitetaan sinne salasana ja painetaan ENTER
 
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "3. periodi lv 2024-2025")) #odotetaan 3. periodin kurssejen nappia
)

selectbutton = driver.find_element(By.ID, "tray-selection-on-first-click") #löydetään pikavalintanäppäin
selectbutton.click()#painetaan sitä

firstbutton = driver.find_element(By.PARTIAL_LINK_TEXT, "3. periodi lv 2024-2025")#löydetään 3. perioidin kurssin nappi
firstbutton.click()#painetaan nappia

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "1. rivin kurssin Xpath")) #odotetaan 1. kurssin nappia
)

courseone = driver.find_element(By.XPATH, "1. rivin kurssin Xpath")#löydetään 1. rivin kurssi
courseone.click()#painetaan sitä

coursetwo = driver.find_element(By.XPATH, "2. rivin kurssin Xpath")#löydetään 2. rivin kurssi
coursetwo.click()#painetaan sitä

coursethree = driver.find_element(By.XPATH, "3. rivin kurssin Xpath")#löydetään 3. rivin kurssi
coursethree.click()#painetaan sitä

coursefour = driver.find_element(By.XPATH, "4. rivin kurssin Xpath")#löydetään 4. rivin kurssi
coursefour.click()#painetaan sitä

coursefive = driver.find_element(By.XPATH, "5. rivin kurssin Xpath")#löydetään 5. rivin kurssi
coursefive.click()#painetaan sitä

coursesix = driver.find_element(By.XPATH, "6. rivin kurssin Xpath")#löydetään 6. rivin kurssi
coursesix.click()#painetaan sitä

courseseven = driver.find_element(By.XPATH, "7. rivin kurssin Xpath")#löydetään 7. rivin kurssi
courseseven.click()#painetaan sitä

firstbutton.click()#suljetaan 3. periodin kurssit

time.sleep(0.5) #odotetaan puoli sekuntia, jotta 4. periodin kurssit ehtivät latautua

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/ul[1]/li[4]/a")) #odotetaan 4. periodin nappia
)

firstbuttona = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/ul[1]/li[4]/a")#löydetään 4. perioidin nappi
firstbuttona.click()#painetaan nappia

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "1. rivin kurssin Xpath")) #odotetaan 1. kurssin nappia
)

courseonea = driver.find_element(By.XPATH, "1. rivin kurssin Xpath")#löydetään 1. rivin kurssi
courseonea.click()#painetaan sitä

coursetwoa = driver.find_element(By.XPATH, "2. rivin kurssin Xpath")#löydetään 2. rivin kurssi
coursetwoa.click()#painetaan sitä

coursethreea = driver.find_element(By.XPATH, "3. rivin kurssin Xpath")#löydetään 3. rivin kurssi
coursethreea.click()#painetaan sitä

coursefoura = driver.find_element(By.XPATH, "4. rivin kurssin Xpath")#löydetään 4. rivin kurssi
coursefoura.click()#painetaan sitä

coursefivea = driver.find_element(By.XPATH, "5. rivin kurssin Xpath")#löydetään 5. rivin kurssi
coursefivea.click()#painetaan sitä

coursesixa = driver.find_element(By.XPATH, "6. rivin kurssin Xpath")#löydetään 6. rivin kurssi
coursesixa.click()#painetaan sitä

coursesevena = driver.find_element(By.XPATH, "7. rivin kurssin Xpath")#löydetään 7. rivin kurssi
coursesevena.click()#painetaan sitä

firstbuttona.click()#suljetaan 4 periodin kurssit

time.sleep(0.5) #odotetaan puoli sekuntia, jotta 4. periodin kurssit ehtivät latautua

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/ul[1]/li[5]/a")) #odotetaan 5. periodin nappia
)

firstbuttonb = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div/div[2]/ul[1]/li[5]/a")#löydetään 5. perioidin  nappi
firstbuttonb.click()#painetaan nappia

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "1. rivin kurssin Xpath")) #odotetaan 1. kurssin nappia
)

courseoneb = driver.find_element(By.XPATH, "1. rivin kurssin Xpath")#löydetään 1. rivin kurssi
courseoneb.click()#painetaan sitä

coursetwob = driver.find_element(By.XPATH, "2. rivin kurssin Xpath")#löydetään 2. rivin kurssi
coursetwob.click()#painetaan sitä

coursethreeb = driver.find_element(By.XPATH, "3. rivin kurssin Xpath")#löydetään 3. rivin kurssi
coursethreeb.click()#painetaan sitä

coursefourb = driver.find_element(By.XPATH, "4. rivin kurssin Xpath")#löydetään 4. rivin kurssi
coursefourb.click()#painetaan sitä

coursefiveb = driver.find_element(By.XPATH, "5. rivin kurssin Xpath")#löydetään 5. rivin kurssi
coursefiveb.click()#painetaan sitä

coursesixb = driver.find_element(By.XPATH, "6. rivin kurssin Xpath")#löydetään 6. rivin kurssi
coursesixb.click()#painetaan sitä

coursesevenb = driver.find_element(By.XPATH, "7. rivin kurssin Xpath")#löydetään 7. rivin kurssi
coursesevenb.click()#painetaan sitä



time.sleep(10) #sovellus odottaa hetken

driver.quit() #sovellus sulkee chromen