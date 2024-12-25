from dotenv import load_dotenv, set_key
import os
from buscadore import GoogleSearch
import argparse
import sys

# Cargamos las variables en el entorno 
def env_config():
    """"Configura el archivo .env"""
    api_key = input("Intruduce tu API KEY de Google: ")
    engine_id = input("Intruduce el id del bucador personalizado de Google: ")
    set_key (".env","API_KEY_GOOGLE", api_key)
    set_key (".env","SEARCH_ENGINE_ID", engine_id)
    
def main(query, configure_env, start_page, pages, lang):
    #verificar si el archivo .env existe
      #se asegura si el esta el la ruta actual o tambien se puede espesificar una ruta
    if configure_env or not os.path.exists(".env"):
        #  Crear o configurar el fichero .env
        env_config()
        print("Archivo .env configurado satifactorioamente")
        sys.exit(1)
        
    load_dotenv()
   
    #construimos la url de consulta:
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE") 

    #Para el buscador
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")
    if not API_KEY_GOOGLE or not SEARCH_ENGINE_ID:
        print("ERROR: Falta la API_KEY o el SEARCH_ENGINE_ID. Por favor, ejecuta la opción --configure para configurar el archivo .env.")
        sys.exit(1)
    if not query:
        print("Indica una consulta con el comando -q. Utiliza el comando -h para mostrar la ayuda.")
        sys.exit(1)

    gseach = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)

    resultados = gseach.search(query, pages=pages, 
                               start_page=start_page,
                               lang=lang)

    print(resultados)

if __name__ == "__main__":
    #configurar los argumentos que sera como guia para el usuario en la utilizacion del programa
    parser = argparse.ArgumentParser(description="Herramienta para realizar búsquedas avanzadas en Google de forma automática.") #Crea el obejeto que optenda las variables de usuario 
    parser.add_argument("-q", "--query", type=str, help="Especifica el dork que deseas buscar. Ejemplo: -q \"filetype:sql 'MySQL dump' (pass|password|passwd|pwd)\"") 
    #Se le da opciones y una ayuda a los usuarios claro siempre con un ejemplo para ayudar a la compresion del usurio 
    parser.add_argument("-c", "--configure", action="store_true", help="Configura o actualiza el archivo .env. Utiliza esta opción sin otros argumentos para configurar las claves.")
    parser.add_argument("--start-page", type=int, default=1, help="Página de inicio para los resultados de búsqueda. Por defecto es 1.")
    parser.add_argument("--pages", type=int, default=1, help="Número de páginas de resultados a retornar. Por defecto es 1.")
    parser.add_argument("--lang", type=str, default="lang_es", help="Código de idioma para los resultados de búsqueda. Por defecto es 'lang_es' (español).")
    #Ahora se debe usar todos los argumentos de el programa para el uso de la libreria
    args = parser.parse_args()
    main(query=args.query, 
         configure_env=args.configure, 
         start_page=args.start_page, 
         pages=args.pages, 
         lang=args.lang)
