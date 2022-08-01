import unittest
from HTMLTestRunner import HTMLTestRunner
import TestSuites
from TestSuites.Spa import *
from TestSuites.Uñas import *
from TestSuites.Cabello import *
from TestSuites.Iniciar_sesion import *
from TestSuites.Cerrar_Sesion import *
from TestSuites.Maquillaje import *
from TestSuites.Agendar_y_pagar_una_cita import *


import os

from TestSuites.config.QaseAPI import create_test_run

lista_test_cases_spa=[10,11,12,13,14,15,16,18,78]
lista_test_cases_uñas=[17,20,32,38,55,59,63,64,79]
lista_test_cases_cabello=[26,66,40,33,57,69,19,61,81]
lista_test_cases_maquillaje=[34,39]
lista_test_cases_agendar_y_pagar=[119,120]
lista_test_cases_cerrar_sesion=[111]
lista_test_cases_iniciar_sesion=[75]


lista_test_cases=[*lista_test_cases_spa,*lista_test_cases_uñas,*lista_test_cases_cabello,*lista_test_cases_iniciar_sesion,
                  *lista_test_cases_agendar_y_pagar,*lista_test_cases_cerrar_sesion,*lista_test_cases_maquillaje]

create_test_run("Automatic Test Run","Prueba Test Suite API","GLITZI",lista_test_cases,2)

# get the directory path to output report file
dir = os.getcwd()

#
# particular = unittest.TestLoader().loadTestsFromTestCase(test_Servicios_Recomendados66.bolsa_cabello_recom)
# testsuite= unittest.TestSuite([particular])


testsuite = unittest.TestLoader().discover('.')
# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
runner.run(testsuite)