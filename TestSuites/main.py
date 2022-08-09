import unittest
from HTMLTestRunner import HTMLTestRunner
from TestSuites.Glitzi_Cliente.Servicios.Spa import *
from TestSuites.Glitzi_Cliente.Servicios.Unias import *
from TestSuites.Glitzi_Cliente.Servicios.Maquillaje import *
from TestSuites.Glitzi_Cliente.Servicios.Peinado import *
from TestSuites.Glitzi_Cliente.Servicios.Workshops import *
from TestSuites.Glitzi_Cliente.Servicios.Paquetes_de_Spa_y_Belleza import *
from TestSuites.Glitzi_Cliente.Pruebas_de_Sistema.Agendar_y_pagar_una_cita import *

import os

from TestSuites.config.QaseAPI import *

# Servicios
lista_test_cases_spa=[10,11,12,13,14,15,16,18,78]
lista_test_cases_unias=[17,20,32,38,55,59,63,64,79]
lista_test_cases_cabello=[26,66,40,33,57,69,19,61,81]
lista_test_cases_maquillaje=[34,39,27,65,56,68,21,60,80]
lista_test_cases_peinado=[82,62,22,70,58,35,50,41,28,67]
lista_test_cases_workshops=[84,52,24,54,51,37,43,53,30]
lista_test_cases_paquetes_de_spa_y_belleza=[83,47,23,49,46,45,36,44,42,29,48]


#Pruebas de sistema
lista_test_cases_agendar_y_pagar=[119,120,132,126,130,131,122]
lista_test_cases_cerrar_sesion=[111]
lista_test_cases_iniciar_sesion=[75]



lista_test_cases=[*lista_test_cases_spa,*lista_test_cases_unias,*lista_test_cases_cabello,*lista_test_cases_iniciar_sesion,
                  *lista_test_cases_agendar_y_pagar,*lista_test_cases_cerrar_sesion,*lista_test_cases_maquillaje,*lista_test_cases_peinado,*lista_test_cases_workshops,
                  *lista_test_cases_paquetes_de_spa_y_belleza]

try:
    active_id = get_id_of_active_run("GLITZI")
    delete_test_run("GLITZI", active_id)
    try:
        active_id = get_id_of_active_run("GLITZI")
        delete_test_run("GLITZI", active_id)
    except:
        pass
except:
    pass

create_test_run("Automatic Test Run","Prueba Test Suite API","GLITZI",lista_test_cases,2)
active_id=get_id_of_active_run("GLITZI")

# get the directory path to output report file
dir = os.getcwd()

# #
# particular = unittest.TestLoader().loadTestsFromTestCase(test_CTA_Ver_Detalles_del_servicio51.ver_detalles_workshops)
# particular2= unittest.TestLoader().loadTestsFromTestCase(test_CTA_Ver_Detalles_del_Servicio56.ver_detalles_maquillaje)
# testsuite= unittest.TestSuite([particular,particular2])


testsuite = unittest.TestLoader().discover('.')
# open the report file
outfile = open(dir + "\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                            open_in_browser=True, description="HTMLTestReport")
runner.run(testsuite)

complete_run("GLITZI",active_id)
# delete_test_run("GLITZI", active_id)