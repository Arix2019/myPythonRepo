#EX: Page Object no http://www.google.com.br

from selenium import webdriver
import time

class google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.google.com.br'
        self.search_bar = 'lst-ib'  # id
        self.btn_search = 'btnK'    # name
        self.btn_i_lucky = 'btnI'    # name

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word='none'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_search).click()

    def lucky(self, word='none'):
        self.driver.find_element_by_id(self.search_bar).send_keys(word)
        self.driver.find_element_by_name(self.btn_i_lucky).click()


ff = webdriver.Firefox(executable_path=r"C:\python\geckodriver\geckodriver.exe")
g = google(ff)
g.navigate()    # navega para http://www.google.com.br
time.sleep(3)
g.search('iron man')   #clica no botão e faz uma busca automatica por 'iron man'
#g.lucky('iron man')   # clica no botao 'estou com sorte'