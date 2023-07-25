import openai
import re
import base64
import requests
import pandas as pd
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
import os

# Leemos el archivo CSV que subimos al directorio(el encoding que me ha funcionado es Latin pero se puede probar con utf-8)

df = pd.read_csv('tu_archivo.csv', encoding='latin-1')
#df = pd.read_csv('tu_archivo.csv', encoding='utf-8')

# Cargar las variables de entorno desde el archivo .env
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Configurar la clave de API de OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')


# RELLENAR: Añade tu usuario de wordpress y en el password la clave que se genera en tu usuario de WP, desde la sección perfil en "Contraseñas de aplicación" pones el nombre que quieras y pegas la contraseña que te genera
login = os.getenv('WORDPRESS_LOGIN')
password = os.getenv('WORDPRESS_PASSWORD')

# Itera sobre las preguntas
questions=[]
for i, row in df.iterrows():
  questions.append(row["title"])

question =', '.join(questions)

prompt= f""" Responde con un articulo de 2500 palabras las siguientes preguntas: {question}.\
Hazlo de manera divertida, dinámica, que llame a ser leído por todo el público amante del tomate.\
El articulo debe contener una estructura HTML con subtitulos en H2.\
No inventes la información. Respalda con datos históricos, estadísticos o relevantes citando la fuente de información.\
No des conclusiones, solo datos objetivos\
"""

try:
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
    { "role": "system", "content": "Eres historiador experto en la historia del tomate en España" },
    { "role": "user", "content": prompt} ],
    max_tokens=5000,
    temperature=0,
  )
except Exception as e:
  print("Error al realizar la solicitud a la API de OpenAI:", str(e))
  exit()


# RELLENAR: Establecer la URL de la API de WordPress y los encabezados de autorización
url = 'https://tomaqueria.com/wp-json/wp/v2/posts'
headers = {
    'Authorization': 'Basic ' + base64.b64encode(f"{login}:{password}".encode()).decode()
}


# Establecer el cuerpo de la solicitud con el título y el estado del post(en este caso lo verás en "draft" pero puedes cambiarlo si lo prefieres a "publish" para su publicación automática)
data = {
    'title': "Aquí va el título que tendrá tu artículo",
    'content': response['choices'][0]['message']['content'],
    'status': 'draft'
}

# Realizar la solicitud POST
response = requests.post(url, headers=headers, json=data)

# Verificar el estado de la respuesta
if response.status_code == 201:
    print('Post creado correctamente')
else:
    print('Error al crear el post')
# Verificar el estado de la respuesta
if response.status_code == 201:
    print('Post creado correctamente')
else:
    print('Error al crear el post')
