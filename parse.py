# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup #biblioteca necessaria para fazer o "parse"
from urllib2 import urlopen
import re
import numpy as np
import urllib
import cv2


def url_to_image(url):
   #baixa a imagem, converte-a em uma matriz NumPy e faz a leitura da imagem no formato OpenCV
   resp = urllib.urlopen(url)
   image = np.asarray(bytearray(resp.read()), dtype="uint8")
   image = cv2.imdecode(image, cv2.IMREAD_COLOR)
   return image


#obtendo os dados da página web:
html_page = urlopen("https://g1.globo.com/globonews/")
soup = BeautifulSoup(html_page)

#extraindo todos os links de imagem:
images = []

'''
O método findAll percorre a árvore, iniciando no ponto especificado: 'img', localizando todas as Tags e Strings de Navegação que correspondem aos critérios fornecidos
O valor de uma String de Navegação pode ser: uma string, uma expressão regular, uma lista ou dicionário
'''
for img in soup.findAll('img'): 
    images.append(img.get('src')) #adiciona no vetor images, as urls das imagens encontradas

'''for i in range(len(images)):
#imprime os links das imagens
   print(images[i])'''

#para cada url no vetor:
for url in images:
   #faz o download da imagem e a exibe na tela
   print ("downloading %s" % (url))
   image = url_to_image(url) #passa a url para esse método
   cv2.imshow("Image", image)
   cv2.waitKey(0)


