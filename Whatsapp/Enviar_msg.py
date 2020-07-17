# Abra o cmd e de o comando pip install selenium
# Fazer download do "Google Chrome Driver", navegador para automação
# Ver versão do google que está sendo usada em seu computador
# Acessar e baixar de acordo com sua versão Chrome https://chromedriver.chromium.org/downloads
# Crie uma pasta na sua área de trabalho ou outro local de sua preferência com o nome "bot whatsapp"
# Vá até a pasta download e extraía os arquivos para a pasta que você criou acima
# Abra está pasta no Visual Code

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = "Bom dia pessoal, esse é um teste de bot!!! Veja o video que acabou de sair https://www.youtube.com/watch?v=IxBNkVPNEI4"
        self.grupos_ou_pessoas = ["nomes"] 
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe')
    
    def EnviarMensagens(self):
        # <span dir="auto" title="Meu" class="_3ko75 _5h6Y_ _3Whw5">Meu</span>
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        self.driver.get('https://web.whatsapp.com')
        time.sleep(20)
        for grupo in self.grupos_ou_pessoas:
            grupo = self.driver.find_element_by_xpath(
                f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

bot = WhatsappBot()
bot.EnviarMensagens()