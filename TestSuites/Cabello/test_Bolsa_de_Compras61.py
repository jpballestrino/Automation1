import os
import time
import unittest

from selenium.webdriver.common.by import By

from TestSuites.config.QaseAPI import actualizar_state, get_id_of_active_run
from ..config.params import dataEnv

data = dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko


class bolsa_cabello(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_bolsa(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get(data.Web + "/servicios/cabello")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-1942"]/div/div[3]/a')
        CTA_detalle.click()
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="add-service"]')
        CTA_agregar.click()
        elemento_en_bolsa = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="ml-service-1942"]/div[2]/div/div[1]/span')
        if elemento_en_bolsa.text == "Corte buzz hombre":
            actualizar_state("GLITZI", status_test="passed", case_id=61, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=61, run_id=active_id)
        self.assertEqual(elemento_en_bolsa.text, "Corte buzz hombre")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
