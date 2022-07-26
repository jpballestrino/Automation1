from selenium.webdriver.common.by import By
import time
import unittest
from WebDriver import driverBuilder
from QaseAPI import actualizar_state,get_id_of_active_run

class carusel_spa_recom(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_carousel(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("https://li41-183.members.linode.com/servicios/spa")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-1243"]/div/div[3]/a')
        CTA_detalle.click()
        self.driver.execute_script("window.scrollTo(0, 1200)")
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="button-add-5"]/div[3]/button')
        CTA_agregar.click()
        CTA_bolsa = self.driver.find_element(By.XPATH,
                                             value='//*[@id="sectionsNav"]/div/div[2]/div[2]/div/div/div[2]/ul[2]/li[3]/a')
        CTA_bolsa.click()
        elemento_en_bolsa = self.driver.find_element(By.XPATH, value='//*[@id="ml-service-5"]/div[2]/div/div[1]/span')

        if elemento_en_bolsa.text == "Pedi Spa":
            actualizar_state("GLITZI", status_test="passed", case_id=18, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=18, run_id=active_id)
        self.assertEqual(elemento_en_bolsa.text, "Pedi Spa")


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
