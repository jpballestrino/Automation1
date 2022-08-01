import os
import time
import unittest

from selenium.webdriver.common.by import By

from TestSuites.config.QaseAPI import actualizar_state, get_id_of_active_run
from ..config.params import dataEnv

data=dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko

class filtro_basico_spa(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_filtro(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get(data.Web + "servicios/spa")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_basico = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/nav/div/div/ul/li[3]/a')
        CTA_basico.click()
        titulo=self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/h1')
        if titulo.text == "SERVICIOS BÁSICOS A DOMICILIO":
            actualizar_state("GLITZI", status_test="passed", case_id=12, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=12, run_id=active_id)
        self.assertEqual(titulo.text, "SERVICIOS BÁSICOS A DOMICILIO")


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
