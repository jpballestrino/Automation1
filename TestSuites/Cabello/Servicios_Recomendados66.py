from selenium.webdriver.common.by import By
import time
import unittest
from TestSuites.config.QaseAPI import actualizar_state,get_id_of_active_run
import os
from TestSuites.config.params import dataEnv

data=dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko

class bolsa_uñas_recom(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_bolsa(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get(data.Web+"/servicios/unas")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-105"]/div/div[3]/a')
        CTA_detalle.click()
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="button-add-6"]/div[3]/button')
        CTA_agregar.click()
        CTA_bolsa = self.driver.find_element(By.XPATH, value='//*[@id="sectionsNav"]/div/div[2]/div[2]/div/div/div[2]/ul[2]/li[3]/a/i')
        CTA_bolsa.click()
        elemento_en_bolsa = self.driver.find_element(By.XPATH, value='//*[@id="ml-service-6"]/div[2]/div/div[1]/span')

        if elemento_en_bolsa.text == "Pedi Gelish":
            actualizar_state("GLITZI", status_test="passed", case_id=63, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=63, run_id=active_id)
        self.assertEqual(elemento_en_bolsa.text, "Pedi Gelish")


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
