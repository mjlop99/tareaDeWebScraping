#librerias a utilizar
from bs4 import BeautifulSoup
import requests as rq

#webScraping
#la pagina a utilizar es una de wikipedia sobre la historia de resident evil 
#se unificaron dos variables ya que los endpoint dificultaban la logica de la tarea
URL="https://es.m.wikipedia.org"

BASE="w/index.php?title=Resident_Evil"
URL_BASE=f"{URL}/{BASE}"
Response=rq.get(URL_BASE)

#obteniendo html
HTML=Response.text


#parseando html
SOUP=BeautifulSoup(HTML,"html.parser")

            #uso del find

#encontrando la etiqueta 'a' que tenga el logo del juego la cual es la que tiene la clase mw-file-description y guardamos la url de su atributo href
SOUP_logo=SOUP.find("a",class_="mw-file-description")
URL_logo=f"{URL}{SOUP_logo['href']}"
print(f"esta es la url de la primera pagina:\n{URL_logo}")

#el atributo href nos envia a atra pagina de wikipedia donde nueva mente buscaremos el logo
response_logo=rq.get(URL_logo).text
SOAP_LOGO=BeautifulSoup(response_logo,"html.parser")

#obtenemos el div que contiene el logo y luego obtenes la propieda href(url) dentro de la etiqueta a dentro de div
div_contenedor=SOAP_LOGO.find("div", {'id': 'file'})
a_dentro_div=div_contenedor.find("a")
a_url=f"https:{a_dentro_div['href']}"
print(f"esta es la url donde se encuentra el logo:\n{a_url}")
#obtenemos el logo con una peticion 
logo=rq.get(a_url)
#lo guardamos para comproba
with open('logo.png','wb') as fb:
        fb.write(logo.content)
        print("se ha guardado la imagen")


        #uso de findAll
#encontrando todos los h2 los cuales son los titulos de cada parrafo 
SOUP_h2s=SOUP.find_all("h2")

print("\naqui imprimiremos todos titulos de etiqueta h2")
for h2 in SOUP_h2s:
    print(h2.get_text(strip=True).replace("[editar]",""))

print("\naqui la info de peliculas")

            #uso de tables



#se optiene el div que posee la tabla que queremos en este caso la de informacion de la peliculas relacionadas con este juego
SOAP_div_contenedor_tabla=SOUP.find("section",class_="mf-section-4")
#optenido el div ahora optenemos el table el cual en su inicio no tenia id o clase que lo deferenciara
SOAP_tabla=SOAP_div_contenedor_tabla.find("table")
#opteemos todas las filas
peliculas=SOAP_tabla.find_all(['tr'],limit=5)
pelis=[]

for pelicula in peliculas:
    #optenemos toda la informacion de los td
    informacion = pelicula.find_all('td')
    #guardamos solo aquello que tengo tamaño 4(n°,pelicula,año,director)
    if len(informacion) == 4:
        #guardamos solo el nombre de la pelicula y su año de lanzamiento
        pelis.append({informacion[1].text: informacion[2].text})
  
    #en esta parte se podria hacer un else con la logica para aquellas cosas que no son informacion de la pelicula


#imprimimos la info
for diccionario in pelis:
    unica_clave = list(diccionario.keys())[0]
    valor = diccionario[unica_clave]
    print(f"{unica_clave} | {valor}")

