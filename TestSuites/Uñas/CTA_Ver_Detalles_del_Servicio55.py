from selenium.webdriver.common.by import By
import time
import unittest
from WebDriver import driverBuilder
from QaseAPI import actualizar_state,get_id_of_active_run

class ver_detalles(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_detalles(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("https://li41-183.members.linode.com/servicios/unas")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-79"]/div/div[3]/a')
        CTA_detalle.click()
        description=self.driver.find_element(By.XPATH, value='//*[@id="service-selected"]/div[1]/div[1]/div[2]/div[1]/div/div/b')
        if description.text == "DESCRIPCIÓN":
            actualizar_state("GLITZI", status_test="passed", case_id=55, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=55, run_id=active_id)
        self.assertEqual(description.text, "DESCRIPCIÓN")


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
