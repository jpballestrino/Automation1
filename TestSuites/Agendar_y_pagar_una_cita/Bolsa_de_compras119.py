from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from QaseAPI import actualizar_state,get_id_of_active_run
from WebDriver import driverBuilder
import os

os.environ['GH_TOKEN'] = "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"

class Bolsa(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.firefox()
        inst.driver.implicitly_wait(4)
        inst.driver.maximize_window()
        # navigate to the application home page

        # enter search keyword and submit
    def test_bolsa(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("https://glitzi.com.mx/")
        time.sleep(4)
        WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(by=By.CLASS_NAME, value='modal-closes.publicity-button'))
        popup = self.driver.find_element(By.XPATH,value='//button[@style="background: transparent"]')
        popup.click()
        time.sleep(1)
        servicios = self.driver.find_element(by=By.XPATH,value='//*[@id="sectionsNav"]/div/div[2]/div[2]/div/div/div[2]/ul[1]/li[1]/a[2]')
        servicios.click()        # enter search keyword and submit
        cabello = self.driver.find_element(by=By.XPATH,value='/html/body/div[3]/div/div[2]/div/div/div/div/div[3]/a/div/div[2]')
        cabello.click()  # enter search keyword and submit
        time.sleep(1)
        pop_up = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        pop_up.click()
        time.sleep(1)
        corte_mujer = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="service-1985"]/div/div[3]/a')
        corte_mujer.click()  # enter search keyword and submit
        time.sleep(1)
        agregar = self.driver.find_element(by=By.XPATH,
                                               value='//*[@id="add-service"]')
        agregar.click()  # enter search keyword and submit
        time.sleep(1)
        seguir = self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="go-to-bag"]')
        seguir.click()  # enter search keyword and submit
        time.sleep(1)
        bolsa= self.driver.find_element(by=By.XPATH,
                                           value='//*[@id="ml-service-1985"]/div[2]/div/div[1]/span')
        if bolsa.text=="Corte Mujer Mi Propio Estilo":
            actualizar_state("GLITZI",status_test="passed",  case_id=119, run_id=active_id)
        else:
            actualizar_state("GLITZI",status_test="failed",  case_id=119, run_id=active_id)
        self.assertEqual(bolsa.text, "Corte Mujer Mi Propio Estilo")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
