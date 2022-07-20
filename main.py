import unittest
from TestSuites.Iniciar_sesion.Inicio_sesion_correcto75 import Login
from TestSuites.Spa.Serviciso_SPA11 import Servicios
from TestSuites.Cerrar_Sesion.Cerrar_sesion_correcto111 import Logout
from TestSuites.Maquillaje.Filtro_de_Maquillaje_de_dia34 import filtro_m_dia
from TestSuites.Maquillaje.Filtro_de_Maquillaje_de_noche39 import filtro_m_noche
from TestSuites.Agendar_y_pagar_una_cita.Bolsa_de_compras119 import Bolsa
from TestSuites.Spa.Boton_de_visualizacion10 import boton_visualizacion
from TestSuites.Spa.Filtro_de_Servicios_Basicos12 import filtro_basico_spa
from TestSuites.Spa.Filtro_de_Servicios_premium13 import filtro_premium_spa
from TestSuites.Spa.CTA_Ver_Detalles_del_Servicio14 import ver_detalles
from HTMLTestRunner import HTMLTestRunner
from TestSuites.Spa.Bolsa_de_Compras15 import bolsa_spa
import os

from QaseAPI import create_test_run

lista_test_cases=[10,11,12,13,14,15] #75 corresponde al test case de login y 11 a servicio SPA
create_test_run("Prueba API","Probando 1 2 3","GLITZI",lista_test_cases,1)

# get the directory path to output report file
dir = os.getcwd()

#Spa
boton_vis= unittest.TestLoader().loadTestsFromTestCase(boton_visualizacion)
service_SPA = unittest.TestLoader().loadTestsFromTestCase(Servicios)
filtro_spa = unittest.TestLoader().loadTestsFromTestCase(filtro_basico_spa)
filtro_spa2 = unittest.TestLoader().loadTestsFromTestCase(filtro_premium_spa)
cta_ver_Detalles= unittest.TestLoader().loadTestsFromTestCase(ver_detalles)
test_bolsa_spa= unittest.TestLoader().loadTestsFromTestCase(bolsa_spa)

login = unittest.TestLoader().loadTestsFromTestCase(Login)

logout = unittest.TestLoader().loadTestsFromTestCase(Logout)
filtro_maquillaje_d=unittest.TestLoader().loadTestsFromTestCase(filtro_m_dia)
filtro_maquillaje_n=unittest.TestLoader().loadTestsFromTestCase(filtro_m_noche)
bolsa_compras=unittest.TestLoader().loadTestsFromTestCase(Bolsa)


test_suite = unittest.TestSuite([boton_vis,service_SPA,filtro_spa,filtro_spa2,cta_ver_Detalles,test_bolsa_spa])
# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
runner.run(test_suite)