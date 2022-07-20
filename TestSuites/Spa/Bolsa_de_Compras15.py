from selenium.webdriver.common.by import By
import time
import unittest
from WebDriver import driverBuilder
from QaseAPI import actualizar_state,get_id_of_active_run

class bolsa_spa(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_bolsa(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("https://glitzi.com.mx/servicios/spa")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-79"]/div/div[3]/a')
        CTA_detalle.click()
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="add-service"]')
        CTA_agregar.click()
        CTA_seguir = self.driver.find_element(By.XPATH, value='//*[@id="go-to-bag"]')
        CTA_seguir.click()
        elemento_en_bolsa = self.driver.find_element(By.XPATH, value='//*[@id="ml-service-79"]/div[2]/div/div[1]/span')

        if elemento_en_bolsa.text == "Masaje Relajante":
            actualizar_state("GLITZI", status_test="passed", case_id=15, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=15, run_id=active_id)
        self.assertEqual(elemento_en_bolsa.text, "Masaje Relajante")


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
