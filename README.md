# Kurssivalitsija
## Valitsee lukion kurssit wilmassa puolestasi

![Kurssivalitsija](https://github.com/user-attachments/assets/13dab8d9-b9b0-464e-b6ca-c141799436db)


## Käyttö ja asennus 

 - Aluksi lataa kurssivalitsija python (.py) tiedosto. 
 - Lataa chromedriver.exe tiedosto.
 - Pistä molemmat lataamasi tiedostot yhteen kansioon tietokoneella .
 - Tämän käyttöä varten sinulla pitää olla ladattuna python ja joku koodieditori.
     - voit käyttää mitä vain koodieditoria, mutta suosittelen [Pycharmia](https://www.jetbrains.com/pycharm/download/?section=windows).
 - Pythonin voi ladata helposti ja nopeasti [Microsoft Storesta](https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare)
 - Jotta koodi toimii, sinun on asennettava selenium.
 - Se pitää tehdä pythonin jälkeen
 - Avaa komentokehote (command prompt) kirjoittamalla cmd windowsin hakuun.
 - Kirjoita sinne ""pip install selenium""
 - Kun olet ladannut kaiken tarvittavan sinun pitää avata koodieditori ja editoida tarvittavat kohdat sieltä
    - Wilman tunnukset
    - Kurssit jotka haluat valita
- Python tiedostossa sanotaan että "Tarvittavan kurssin **Xpath**"
    - Xpathin saa helposti
    - Avaa chrome selaimessa Wilma
    - Wilmassa avaa kurssitarojotin
    - paina **CTRL + SHIFT + I**
    - Paina vasemmassa yläkulmassa olevaa nappia avautuneessa valikossa, joka löytää sinulle tarvittavan rivin HTML-koodissa
    - paina sitä riviä oikealla hiiren napilla
    - ja paina "**copy full Xpath**"
 - Kun kaikki on valmiina käynnistä koodi joko editorin tai cmd:n kautta 
 - lopuksi valitsee sinulle etukäteen syöttämäsi kurssit

[Video-ohje](https://www.youtube.com/watch?v=Tp0cM2fn9U0)


**Kannattaa tarkistaa se toimiiko koodi ennen kun kurssitarjotin avautuu, koska joskus voit vahingossa laittaa väärän kurssin koodiin tai tehdä jotain muita virheitä**




*Tämä koodi on alunperin tehty Alppilan lukion kurssitarjotinta varten, joten en ole varma tuleeko se toimimaan muissa lukioissa*


  

