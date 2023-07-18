# wordpress-gpt
Este proyecto tiene como objetivo utilizar la inteligencia artificial para generar contenido automáticamente y publicarlo en un sitio web de WordPress. Combina la potencia de la API de OpenAI y la flexibilidad de WordPress para ahorrar tiempo y esfuerzo en la creación de contenido.

Características principales:

Generación automática de contenido: Utiliza la API de OpenAI para generar contenido basado en preguntas y respuestas relacionadas con un tema específico.
Documento previo: Genera un documento previo en formato de texto sin formato para revisar y ajustar el contenido antes de su publicación en WordPress.
Publicación en WordPress: Utiliza la API de WordPress para crear una nueva publicación con el contenido generado. Se puede especificar si se desea publicar como borrador o publicación inmediata.
Configuración segura: Utiliza la librería python-dotenv para gestionar las credenciales y configuraciones sensibles en un archivo .env separado.

Guía de uso
Configuración del entorno:

Instala las dependencias necesarias utilizando pip install -r requirements.txt.

Crea un archivo .env con las variables de entorno necesarias, como las credenciales de WordPress.
Preparación de los datos:

Prepara un archivo CSV con las preguntas relacionadas con el tema deseado en una única columna titulada "title" y subelo al mismo directorio del proyecto

Generación de contenido:

Utiliza el script para generar automáticamente el contenido respondiendo a las preguntas contenidas en tu archivo csv utilizando la API de OpenAI.
El contenido generado se publicará de manera automática en la carpeta de borradores de tu wordpress.

Asegúrate de configurar correctamente las credenciales de WordPress en el archivo .env.

Contribuciones
¡Las contribuciones a este proyecto son bienvenidas! Si tienes ideas de mejora, problemas o sugerencias, no dudes en abrir un issue o enviar un pull request.
