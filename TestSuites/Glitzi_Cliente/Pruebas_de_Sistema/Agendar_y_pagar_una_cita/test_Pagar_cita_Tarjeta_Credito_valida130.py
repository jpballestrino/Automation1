from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from TestSuites.config.QaseAPI import actualizar_state,get_id_of_active_run
import os
from TestSuites.config.params import dataEnv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
data=dataEnv()

os.environ['GH_TOKEN'] = data.TokenGecko

class Pagar_cita_tarjeta(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # create a new Chrome session
        inst.driver = data.navigator()
        inst.driver.implicitly_wait(15)
        inst.driver.maximize_window()
        # navigate to the application home page

        # enter search keyword and submit
    def test_login_mas_serv_mas_prog(self):
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
        time.sleep(1)
        self.driver.get(data.Web + "servicios/spa")
        time.sleep(1)
        popup = self.driver.find_element(By.XPATH, value='//*[@id="modalCoaches"]/div/div/div[1]/button/span')
        popup.click()
        CTA_detalle = self.driver.find_element(By.XPATH, value='//*[@id="service-79"]/div/div[3]/a')
        CTA_detalle.click()
        CTA_agregar = self.driver.find_element(By.XPATH, value='//*[@id="add-service"]')
        CTA_agregar.click()
        time.sleep(1)
        CTA_seguir = self.driver.find_element(By.XPATH, value='//*[@id="go-to-bag"]')
        CTA_seguir.click()
        time.sleep(2)
        CTA_programar_cita = self.driver.find_element(By.XPATH, value='//*[@id="create-appointment"]')
        CTA_programar_cita.click()

        CTA_direccion = self.driver.find_element(By.XPATH, value='//*[@id="address-user"]/div/div[2]/div/label/span')
        CTA_direccion.click()

        CTA_seguir = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="next"]')
        CTA_seguir.click()

        CTA_siguiente_mes = self.driver.find_element(By.XPATH, value='//*[@id="tab2"]/div/div/div[1]/div/div/div[1]/a[2]/span')
        CTA_siguiente_mes.click()

        CTA_dia_1 = self.driver.find_element(By.XPATH,
                                                         value='//*[@id="tab2"]/div/div/div[1]/div/div/div[3]/div[1]/div[6]/a')
        CTA_dia_1.click()

        time.sleep(10)

        CTA_8am = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="time-4"]/div/button')
        CTA_8am.click()
        CTA_seguir = self.driver.find_element(By.XPATH,
                                               value='//*[@id="next"]')
        CTA_seguir.click()

        time.sleep(4)
        CTA_seguir = self.driver.find_element(By.XPATH,
                                              value='//*[@id="next"]')
        CTA_seguir.click()
        CTA_seguir.click()

    # def pago_tarjeta(self):
        CTA_nueva_tarj = self.driver.find_element(By.XPATH,
                                              value='//*[@id="addCardBtn"]')
        CTA_nueva_tarj.click()
        self.search_field = self.driver.find_element(by=By.ID, value='cc-name')
        self.search_field.send_keys("jefezote")

        self.search_field = self.driver.find_element(by=By.ID, value='cc-number')
        self.search_field.send_keys(data.nro_tarjeta_credito)

        field_mes = self.driver.find_element(By.XPATH,
                                              value='//*[@id="cc-exp-month"]')
        field_mes.click()
        action = ActionChains(self.driver)

        # perform the operation
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()

        field_año = self.driver.find_element(By.XPATH,
                                           value='//*[@id="cc-exp-year"]')
        field_año.click()
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        action.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()

        self.search_field = self.driver.find_element(by=By.ID, value='cc-csc')
        self.search_field.send_keys("123")
        time.sleep(2)
        CTA_PAGAR= self.driver.find_element(By.XPATH,
                                              value='//*[@id="next"]')
        CTA_PAGAR.click()

        time.sleep(10)
        verificar=self.driver.find_element(By.XPATH,
                                              value='//*[@id="send_questionnaire_customer"]/div/p[1]/b')
        if verificar.text=="¿Quieres personalizar tu cita?":
            actualizar_state("GLITZI",status_test="passed",  case_id=130, run_id=active_id)
        else:
            actualizar_state("GLITZI",status_test="failed",  case_id=130, run_id=active_id)
        self.assertEqual(verificar.text, "¿Quieres personalizar tu cita?")

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
