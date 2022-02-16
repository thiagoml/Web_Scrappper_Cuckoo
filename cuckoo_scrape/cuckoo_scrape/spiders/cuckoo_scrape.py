import scrapy
import json
from scrapy import Request
import requests




class CuckooSpider(scrapy.Spider):
    name = 'cuckoo'
    limite_request = 100
    url = "https://cuckoo.cert.ee/analysis/api/tasks/recent/"
    body_POST_init = {"cats": [], "packs": [], "score": "", "offset": 0, "limit": limite_request}
    contador = 0

    headers = {
        "Connection": "keep-alive",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"98\", \"Google Chrome\";v=\"98\"",
        "sec-ch-ua-mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": "oTtoXlPh9ojm7V2yw2Pk0XVx9nGMBS64",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": "https://cuckoo.cert.ee",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://cuckoo.cert.ee/analysis/",
        "Accept-Language": "en,en-US;q=0.9,pt-BR;q=0.8,pt;q=0.7"
    }

    cookies = {
        "csrftoken": "oTtoXlPh9ojm7V2yw2Pk0XVx9nGMBS64",
        "ai_user": "uIGY1bru7A5YYddo0Bunvz|2022-02-13T02:19:45.299Z"
    }

    def start_requests(self):
        print("entrou no start_requests")
        #url = "https://cuckoo.cert.ee/analysis/api/tasks/recent/"
        #body_dict = {"cats": [], "packs": [], "score": "", "offset": 0, "limit": 100}
        #body_dict['offset'] = body_dict['offset'] + 100
        body_string = json.dumps(self.body_POST_init)
        #body_full_file = '{ "cats":[], "packs":[],"score":"","offset":0,"limit":1000000}'

        yield scrapy.http.Request(self.url,headers=self.headers, body=body_string, cookies=self.cookies, method="POST")

    def parse(self, response):
        print("dentro do parse contador: ", self.contador)
        print("offset: ", self.body_POST_init['offset'])
        self.contador += 1
        data = json.loads(response.body)

        linhas = data["tasks"]

        if (self.contador == 3):
            return

        #teste
        if(data == '' or data is None or response.body == '' or response.body is None):
            print("acabou")
            return

        #print("printando json de retorno: ",data)
        self.body_POST_init['offset'] = self.body_POST_init['offset'] + self.limite_request
        body_string = json.dumps(self.body_POST_init)

        yield scrapy.Request(self.url,callback=self.parse,headers=self.headers, body=body_string,cookies=self.cookies,method="POST")


        self.baixar_zip(linhas)

        #print("tipo linhas:",type(linhas))
        #print("quantidade linhas:", len(linhas))
        #print("achei id:",linhas[0].get("id"))

        #print("print das linhas:",linhas[0])

        #print("quantidade de linhas", len(linhas))

        # grava no arquivo as linhas da tabela, apenas teste
        #with open("cuckoo_table.txt", 'a') as f:
        #   for linha in linhas:
        #    print("id: ",linha.get("id"))
            #f.write(str(value[count].get("id")) + "\n")
               #f.write(str(linhas))

        return

    def baixar_zip(self,linhas):
        URL_DOWNLOAD = "https://cuckoo.cert.ee/analysis/2753987/export/"
        #r = requests.get(URL_DOWNLOAD, allow_redirects=True)
        #open('2753987.zip', 'wb').write(r.content)

        #for linha in linhas:
            #print("id: ", linha.get("id"))
