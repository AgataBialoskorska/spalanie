import requests, time, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Chrome()
driver.get("https://www.e-petrol.pl/notowania")
cookie = driver.find_element(by=By.ID, value="cookieChoiceDismiss").click()
table = driver.find_element(by=By.XPATH, value='//*[@id="sekcja-dwa"]/div[1]/div/div/div[1]/div[2]/div/div')
driver.execute_script('arguments[0].scrollIntoView({block: "center", inline: "center"})', table)
time.sleep(1)
today = (datetime.date.today())
date = today.strftime('%Y_%b_%d')
driver.save_screenshot("ceny_paliw_"+date+".png")
time.sleep(0.5)
driver.quit()

print("\nCześć!\n Jesli chcesz sprawdzić ile paliwa spalił Twoj samochód na ostaniej trasie, uzupełnij ponizsze wartości.\n Pamiętaj, aby Twoj samochod był zatankowany do pełna przed pomiarem.\n")
while True:
  try:
     przed = float(input("Podaj przebieg PRZED trasą: "))       
  except ValueError:
     print("Wpisz poprawną liczbę!")
     continue
  else:
     print("Dziękuję\n")
     break 

while True:
   try:
      po = float(input("Podaj przebieg PO trasie: "))
      if po>przed:
         next 
      else:
         print("Wartość PO nie moze być mniejsza niz PRZED!\nWpisz poprawną wartość.\n")
         continue
   except ValueError:
      print("Wpisz poprawną liczbę!\n")
      continue
   else:
      print("Dziękuję\n")
      break 

while True:
    try:
     tankowanie = float(input("Podaj ile litrów zatankowałeś(-aś): "))       
    except ValueError:
     print("Wpisz poprawną liczbę!\n")
     continue
    else:
     print("OK\n")
     break 

spalanie = (tankowanie * 100//(po - przed)) 
print ("Twój samochód spalił ",round(spalanie,2),"litrów paliwa na tej trasie.")
if spalanie<=6:
   print("Świetny wynik!!!")
elif 6 < spalanie <= 12:
   print("Spalanie całkiem dobre...")
else:
   print("Łoo Panie!!! Kup Passata TDI :)")

print("\nTeraz sprawdź plik .png z cenami paliw.\nDowiesz się ile Cię kosztawała ta wycieczka.\n")