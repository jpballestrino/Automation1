from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from WebDriver import driverBuilder
from QaseAPI import actualizar_state,get_id_of_active_run

class Servicios(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_Servicios(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("https://li41-183.members.linode.com/")
        time.sleep(4)
        WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(by=By.CLASS_NAME, value='modal-closes.publicity-button'))
        popup = self.driver.find_element(By.XPATH,value='//button[@style="background: transparent"]')
        popup.click()
        self.cta_ver_servicios = self.driver.find_element(by=By.CLASS_NAME, value='btn.btn-warning.text-white.text-uppercase.btn-block')
        self.cta_ver_servicios.click()
        titulo = self.driver.find_element(by=By.CLASS_NAME,value='title')
        if titulo.text == "SPA Y BELLEZA CERCA DE TI EN CUALQUIER MOMENTO":
            pass
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=11, run_id=active_id)
        self.assertEqual(titulo.text, "SPA Y BELLEZA CERCA DE TI EN CUALQUIER MOMENTO")

    def test_Servicios_SPA(self):
        active_id = get_id_of_active_run("GLITZI")
        cta_spa = self.driver.find_element(By.XPATH, value='//a[@data-id="SPA"]')
        cta_spa.click()
        url = self.driver.current_url
        if url == "https://li41-183.members.linode.com/servicios/spa":
            actualizar_state("GLITZI", status_test="passed", case_id=11, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=11, run_id=active_id)
        self.assertEqual(url, "https://li41-183.members.linode.com/servicios/spa")
        time.sleep(1)


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()