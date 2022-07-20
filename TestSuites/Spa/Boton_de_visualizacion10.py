from selenium.webdriver.common.by import By
import time
import unittest
from WebDriver import driverBuilder
from QaseAPI import actualizar_state,get_id_of_active_run

class boton_visualizacion(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_boton(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("https://glitzi.com.mx/servicios/spa")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_grid = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/div[1]/button[2]')
        CTA_grid.click()
        if CTA_grid.get_attribute("class") == "btn btn-lg btn-just-icon ml-2 btn-info":
            actualizar_state("GLITZI", status_test="passed", case_id=10, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=10, run_id=active_id)
        self.assertEqual(CTA_grid.get_attribute("class"), "btn btn-lg btn-just-icon ml-2 btn-info")



    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()