import os
import time
import unittest

from selenium.webdriver.common.by import By

from TestSuites.config.QaseAPI import actualizar_state, get_id_of_active_run
from ..config.params import dataEnv

data = dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko


class carusel_cabello_recom(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_carousel(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get(data.Web + "servicios/cabello")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-1932"]/div/div[3]/a')
        CTA_detalle.click()
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="button-add-1600"]/div[3]/button')
        CTA_agregar.click()
        CTA_bolsa = self.driver.find_element(By.XPATH,
                                             value='//*[@id="sectionsNav"]/div/div[2]/div[2]/div/div/div[2]/ul[2]/li[3]/a')
        CTA_bolsa.click()
        elemento_en_bolsa = self.driver.find_element(By.XPATH, value='//*[@id="ml-service-5"]/div[2]/div/div[1]/span')

        if elemento_en_bolsa.text == "Pedi Spa":
            actualizar_state("GLITZI", status_test="passed", case_id=69, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=69, run_id=active_id)
        self.assertEqual(elemento_en_bolsa.text, "Pedi Spa")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
