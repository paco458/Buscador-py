import requests

class GoogleSearch:
    def __init__(self, api_key, engine_id):
        self.api_key = api_key
        self.engine_id = engine_id

    def search(self, query, start_page=1, pages=1, lang="lang_es" ):
        final_resultado = []
        results_per_page = 10
        for page in range(pages):
            #calculamos el resultado por cada pagina
            start_index = (start_page - 1) * results_per_page + 1 + (page * results_per_page)
    
            url = f"https://www.googleapis.com/customsearch/v1?key={self.api_key}&cx={self.engine_id }&q={query}&start={start_index}&lr={lang}"

            response = requests.get(url)
            # Comprobamos si la respuesta es correcta

            if response.status_code == 200:
                data = response.json()
                results = data.get("items")
                cresults = self.custom_results(results)
                final_resultado.extend(cresults)
            else:
                print(f"error obtenido al ver la pagina {page}: HTTP {response.status_code}")
                break
        return final_resultado
    
    def custom_results (self, results):
        
        custom_results = []

        for r in results:
            cresult = {}
            cresult ["title"]= r.get("title")
            cresult ["description"]= r.get("sniper")
            cresult ["link"]= r.get("link")
            custom_results.append(cresult)
        return custom_results