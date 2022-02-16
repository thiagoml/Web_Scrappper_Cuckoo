from scrapy import Request

url = 'https://cuckoo.cert.ee/analysis/api/tasks/recent/'

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

body = '{"cats":[],"packs":[],"score":"","offset":100,"limit":100}'

request = Request(
    url=url,
    method='POST',
    dont_filter=True,
    cookies=cookies,
    headers=headers,
    body=body,
)

#fetch(request)


