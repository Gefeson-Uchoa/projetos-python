from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class AutoChrome:
    def __init__(self):
        self.driver_path = './chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('user-data-dir=Perfl')
        self.Chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def EntraSite(self,site):
        self.Chrome.get(site)

    def PesquisaAcao(self,acao):
        barra_click = self.Chrome.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.KdK6Xc > div.e1AOyf > '
                                                'div > div > div > div.d1dlne > input.Ax4B8.ZAGvjd').send_keys(acao)
        barra_de_pesquisa = self.Chrome.find_element_by_css_selector('#yDmH0d > c-wiz > div > div.KdK6Xc > div.e1AOyf > '
                                        'div > div > div > div.d1dlne > input.Ax4B8.ZAGvjd').send_keys(Keys.ENTER)

    def ValorAcao(self):
        valor = self.Chrome.find_element_by_class_name('YMlKec').text
        return valor


