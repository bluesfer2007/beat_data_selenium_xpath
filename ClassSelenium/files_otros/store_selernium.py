import selenium
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL='http://demo-store.seleniumacademy.com'

class Store_Sele(webdriver.Chrome):
    def __init__(self, self_path='D:\driver_sel\webdriver', teardown=False):
        self.self_path=self_path
        self.teardown=teardown

        super(Store_Sele, self).__init__()
        self.maximize_window()
    
    def __exit__(self, exce_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    #escriber metodos
    def get_url(self):
        self.get(URL)

    #rellenar formulario
    def rellenar_form(self):
        cuenta=self.find_element(By.XPATH,'//span[contains(text(), "Account")]')
        cuenta.click()
        register=self.find_element(By.XPATH, '//li/a[@title="Register"]')
        register.click()
        #rellenar formulario
        first_name=self.find_element(By.XPATH,'//input[@id="firstname"]')
        first_name.send_keys('fernando')

        midle_name=self.find_element(By.XPATH,'//input[@id="middlename"]')
        midle_name.send_keys('pullutasig')

        last_name=self.find_element(By.XPATH,'//input[@id="lastname"]')
        last_name.send_keys('pullutasig')

        email=self.find_element(By.XPATH,'//input[@id="email_address"]')
        email.send_keys('ejemplo@correo.com.ec')

        password=self.find_element(By.XPATH,'//input[@id="password"]')
        password.send_keys('abc123')

        password_confir=self.find_element(By.XPATH,'//input[@id="confirmation"]')
        password_confir.send_keys('abc123')

        check_input=self.find_element(By.XPATH, '//input[@type="checkbox"]')
        check_input.click()

        registro=self.find_element(By.XPATH,'//button[@title="Register"]')
        registro.click()
