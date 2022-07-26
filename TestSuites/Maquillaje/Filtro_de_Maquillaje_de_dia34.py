from selenium.webdriver.common.by import By
import unittest
from WebDriver import driverBuilder
from QaseAPI import actualizar_state,get_id_of_active_run

class filtro_m_dia(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = driverBuilder.chrome()
        inst.driver.implicitly_wait(3)
        inst.driver.maximize_window()
        # navigate to the application home page

    def test_filtro_dia(self):
        active_id = get_id_of_active_run("GLITZI")
        self.driver.get("mail31696@irondev.com.mx/servicios/maquillaje")
        pop_up = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        pop_up.click()
        cta_maq_dia = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div/div/nav/div/div/ul/li[2]/a')
        cta_maq_dia.click()
        titulo = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/h1')
        if titulo.text=="MAQUILLAJE DE DÍA A DOMICILIO":
            actualizar_state("GLITZI",status_test="passed",  case_id=34, run_id=active_id)
        else:
            actualizar_state("GLITZI",status_test="failed",  case_id=34, run_id=active_id)
        self.assertEqual(titulo.text, "MAQUILLAJE DE DÍA A DOMICILIO")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()