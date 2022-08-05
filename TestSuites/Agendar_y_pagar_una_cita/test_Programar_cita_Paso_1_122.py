from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from TestSuites.config.QaseAPI import actualizar_state,get_id_of_active_run
import os
from ..config.params import dataEnv

data=dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko

class Programar_cita_1(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(4)
        inst.driver.maximize_window()
        # navigate to the application home page

        # enter search keyword and submit
    def test_login_mas_serv(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get(data.Web)
        time.sleep(4)
        WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(by=By.CLASS_NAME, value='modal-closes.publicity-button'))
        popup = self.driver.find_element(By.XPATH,value='//button[@style="background: transparent"]')
        popup.click()
        login = self.driver.find_element(by=By.XPATH,value='//a[@id="log-in-link"]')
        self.driver.execute_script("arguments[0].click();",login)
        # enter search keyword and submit
        self.search_field = self.driver.find_element(by=By.ID, value='email')
        self.search_field.send_keys(data.email)
        time.sleep(1)
        self.search_field = self.driver.find_element(by=By.ID, value='password')
        self.search_field.send_keys(data.password)
        time.sleep(1)
        self.search_field.submit()
        time.sleep(1)
        self.driver.get(data.Web + "servicios/spa")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-79"]/div/div[3]/a')
        CTA_detalle.click()
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="add-service"]')
        CTA_agregar.click()
        time.sleep(1)
        CTA_seguir = self.driver.find_element(By.XPATH, value='//*[@id="go-to-bag"]')
        CTA_seguir.click()

    def test_programar_cita_paso1(self):
        CTA_programar_cita = self.driver.find_element(By.XPATH, value='//*[@id="create-appointment"]')
        CTA_programar_cita.click()

        CTA_direccion = self.driver.find_element(By.XPATH, value='//*[@id="address-user"]/div/div[2]/div/label/span')
        CTA_direccion.click()

        CTA_seguir = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="next"]')
        CTA_seguir.click()

    def test_programar_cita_paso2(self):
        CTA_siguiente_mes = self.driver.find_element(By.XPATH, value='//*[@id="tab2"]/div/div/div[1]/div/div/div[1]/a[2]/span')
        CTA_siguiente_mes.click()

        CTA_dia_1 = self.driver.find_element(By.XPATH,
                                                         value='//*[@id="tab2"]/div/div/div[1]/div/div/div[3]/div[1]/div[5]/a')
        CTA_dia_1.click()

        time.sleep(10)

        CTA_8am = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="time-4"]/div/button')
        CTA_8am.click()
        CTA_seguir = self.driver.find_element(By.XPATH,
                                               value='//*[@id="next"]')
        CTA_seguir.click()

    def test_programar_cita_paso3(self):
        time.sleep(4)
        CTA_seguir = self.driver.find_element(By.XPATH,
                                              value='//*[@id="next"]')
        CTA_seguir.click()
        CTA_seguir.click()

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
