# US PC

import http.client

import string
import random
import time

def process(cookie,num):        
    for x in range(num):
        N = 7
        rex = ''.join(random.choices(string.ascii_lowercase +string.digits, k=N))
        rex=rex+str(x)
        conn = http.client.HTTPSConnection("www.bing.com")
        payload = ''
        headers = {
        'authority': 'www.bing.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'avail-dictionary': '5WIuc1mB',
        'cookie': cookie,
        'referer': 'https://www.bing.com/search?q=bring&cvid=dc8f04df41a54794b318d062f2559315&aqs=edge.0.69i59j0j46l2j0l5.1058j0j4&FORM=ANAB01&PC=U531',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-arch': '""',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"111.0.1661.54"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="111.0.1661.54", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.111"',
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
        conn.request("GET", "/search?q=bri{}ngz&qs=n&form=QBRE&sp=-1&lq=0&pq=bringz&sc=10-6&sk=&cvid=48F2B391A67941FF8CAFA330EDBA34AB&ghsh=0&ghacc=0&ghpl=".format(rex), payload, headers)
        res = conn.getresponse()
        print(res.status)
        time.sleep(1)


accounts=[]

#m6
cookie6='MUID=25E083CFAD9A6E470B45912AAC6D6F51; _EDGE_V=1; SRCHD=AF=SHORUN; SRCHUID=V=2&GUID=56B29CEF22F445F997C9063C2DFF836A&dmnchg=1; MUIDB=25E083CFAD9A6E470B45912AAC6D6F51; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=bc909d66-7483-4800-afd0-3ce4804e6948; CSRFCookie=153ed28c-6b07-41b5-b8e8-4f5fac44d9db; ANON=A=27F2BA8D40BC138B4EC141D8FFFFFFFF&E=1c29&W=1; NAP=V=1.9&E=1bcf&C=tu8FUR4TYST4B8-70O1DryWe3jM6AJ3xLa2BOwnP1xgqrSHlzWYGjQ&W=1; PPLState=1; KievRPSSecAuth=FABqBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACKHR92PD5OzLKAREusRjK/1HajzfDsbskyrYDFahlHwIQEiS8XRrsC6qMDHkvSp8ZUsFEQuxs0jOFzPrxyg6EYTvemjGafHAzlwhpZix6BHRhHYFu9x3KYrP262a3FCcp31iuGKBiDy3P9vGE3g0RvBGj7gw25AWWLnjtH4sOFG362PrpuA6iTQIk3jC23qgeZfwpn32rvhoYkqJqabdWwiBXpEGa1tKQ4VKi3MaMaB1mdjHSIwSW2lsfJqf5SoPPOHmsExdwjBHL90HUs3sot1O8xz8qpAkPhzE7dWaGBGfPez98RiqmaLtJ7XQnkdCjnMdeFbzkhLvIg7Gzu7P1Z3DcV/PKj2ZtHmYlsgxeifiQti+Kue+3yx7TekBUU7WZyimOjvakTb5WdpLNdA91CuAGycgP2BbSg2ND+L5Hr8obcV1QZq6C+DbO7h7oq4in0NN4EV8i41EYfsqHaSb+3or/lS6cngn1Ff6M5Q7yA+kfhpQls3VYHHcgjZPiZVzja/4Yez4ZVFDd13b85fVjXZHueF2GEnbuBB3A9tIAuTcz5gyJ4ZPvKEy8lTOVkEw6UwGPVal+Ae3k5aDvs+eD1EAP1735JUIwxh3MBvDTg0aWfiHMtk9AYwLyt+3s4sL37KpEZR0iSygm88SDDhREmexvCQKPtF1C/cc76fNP2VfFsGqzH6pIoQjA5oIqUmGKa69BmvItdOo9o6tGkNfNseBxF/0Hq115ZIPG7YPJACL/SbUoAzkpeDPVLlKWGpDrHGjJus9wI+rOUp3fsxrCPy4agAnxezBAm+hmCRPdRSkn202bsvxjpD+rJ1ZJ3wn+ShXsJ1qHeUoXJfP4O4FzTGeP7LGk+UckTo7N1moUvqmVABaJqN6iri8hmVrmxSe+iWfqegTf6dQN6ER7PCbknXbthCvLVQCcBNjB2r24sUtRhfMVFuqGtZQvvbrMDTZWOMib7m3Bb32d3XwT5+uY94Z28Q/aveq6hyLxSi+yTugh2PbJf1FY4ZQlnYve9Qd7hVXEuMOyUE4/NRjtrd3r6T1EExkw5K9okkPTEElUC8DskpesJvlROWbbNWyIfzXi5FCrjDdTx+R/75s8SW/PcnyfCHeyayDV9SLnB4kg9go3LOPsNmjVjJ1wCu2JzH58kRNx7IODVvtA82Hi1LpzTbtqj4F3pNjkdLtMxU1063taSs8QtYs86eJijOtP9jRP8wxQpG5pTwcxrvxS32equKLQ3RtSWFCesB4ddYVEIO4NwmybXmm7dYyhBMOlm1gPAI+XfJA0vrPznqEbNnVCP1O8S2fekVP3VWMFHzOjUYpJWwH65jxCOAxSO6aJcMcGK/ftxSTB6V8PYe1v3kYzuj/VgsltFiEonDmYstlrWCAmlCRD04YDkkeonRKcSHbNa7CxgZl9xGnzyuahuOav+SxkxQAeDyc0TxsRCtgJ7Sq0IUX+CYgkkI=; _U=1XpsIU6aAHkFby6cI2pEse59d7AFQVGy3VvWcaPSWdxBLJRtmvPckOW7bwPvnMWVu783WjAfkaASpGJwF-VU2Z3pdmJqRrgsNI20kJvtuHk1ureUkvWYOUEVH6Bk9COkaYohYCI8B4hOkzs78BPiQeN4PvQbLeS6GLrjjbGbfNtkJlndiaA5mhjzpJWehmCNXuQGn-xPeSDdYFlyEU67YfQ; WLS=C=a6fe7921274d781d&N=Arjun; WLID=EIiNPobb2KIErV9lLgaV89uHjUnWT6NPJHbbJurPaoK8T0R+z7cPcKIiL3328j7yYzmygmM8NHr5TSycdULhjXefL5m0JFzkTCg/aLs11ck=; SUID=A; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMy0zMVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6Mn0=; MSCC=NR; _BINGNEWS=SW=907&SH=737; _clck=x50i0w|1|fad|1; ANIMIA=FRE=1; _EDGE_S=F=1&SID=0165290FE560691B01E93BEAE49768F8&mkt=EN-US&ui=en-us; ABDEF=V=13&ABDV=11&MRNB=1680287779638&MRB=0; SRCHUSR=DOB=20230331&T=1680288370000&POEX=W; ipv6=hit=1680291981511&t=4; _uetsid=eae47f60cfeb11ed9608b183dfb064f6; _uetvid=eae4ed00cfeb11ed9a99f1f2acc01bc1; _SS=SID=0165290FE560691B01E93BEAE49768F8&R=498&RB=498&GB=0&RG=0&RP=498&OCID=ML2BF1&BTQID=-&BTSTKey=-&RA=-&BTOID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-&PC=U531; SRCHS=PC=U531; ai_session=IkRPLTehwzIeqP3FgL7270|1680288694977|1680288694977; dsc=order=News; _RwBf=ilt=1&ihpd=1&ispd=0&rc=498&rb=498&gb=0&rg=0&pc=498&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=46&l=2023-03-31T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGTRIAL5TO250P201808&c=MY00IA&t=866&s=2023-03-31T17:41:01.0182039+00:00&ts=2023-03-31T18:51:37.8942547+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&mta=0&e=X9Efaph0NFmTO1UqqR8DilgF-VWaKLToHHuFRGCOB93ExjvHwxVM5lCTf3boCoP544J34pZBFlzx4Px2x8ODlg&A=27F2BA8D40BC138B4EC141D8FFFFFFFF; USRLOC=HS=1&ELOC=LAT=9.492409706115723|LON=76.33300018310547|N=Alleppey%2C%20Kerala|ELT=4|&DLOC=LAT=37.733543|LON=-122.391975|A=22402|N=San+Francisco%2c+San+Francisco+Co.|C=|S=|TS=230331185138|ETS=230331190138|; _clsk=1vn9o5|1680288702416|53|1|s.clarity.ms/collect; SRCHHPGUSR=SRCHLANG=en&DM=0&PV=11&BRW=S&BRH=T&CW=1164&CH=2518&SCW=1164&SCH=3506&DPR=1.3&UTC=330&WTS=63815881183&HV=1680288698&PRVCW=1462&PRVCH=754&EXLTT=31; SRCHHPGUSR=SRCHLANG=en&BRW=XW&BRH=M&CW=1536&CH=758&SCW=1519&SCH=3682&DPR=1.3&UTC=330&DM=1&WTS=63815849103&HV=1680252946&PRVCW=1536&PRVCH=758&PV=10.0.0; _EDGE_S=F=1&SID=0165290FE560691B01E93BEAE49768F8&mkt=en-us&ui=en-us; _SS=SID=0165290FE560691B01E93BEAE49768F8&R=123&RB=123&GB=0&RG=0&RP=73&OCID=ML2CLB; MUIDB=25E083CFAD9A6E470B45912AAC6D6F51'



accounts.append(cookie6)
n=35
for cookie in accounts:
    process(cookie,n)