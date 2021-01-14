from bs4 import BeautifulSoup
import requests
import pyshorteners

l = pyshorteners.Shortener()

def linkedin():
  link = 'https://www.linkedin.com/jobs/desenvolvedor-python-vagas/?originalSubdomain=br'
  req = requests.get(link)
  soup = BeautifulSoup(req.content, 'html.parser')

  vaga = soup.find_all('div')

  print('--------------------LINKEDIN--------------------\n\n\n')
  for i in range(10):
    if i%2 == 0:
      nome = str(vaga[44+i]).split('title">')[1].split('</h3>')[0]
      link = l.tinyurl.short(str(vaga[44+i]).split('href=')[1].split('">')[0].split('?trk')[0]+'/jobs/')
      local = str(vaga[44+i]).split('location">')[1].split('</span>')[0]
      data = str(vaga[44+i]).split('datetime="')[1].split('</time>')[0].split('">')[0]
      hora = str(vaga[44+i]).split('datetime="')[1].split('</time>')[0].split('">')[1]
      
      print(f'{nome}\nlink da empresa:{link}\n{local}\n{data}  {hora}\n')

def procurar():
  linkedin()
  
  
  
  
procurar()