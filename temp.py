import http.client
import json


def balance(cookie,payloadstr):
    conn = http.client.HTTPSConnection("rewards.bing.com")
    payload = payloadstr
    headers = {
    'authority': 'rewards.bing.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': cookie,
    'correlation-context': 'v=1,ms.b.tel.market=en-US',
    'origin': 'https://rewards.bing.com',
    'referer': 'https://rewards.bing.com/',
    'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"111.0.1661.54"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'
    }
    try:
        conn.request("POST", "/api/reportactivity?X-Requested-With=XMLHttpRequest", payload, headers)
        res = conn.getresponse()
        data = res.read()
        data=(data.decode("utf-8"))
        reward=json.loads(data)
        print(reward["balance"])
        conn.close()
    except:
        print("Connection failed")


conn = http.client.HTTPSConnection("crazy-headscarf-crab.cyclic.app")
conn.request("GET", "/")
res = conn.getresponse()
data = json.loads(res.read())
for obj in data:
    print(obj["email"])
    balance(obj["cookie"],obj["payload"])