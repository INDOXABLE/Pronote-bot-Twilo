import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class crawlerbot():
    crawler = webdriver.PhantomJS()

    crawler.get("https://www.agora06.fr/")


    identifiant = crawler.find_element_by_class_name("credentials_input_text")
    motdepasse = crawler.find_element_by_class_name("credentials_input_password")

    
    identifiant.send_keys("mehdi.benahmed1")
    motdepasse.send_keys("kx49ba55&*")

    connexion = crawler.find_element_by_class_name("credentials_input_submit")
    connexion.click()



