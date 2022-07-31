import unittest
from HTMLTestRunner import HTMLTestRunner
import TestSuites
from TestSuites.Spa import *
from TestSuites.Uñas import *

from TestSuites.Iniciar_sesion.Inicio_sesion_correcto75 import Login
from TestSuites.Cerrar_Sesion.Cerrar_sesion_correcto111 import Logout
from TestSuites.Maquillaje.Filtro_de_Maquillaje_de_dia34 import filtro_m_dia
from TestSuites.Maquillaje.Filtro_de_Maquillaje_de_noche39 import filtro_m_noche
from TestSuites.Agendar_y_pagar_una_cita.Bolsa_de_compras119 import Bolsa
import os

from TestSuites.config.QaseAPI import create_test_run

# lista_test_cases_uñas=[17,20,32,38,55,59,63,64,79]
# lista_test_cases_spa=[10,11,12,13,14,15,16,18,78] #75 corresponde al test case de login y 11 a servicio SPA
lista_test_cases_uñas=[17,20,32,38,55,59,63,64,79]
create_test_run("Automatic Test Run","Prueba Test Suite API","GLITZI",lista_test_cases,2)

# get the directory path to output report file
dir = os.getcwd()


#Spa
boton_vis= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Boton_de_visualizacion10.boton_visualizacion)
service_SPA = unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Servicios_SPA11.Servicios)
filtro_spa = unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Filtro_de_Servicios_Basicos12.filtro_basico_spa)
filtro_spa2 = unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Filtro_de_Servicios_premium13.filtro_premium_spa)
cta_ver_Detalles= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.CTA_Ver_Detalles_del_Servicio14.ver_detalles)
bolsa_spa= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Bolsa_de_Compras15.bolsa_spa)
bolsa_spa_recom= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Servicios_Recomendados16.bolsa_spa_recom)
carousel= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Carrusel_recomendados18.carusel_spa_recom)
serv= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Spa.Agregar_Servicios_Recomendado__Servicio78.serv_recom_y_serv)

test_suite_spa = unittest.TestSuite([boton_vis,service_SPA,filtro_spa,filtro_spa2,cta_ver_Detalles,bolsa_spa,bolsa_spa_recom,carousel,serv])

# lista_test_cases=[10,11,12,13,14,15,16,18,78]

#Uñas

service_uñas = unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Servicios_UÑAS20.Servicios_uñas)
boton_vis_uñas= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Boton_de_visualizacion17.boton_visualizacion_uñas)
filtro_uñas = unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Filtro_de_Servicios_Basicos32.filtro_basico_uñas)
filtro_uñas2 = unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Filtro_de_Servicios_premium38.filtro_premium_uñas)
cta_ver_Detalles_uñas= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.CTA_Ver_Detalles_del_Servicio55.ver_detalles_uñas)
bolsa_uñas= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Bolsa_de_Compras59.bolsa_uñas)
bolsa_uñas_recom= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Servicios_Recomendados63.bolsa_uñas_recom)
carousel_uñas= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Carrusel_recomendados64.carusel_uñas_recom)
serv_uñas= unittest.TestLoader().loadTestsFromTestCase(TestSuites.Uñas.Agregar_Servicios_Recomendado__Servicio79.serv_recom_y_serv)

# test_suite_uñas = unittest.TestSuite([service_uñas,boton_vis_uñas,filtro_uñas,filtro_uñas2,cta_ver_Detalles_uñas,bolsa_uñas,bolsa_uñas_recom,carousel_uñas,serv_uñas])

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