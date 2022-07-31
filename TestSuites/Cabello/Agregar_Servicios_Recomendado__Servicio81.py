from selenium.webdriver.common.by import By
import time
import unittest
from TestSuites.config.QaseAPI import actualizar_state,get_id_of_active_run
import os
from ..config.params import dataEnv

data=dataEnv()


os.environ['GH_TOKEN'] = dataEnv.TokenGecko

class serv_recom_y_serv(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_bolsa(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get(data.Web +"servicios/unas")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-1421"]/div/div[3]/a')
        CTA_detalle.click()
        self.driver.execute_script("window.scrollTo(0, 1200)")

        next = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div/div[2]/div[2]/div/div[2]/button[2]/i')
        next.click()
        time.sleep(0.5)
        next.click()
        time.sleep(0.5)
        next.click()
        time.sleep(0.5)
        next.click()
        time.sleep(0.5)
        next.click()
        time.sleep(0.5)
        next.click()
        time.sleep(0.5)
        next.click()
        time.sleep(0.5)
        next.click()
        CTA_agregar_recom = self.driver.find_element(By.XPATH, value='//*[@id="button-add-83"]/div[3]/button')
        CTA_agregar_recom.click()
        self.driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="add-service"]')
        CTA_agregar.click()
        time.sleep(1)
        CTA_seguir = self.driver.find_element(By.XPATH, value='//*[@id="go-to-bag"]')
        CTA_seguir.click()
        elemento_en_bolsa_1 = self.driver.find_element(By.XPATH, value='//*[@id="ml-service-1421"]/div[2]/div/div[1]/span')
        elemento_en_bolsa_2 = self.driver.find_element(By.XPATH,
                                                       value='//*[@id="ml-service-83"]/div[2]/div/div[1]/span')
        if elemento_en_bolsa_1.text == "Pedi para deportistas" and elemento_en_bolsa_2.text == 'Reflexología Podal':
            a=1
            actualizar_state("GLITZI", status_test="passed", case_id=79, run_id=active_id)
        else:
            a=0
            actualizar_state("GLITZI", status_test="failed", case_id=79, run_id=active_id)
        self.assertEqual(a, 1)


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
