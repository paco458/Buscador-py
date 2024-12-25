import json

class ResultsParse:
    def __init__(self, resultados):
        self.resultados = resultados
    
    def exportar_html(self, archivo_salida):
        #leer plantilla "r"
        with open("html_template.html", 'r', enconding='utf-8') as f:
            plantilla= f.read()
        #recorer los resulados
        elemtos_html = ' '
        for indice, resultados in enumerate(self.resultados, start=1):
            #generamos bloques para guardar los resultados 
            elmento = f'*<div class ="resultados">' \ 
                            f'<div class'