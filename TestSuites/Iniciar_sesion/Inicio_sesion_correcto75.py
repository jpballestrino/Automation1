from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from TestSuites.config.QaseAPI import actualizar_state,get_id_of_active_run
import os
from ..config.params import dataEnv

data=dataEnv()


os.environ['GH_TOKEN'] = dataEnv.TokenGecko

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navegador()
        inst.driver.implicitly_wait(4)
        inst.driver.maximize_window()
        # navigate to the application home page

        # enter search keyword and submit
    def test_login(self):
        active_id = get_id_of_active_run("GLITZI")
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
        verificar=self.driver.find_element(By.XPATH,value='//*[@id = "preview_verification"]/div/h4')
        time.sleep(1)
        if verificar.text=="VERIFICAR TELÉFONO":
            actualizar_state("GLITZI",status_test="passed",  case_id=75, run_id=active_id)
        else:
            actualizar_state("GLITZI",status_test="failed",  case_id=75, run_id=active_id)
        self.assertEqual(verificar.text, "VERIFICAR TELÉFONO")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
