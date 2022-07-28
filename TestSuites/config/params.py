from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class dataEnv():
    TokenGecko= "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" # os.environ['GH_TOKEN'] = "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"
    Web= "https://li41-183.members.linode.com/"
    email="mail31696@irondev.com.mx"
    password="123456"

    def navigator(self):
        nav="chrome"
        if nav=="chrome":
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
            return driver

        elif nav=="firefox":
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
            return driver
        elif nav=="edge":
            service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Edge(service=service)
            return driver




