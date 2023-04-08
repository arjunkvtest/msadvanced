from urllib.parse import urljoin
import json
import http.client
import random
import time


def getScript( url):
    connection = http.client.HTTPSConnection("script.googleusercontent.com")
    connection.request('GET', url)
    response = connection.getresponse()
    location_header = response.getheader('location')
    if location_header is None:
        return response
    else:
        location = urljoin(url, location_header)
        return getScript(location)

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
        conn.close
    except:
        print("Connection failed")

def processIndPc(cookie,num):        
    for x in range(num):
        rex = randomWords()
        conn = http.client.HTTPSConnection("www.bing.com")
        payload = ''
        headers = {
        'authority': 'www.bing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': cookie,
        'referer': 'https://www.bing.com/',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"111.0.1661.62"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="111.0.1661.62", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'
        }
        try:
            conn.request("GET", "/search?q={}&qs=n&form=QBRE&sp=-1&lq=0&pq=firstinb&sc=10-8&sk=&cvid=7178BC7EB63B4E958422EE8819EB4D6F&ghsh=0&ghacc=0&ghpl=".format(rex), payload, headers)
            res = conn.getresponse()
            if(res.status==200):
                print(x+1)
            time.sleep(1)
        except :
            print("failed")

def processIndMob(cookie,num):        
    for x in range(num):
        rex = randomWords()
        conn = http.client.HTTPSConnection("www.bing.com")
        payload = ''
        headers = {
        'authority': 'www.bing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'avail-dictionary': '5WIuc1mB',
        'cookie': cookie,
        'referer': 'https://www.bing.com/search?q=fun&form=QBLH',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"111.0.1661.62"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="111.0.1661.62", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.149"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Pixel 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/111.0.0.0'
        }
        try:
            conn.request("GET", "/search?q={}&qs=n&form=QBRE&sp=-1&lq=0&pq=bringz&sc=10-6&sk=&cvid=48F2B391A67941FF8CAFA330EDBA34AB&ghsh=0&ghacc=0&ghpl=".format(rex), payload, headers)
            res = conn.getresponse()
            if(res.status==200):
                print(x+1)
            time.sleep(1)
        except:
            print("failed")

def getBalance(start=None,end=None):
    if (start==None and end==None):
        for user in data:
            # print(user["name"],"=",end="")
            balance(user["cookie"],user["payload"])
    elif(end==None):
        print(data[start-1]["name"],end="=")
        balance(data[start-1]["cookie"],data[start-1]["payload"])
    else:
        for i in range(start-1,end):
            # print(data[i]["name"],"=",end="")
            balance(data[i]["cookie"],data[i]["payload"])

def runIndiaPc(pcNum,start=None,end=None):
    print("runnning india pc")
    if (start==None and end==None):
        for user in data:
            print(user["name"],"=",end="")
            processIndPc(user["cookieIn"],pcNum)
    elif(end==None):
        print(data[start-1]["name"],end="=")
        processIndPc(data[start-1]["cookieIn"],pcNum)
    else:
        for i in range(start-1,end):
            print(data[i]["name"],"=",end="")
            processIndPc(data[i]["cookieIn"],pcNum)

def runIndiaMob(MobNum,start=None,end=None):
    print("running india mob")
    if (start==None and end==None):
        for user in data:
            print(user["name"],"=",end="")
            processIndMob(user["cookieIn"],MobNum)
    elif(end==None):
        print(data[start-1]["name"],end="=")
        processIndMob(data[start-1]["cookieIn"],MobNum)
    else:
        for i in range(start-1,end):
            print(data[i]["name"],"=",end="")
            processIndMob(data[i]["cookieIn"],MobNum)

def randomWords():
    sentence=''
    for i in range(3):
        sentence += random.choice(words)
        if(i<2):
            sentence+="+"
    return(sentence)

def getWords():  
    conn = http.client.HTTPSConnection("svnweb.freebsd.org")
    path = "/csrg/share/dict/words?view=co&content-type=text/plain"
    conn.request("GET", path)
    response = conn.getresponse()
    long_txt = response.read().decode()
    return(long_txt.splitlines())

words = getWords()
url = "/macros/echo?user_content_key=OhXWUnaehAbEV70308fc-xjG7y5mOkpOYLQMrj6Na_w8i2U2bj2Pd6DtcZxDx7v7etNBYoPYVuY9IDOxTZ0sGMyazRSE9trtm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnO4fKPg94uZEnJYx4LRx0bJ6OanAT-hCpsrio_vbjQ_qbmp5nt1l32-SD7GcQDUuVYrXglU0r_H2uNHwC3Fe6R5HB6qA6zxzOw&lib=MxsreQc10Fcxinxag_dhHEUCAssumqzID"
response = getScript(url)
data=json.loads(response.read())

# print(data[31]["cookieUs"])
getBalance(4,5)
# runIndiaPc(36,26,30)
# runIndiaMob(22,26,30)
