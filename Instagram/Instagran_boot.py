# Baixar Geckoriver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox (executable_path= r'C:\codepython\Redes Sociais\geckodriver.exe')

# <a href="/accounts/emailsignup/" tabindex="0"><span class="_7UhW9   xLCgt       qyrsm      gtFbE     se6yk        "
# <a//[@href="/accounts/login/?source=auth_switcher"
# <input aria-label="Telefone, nome de usuário ou email" aria-required="true" autocapitalize="off" autocorrect="off" maxlength="75" name="username" type="text" class="_2hvTZ pexuQ zyHYP" value="">
# <input aria-label="Senha" aria-required="true" autocapitalize="off" autocorrect="off" name="password" type="password" class="_2hvTZ pexuQ zyHYP" value="">
#     
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(5)
        acessar = driver.find_element_by_xpath("//a[@href='/accounts/emailsignup/']")
        acessar.click()
        time.sleep(2)
        conecte_se = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        conecte_se.click()
        usuario = driver.find_element_by_xpath("//input[@name='username']")
        usuario.clear()
        usuario.send_keys(self.username)
        senha = driver.find_element_by_xpath("//input[@name='password']")
        senha.clear()
        senha.send_keys(self.password)
        senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.curtir_fotos('memesBR')

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('endereço' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(O, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in hrefs]
        print(hashtag + 'fotos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(O, document.body.scrollHeight);")
            try:                
                driver.find_element_by_class_name('//button[@class="dCJp8 afkep _Omzm-"]').click()
                time.sleep(19)
            except Exception as e:
                time.sleep(5)






edsonBot = InstagramBot('IssoVaiDominarOMundo','aindaBemQueEuSeiCriarUm')
edsonBot.login()

