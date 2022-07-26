import unittest
from TestSuites.Iniciar_sesion.Inicio_sesion_correcto75 import Login
from TestSuites.Spa.Servicios_SPA11 import Servicios
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
from TestSuites.Spa.Servicios_Recomendados16 import bolsa_spa_recom
from TestSuites.Spa.Carrusel_recomendados18 import carusel_spa_recom
from TestSuites.Spa.Agregar_Servicios_Recomendado__Servicio78 import serv_recom_y_serv

from TestSuites.Uñas.Servicios_UÑAS20 import Servicios_uñas
from TestSuites.Uñas.Boton_de_visualizacion17 import boton_visualizacion_uñas
import os

from QaseAPI import create_test_run

lista_test_cases=[10,11,12,13,14,15,16,18,78] #75 corresponde al test case de login y 11 a servicio SPA
create_test_run("Prueba API","Probando 1 2 3","GLITZI",lista_test_cases,2)

# get the directory path to output report file
dir = os.getcwd()

#Spa
boton_vis= unittest.TestLoader().loadTestsFromTestCase(boton_visualizacion)
service_SPA = unittest.TestLoader().loadTestsFromTestCase(Servicios)
filtro_spa = unittest.TestLoader().loadTestsFromTestCase(filtro_basico_spa)
filtro_spa2 = unittest.TestLoader().loadTestsFromTestCase(filtro_premium_spa)
cta_ver_Detalles= unittest.TestLoader().loadTestsFromTestCase(ver_detalles)
bolsa_spa= unittest.TestLoader().loadTestsFromTestCase(bolsa_spa)
bolsa_spa_recom= unittest.TestLoader().loadTestsFromTestCase(bolsa_spa_recom)
carousel= unittest.TestLoader().loadTestsFromTestCase(carusel_spa_recom)
serv= unittest.TestLoader().loadTestsFromTestCase(serv_recom_y_serv)

# test_suite_spa = unittest.TestSuite([boton_vis,service_SPA,filtro_spa,filtro_spa2,cta_ver_Detalles,bolsa_spa,bolsa_spa_recom,carousel,serv])
# lista_test_cases=[10,11,12,13,14,15,16,18,78]

#Uñas

service_uñas = unittest.TestLoader().loadTestsFromTestCase(Servicios_uñas)
boton_vis_uñas= unittest.TestLoader().loadTestsFromTestCase(boton_visualizacion_uñas)

test_suite_uñas = unittest.TestSuite([boton_vis_uñas,service_uñas])
lista_test_cases=[17,20,32,38,55,59,63,64,79]

login = unittest.TestLoader().loadTestsFromTestCase(Login)
logout = unittest.TestLoader().loadTestsFromTestCase(Logout)
filtro_maquillaje_d=unittest.TestLoader().loadTestsFromTestCase(filtro_m_dia)
filtro_maquillaje_n=unittest.TestLoader().loadTestsFromTestCase(filtro_m_noche)
bolsa_compras=unittest.TestLoader().loadTestsFromTestCase(Bolsa)

# test_suite = unittest.TestSuite([serv])
# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
runner.run(test_suite_uñas)