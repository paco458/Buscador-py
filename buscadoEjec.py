from dotenv import load_dotenv
import os
from buscadore import GoogleSearch
import argparse

# Cargamos las variables en el entorno 
load_dotenv()

def main():
    
    query = "J" 
    #construimos la url de consulta:
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE") 

    #Para el buscador
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

    gseach = GoogleSearch(API_KEY_GOOGLE, SEARCH_ENGINE_ID)

    resultados = gseach.search(query, pages=1, start_page=3)

    print(resultados)

if __name__ == "__main__":
    #configurar los armentos
    
    main()
