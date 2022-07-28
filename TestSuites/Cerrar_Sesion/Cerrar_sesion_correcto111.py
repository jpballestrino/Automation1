from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from TestSuites.config.QaseAPI import actualizar_state, get_id_of_active_run
import os
from ..config.params import dataEnv

data=dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko
class Logout(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(4)
        inst.driver.maximize_window()
        # navigate to the application home page

        # enter search keyword and submit
    def test_login(self):

        self.driver.get(data.Web)
        time.sleep(4)
        WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(by=By.CLASS_NAME, value='modal-closes.publicity-button'))
        popup = self.driver.find_element(By.XPATH,value='//button[@style="background: transparent"]')
        popup.click()
        login = self.driver.find_element(by=By.XPATH,value='//a[@id="log-in-link"]')
        self.driver.execute_script("arguments[0].click();",login)
        # enter search keyword and submit
        self.search_field = self.driver.find_element(by=By.ID, value='email')
        self.search_field.send_keys(data.email)
        time.sleep(1)
        self.search_field = self.driver.find_element(by=By.ID, value='password')
        self.search_field.send_keys(data.password)
        time.sleep(1)
        self.search_field.submit()


    def test_logout(self):
        active_id = get_id_of_active_run("GLITZI")
        saltar_ver= self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[1]/div/div/div/div/div[6]/a/u')
        saltar_ver.click()
        options= self.driver.find_element(by=By.XPATH,value="/html/body/div[3]/div[2]/nav/div/div[2]/div[2]/div/div/div[2]/ul[2]/li[4]/a/i")
        options.click()
        time.sleep(1)
        cerrar = self.driver.find_element(by=By.XPATH,value="/html/body/div[3]/div[2]/nav/div/div[2]/div[2]/div/div/div[2]/ul[2]/li[4]/div/a[3]")
        cerrar.click()
        time.sleep(1)
        iniciar_sesion=self.driver.find_element(by=By.XPATH,value='//*[@id="log-in-link_"]')
        if iniciar_sesion.text == 'INICIAR SESIÓN':
            actualizar_state("GLITZI", status_test="passed", case_id=111, run_id=active_id)
        else:
            actualizar_state("GLITZI", status_test="failed", case_id=111, run_id=active_id)
        self.assertEqual(iniciar_sesion.text, 'INICIAR SESIÓN')


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
