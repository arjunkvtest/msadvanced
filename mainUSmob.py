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
        'cookie': cookie,
        'referer': 'https://www.bing.com/search?q=usenow2&qs=n&form=QBRE&pc=U531&sp=-1&lq=1&pq=usenow&sc=1-6&sk=&cvid=2FB842E897154881AFF222851BEF59E1&ghsh=0&ghacc=0&ghpl=',
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
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36 Edg/111.0.0.0'
        }
        conn.request("GET", "/search?q=useno{}w2&qs=n&form=QBRE&pc=U531&sp=-1&lq=1&pq=usenow&sc=1-6&sk=&cvid=2FB842E897154881AFF222851BEF59E1&ghsh=0&ghacc=0&ghpl=&rdr=1&rdrig=6E6B26EFFA2B4591A534EF9C9618AF4D".format(rex), payload, headers)
        res = conn.getresponse()
        print(res.status)
        time.sleep(3)


accounts=[]
#ms1

#ms4
cookie4='MUID=1C77D27D47D268B40804C09946496985; _EDGE_V=1; SRCHD=AF=SHORUN; SRCHUID=V=2&GUID=787BCD8B9CF247A5A6714138A05F21A7&dmnchg=1; MUIDB=1C77D27D47D268B40804C09946496985; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=d759047a-925a-494d-b7bc-a8fa79427df6; _clck=k1wkg0|1|fad|1; MSCC=NR; _BINGNEWS=SW=1462&SH=754; ANIMIA=FRE=1; msaoptout=0; ipv6=hit=1680276828438&t=4; NAP=V=1.9&E=1bcf&C=X9OO8rob_YqVQNGmfRT3IxVwx40DIwzQiRzjAW8w3-M_r4HFZ-hkaA&W=1; SRCHS=PC=U531; CSRFCookie=dc1ca316-759a-4434-8e42-7cd9f89d359e; ANON=A=6802572D0FB4E1DA70439420FFFFFFFF&E=1c29&W=1; PPLState=1; KievRPSSecAuth=FABqBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACKWeevIquC7tKAQu9xgFV/i87z72yYKE9lwgXZ/iCSp4vHnaL7ivz5A7xr7WLa3V/iTt6PdKsH3MajjL/sjL6wHezrh5XPowCPjXZ0toVpoDSszbDt17EjYIll0c+cjbkIJCVMQZjGSIjenXi8X/3nl4Iw8QVvGt1pdI3ea/WEQXQwpiYV+TbBvvqBzUHrjpshXw+oe93WgZn7LgwBPhAUDaAbyFbOqii8WC6WdT9rKILUmV6pwmko00PssLgqUT652k1y0veIn74p4/kMVgXyXSpM0dgkDJGGrx4E8ykdJqQUzGG4immo4wbvfQNnDwZRbspz5bamJ52PCgBSJsW9bnQguf61WklkFseJfOnMIMw+9xTw22APbEvXxaswwRZmJMT42UzSeYGPD4b/OpM1wL9w2PfJ6f9VjFdPRhmgg+RYz4DIn6d9bGqj811TYn4Oqq7y0JJYJasZO+ZM+maCcjnjsN5ucAfGPPcLlttGT66TqtuB3nZv6TvzjM/kYW7UtaGObLRpSxfCWiQTh9Skoue9Ew5rhAWZHIsYk7/XIZbnSQdBy5sSRY0PSeIL41G+ZtS8K31IrWEc23qcuiXLL0TX5Nu/vH7to2ha6YNP9nkv6gHXPQQPHIcqiSvRfTTTn/emvhRM9kIYfDDQWVGDqX2+4WtcoT9JtmXYDSCeWkF5jS63AlECJj3KX6d71CYzpwLvOofFXZXOfdlUoPZgG3LC/Z344VtgUlOh52q6YuVf0yuXdcgfhSmXV3Npqz65OlRZfDldh/ufsAK0lRqYjU+9ISUaUhiIoWjzBCcoMA6HsrHjkvEk1bjsumr8TOqo9AX9/+bytEe55QKAvxfa20ecLw5XIIa9Iz0G1K9ciyUN7qO1Zr666LOIvBKU80ROWkRJunmh4hCjgJMHbNMOoMIR1CqEbiKz7duwI8uncRfvFPAu5a4vbLz7+KpW9I7L948EnKenK25eAzSKZYxr+6f7ySl9F5YP5gIk7njYHpDZBt/M7JlyQIQv1hp5flnMjqXzyFRQtOEpr1vovMbzIj3BXQmt/KXAKGlvV6mau45t0UOo4CmIn7r3H/d2Ji2BTATT94vYptI3BURvjEtnnFiE64M0Y31StZa0pPQ8gEi5rK6xa05X52zAcjosTLTyN8ootL7vTEsKvMAUGcz9Z/PMdvRvLlou/qNPpYCq3B/M34A2pdRL2NfHxqDcgdr14ghbvu9LeJKtSifEkKGGzm72AKCxqT15V3U0xlRb3+bIfnOj+NgfpiNOx0nmt55D1eJ02NOMG34vvRfprqtzj8J/C9a9SuJuPqU3PZXi14Kw1dGJu+Emjf5DnL96OPQ2LDj0uekqHEDYbQRRolE80Seog+jFEEhdyPN2NBj4CwF5Y13KuNzJ9QrmHWu1XyZytcvmdWkgPeLCvkrvcivv67dBQADbT3MNB6YNAWfyw/B+H/HulUf7s=; _U=1Dur3yxkxynVEwp24IjcQIn9l76FVeBdEBtxTkHOuiAdI7D44CJvPFC9GwsG04A5WT62OE512hw_NGaad4BKhVSYXZ1OUx5115ZE13mppY2fQkvwdmgPJi2MzXwo1t5oAlmWvvQtnBi33E4xOGpVBcHAD1xgQVqqJn5WQ2rCBvyQNIeuOigQG03zM_QVZps2WSXA4WoSZeIurZkiubzR4OQ; WLS=C=bdab2aa2c531e7d3&N=Arjun; WLID=UJIazOq83STP8LV6kRXP9XrpcUtKQHjV0A24XyroMzGqsyXGD10zSGNsG5u1v53zY0BHH9gtykLKWUOYdxs7Wdw4gVWA4mh4birs++ZwErY=; SUID=A; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMy0zMVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NDh9; SRCHUSR=DOB=20230330&T=1680273425000; ABDEF=V=13&ABDV=11&MRNB=1680274730180&MRB=0; USRLOC=HS=1&ELOC=LAT=30.50135040283203|LON=38.20066833496094|N=Al%20Rahmanyah%20District%2C%20Al%20Jawf|ELT=4|; _uetsid=5e0cb1f0cfa311edad32810c572617c4; _uetvid=53d86080ced511ed9f5d614d78e12b62; _EDGE_S=SID=2119A1A8A1A0668E3EBAB34DA0E36738&mkt=en-us&ui=en-us; _clsk=8ck1t3|1680275938315|132|1|p.clarity.ms/collect; _SS=SID=3B95457513B16F360223579012F26E28&R=728&RB=728&GB=0&RG=0&RP=728&PC=U531&OCID=MY00CH&BTQID=-&BTSTKey=-&RA=-&BTOID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-; _RwBf=ilt=1&ihpd=1&ispd=0&rc=728&rb=728&gb=0&rg=0&pc=728&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=68&l=2023-03-31T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=None&c=MOBILE&t=6337&s=2023-03-30T13:31:11.2036700+00:00&ts=2023-03-31T15:19:20.9276495+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&W=1&mta=0&e=2xFgSNm-JO3av2T6OTua4BA8YoJUrEmwBYOgcuDOAYwaG_Gfj6bUzKWyt3JbJAJKyYvJpl1WJnZk_BEMwsgvUg&A=6802572D0FB4E1DA70439420FFFFFFFF; SRCHHPGUSR=SRCHLANG=en&DM=0&PV=11&BRW=MW&BRH=MT&CW=394&CH=851&SCW=394&SCH=851&DPR=2.8&UTC=330&HV=1680275963&PRVCW=1164&PRVCH=2518&EXLTT=31&WTS=63815870174; SRCHHPGUSR=SRCHLANG=en&BRW=XW&BRH=M&CW=1536&CH=758&SCW=1519&SCH=3682&DPR=1.3&UTC=330&DM=1&WTS=63815849103&HV=1680252946&PRVCW=1536&PRVCH=758&PV=10.0.0; MUIDB=1C77D27D47D268B40804C09946496985'


accounts.append(cookie4)


n=35
for cookie in accounts:
    process(cookie,n)