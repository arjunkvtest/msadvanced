# INDIA PC

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
        'referer': 'https://www.bing.com/search?q=firstin&cvid=c8aa306149dd48a7889ce514b557501e&aqs=edge..69i57j0l8.3578j0j1&pglt=2083&FORM=ANNTA1&PC=U531',
        'sec-ch-ua': '"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"111.0.1661.54"',
        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="111.0.1661.54", "Not(A:Brand";v="8.0.0.0", "Chromium";v="111.0.5563.111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'
        }
        conn.request("GET", "/search?q=firstin{}b&qs=n&form=QBRE&sp=-1&lq=0&pq=firstinb&sc=10-8&sk=&cvid=7178BC7EB63B4E958422EE8819EB4D6F&ghsh=0&ghacc=0&ghpl=".format(rex), payload, headers)
        res = conn.getresponse()
        print(res.status)
        time.sleep(1)



accounts=[]
#ms1

#ms4
cookie4='MUID=1C77D27D47D268B40804C09946496985; _EDGE_V=1; SRCHD=AF=SHORUN; SRCHUID=V=2&GUID=787BCD8B9CF247A5A6714138A05F21A7&dmnchg=1; MUIDB=1C77D27D47D268B40804C09946496985; _UR=QS=0&TQS=0; MicrosoftApplicationsTelemetryDeviceId=d759047a-925a-494d-b7bc-a8fa79427df6; _clck=k1wkg0|1|fad|1; MSCC=NR; _BINGNEWS=SW=1462&SH=754; ANIMIA=FRE=1; msaoptout=0; ipv6=hit=1680276828438&t=4; NAP=V=1.9&E=1bcf&C=X9OO8rob_YqVQNGmfRT3IxVwx40DIwzQiRzjAW8w3-M_r4HFZ-hkaA&W=1; SRCHS=PC=U531; CSRFCookie=dc1ca316-759a-4434-8e42-7cd9f89d359e; ANON=A=6802572D0FB4E1DA70439420FFFFFFFF&E=1c29&W=1; PPLState=1; KievRPSSecAuth=FABqBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACKWeevIquC7tKAQu9xgFV/i87z72yYKE9lwgXZ/iCSp4vHnaL7ivz5A7xr7WLa3V/iTt6PdKsH3MajjL/sjL6wHezrh5XPowCPjXZ0toVpoDSszbDt17EjYIll0c+cjbkIJCVMQZjGSIjenXi8X/3nl4Iw8QVvGt1pdI3ea/WEQXQwpiYV+TbBvvqBzUHrjpshXw+oe93WgZn7LgwBPhAUDaAbyFbOqii8WC6WdT9rKILUmV6pwmko00PssLgqUT652k1y0veIn74p4/kMVgXyXSpM0dgkDJGGrx4E8ykdJqQUzGG4immo4wbvfQNnDwZRbspz5bamJ52PCgBSJsW9bnQguf61WklkFseJfOnMIMw+9xTw22APbEvXxaswwRZmJMT42UzSeYGPD4b/OpM1wL9w2PfJ6f9VjFdPRhmgg+RYz4DIn6d9bGqj811TYn4Oqq7y0JJYJasZO+ZM+maCcjnjsN5ucAfGPPcLlttGT66TqtuB3nZv6TvzjM/kYW7UtaGObLRpSxfCWiQTh9Skoue9Ew5rhAWZHIsYk7/XIZbnSQdBy5sSRY0PSeIL41G+ZtS8K31IrWEc23qcuiXLL0TX5Nu/vH7to2ha6YNP9nkv6gHXPQQPHIcqiSvRfTTTn/emvhRM9kIYfDDQWVGDqX2+4WtcoT9JtmXYDSCeWkF5jS63AlECJj3KX6d71CYzpwLvOofFXZXOfdlUoPZgG3LC/Z344VtgUlOh52q6YuVf0yuXdcgfhSmXV3Npqz65OlRZfDldh/ufsAK0lRqYjU+9ISUaUhiIoWjzBCcoMA6HsrHjkvEk1bjsumr8TOqo9AX9/+bytEe55QKAvxfa20ecLw5XIIa9Iz0G1K9ciyUN7qO1Zr666LOIvBKU80ROWkRJunmh4hCjgJMHbNMOoMIR1CqEbiKz7duwI8uncRfvFPAu5a4vbLz7+KpW9I7L948EnKenK25eAzSKZYxr+6f7ySl9F5YP5gIk7njYHpDZBt/M7JlyQIQv1hp5flnMjqXzyFRQtOEpr1vovMbzIj3BXQmt/KXAKGlvV6mau45t0UOo4CmIn7r3H/d2Ji2BTATT94vYptI3BURvjEtnnFiE64M0Y31StZa0pPQ8gEi5rK6xa05X52zAcjosTLTyN8ootL7vTEsKvMAUGcz9Z/PMdvRvLlou/qNPpYCq3B/M34A2pdRL2NfHxqDcgdr14ghbvu9LeJKtSifEkKGGzm72AKCxqT15V3U0xlRb3+bIfnOj+NgfpiNOx0nmt55D1eJ02NOMG34vvRfprqtzj8J/C9a9SuJuPqU3PZXi14Kw1dGJu+Emjf5DnL96OPQ2LDj0uekqHEDYbQRRolE80Seog+jFEEhdyPN2NBj4CwF5Y13KuNzJ9QrmHWu1XyZytcvmdWkgPeLCvkrvcivv67dBQADbT3MNB6YNAWfyw/B+H/HulUf7s=; _U=1Dur3yxkxynVEwp24IjcQIn9l76FVeBdEBtxTkHOuiAdI7D44CJvPFC9GwsG04A5WT62OE512hw_NGaad4BKhVSYXZ1OUx5115ZE13mppY2fQkvwdmgPJi2MzXwo1t5oAlmWvvQtnBi33E4xOGpVBcHAD1xgQVqqJn5WQ2rCBvyQNIeuOigQG03zM_QVZps2WSXA4WoSZeIurZkiubzR4OQ; WLS=C=bdab2aa2c531e7d3&N=Arjun; WLID=UJIazOq83STP8LV6kRXP9XrpcUtKQHjV0A24XyroMzGqsyXGD10zSGNsG5u1v53zY0BHH9gtykLKWUOYdxs7Wdw4gVWA4mh4birs++ZwErY=; SUID=A; _HPVN=CS=eyJQbiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MiwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMy0zMVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6NDh9; ai_session=MHqiCQKvLzTeHcLCN+bk6Z|1680272959287|1680273403242; _EDGE_S=SID=2119A1A8A1A0668E3EBAB34DA0E36738&mkt=en-us&ui=en-us; ABDEF=V=13&ABDV=11&MRNB=1680273428890&MRB=0; SRCHUSR=DOB=20230330&T=1680273425000; _uetsid=5e0cb1f0cfa311edad32810c572617c4; _uetvid=53d86080ced511ed9f5d614d78e12b62; USRLOC=HS=1&ELOC=LAT=9.492409706115723|LON=76.33300018310547|N=Alleppey%2C%20Kerala|ELT=4|; _SS=SID=3B95457513B16F360223579012F26E28&R=168&RB=168&GB=0&RG=0&RP=155&PC=U531&OCID=ML2CLC; dsc=order=TravelHub; _RwBf=ilt=1&ihpd=1&ispd=0&rc=168&rb=168&gb=0&rg=0&pc=155&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=6&l=2023-03-31T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=None&c=MOBILE&t=6337&s=2023-03-30T13:31:11.2036700+00:00&ts=2023-03-31T14:54:22.9373781+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&W=1&mta=0&e=2xFgSNm-JO3av2T6OTua4BA8YoJUrEmwBYOgcuDOAYwaG_Gfj6bUzKWyt3JbJAJKyYvJpl1WJnZk_BEMwsgvUg&A=6802572D0FB4E1DA70439420FFFFFFFF; _clsk=8ck1t3|1680274467350|112|1|p.clarity.ms/collect; SRCHHPGUSR=SRCHLANG=en&DM=0&PV=10.0.0&BRW=HTP&BRH=M&CW=896&CH=754&SCW=1164&SCH=2270&DPR=1.3&UTC=330&HV=1680274463&PRVCW=1479&PRVCH=754&EXLTT=31&WTS=63815870174; SRCHHPGUSR=SRCHLANG=en&BRW=XW&BRH=M&CW=1536&CH=758&SCW=1519&SCH=3682&DPR=1.3&UTC=330&DM=1&WTS=63815849103&HV=1680252946&PRVCW=1536&PRVCH=758&PV=10.0.0; MUIDB=1C77D27D47D268B40804C09946496985'

#ms6
cookie6='MUID=25E083CFAD9A6E470B45912AAC6D6F51; _EDGE_V=1; SRCHD=AF=SHORUN; SRCHUID=V=2&GUID=56B29CEF22F445F997C9063C2DFF836A&dmnchg=1; MUIDB=25E083CFAD9A6E470B45912AAC6D6F51; _UR=QS=0&TQS=0; ipv6=hit=1680287984485&t=4; MicrosoftApplicationsTelemetryDeviceId=bc909d66-7483-4800-afd0-3ce4804e6948; CSRFCookie=153ed28c-6b07-41b5-b8e8-4f5fac44d9db; SRCHUSR=DOB=20230331&T=1680284383000&POEX=W; ANON=A=27F2BA8D40BC138B4EC141D8FFFFFFFF&E=1c29&W=1; NAP=V=1.9&E=1bcf&C=tu8FUR4TYST4B8-70O1DryWe3jM6AJ3xLa2BOwnP1xgqrSHlzWYGjQ&W=1; PPLState=1; KievRPSSecAuth=FABqBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACKHR92PD5OzLKAREusRjK/1HajzfDsbskyrYDFahlHwIQEiS8XRrsC6qMDHkvSp8ZUsFEQuxs0jOFzPrxyg6EYTvemjGafHAzlwhpZix6BHRhHYFu9x3KYrP262a3FCcp31iuGKBiDy3P9vGE3g0RvBGj7gw25AWWLnjtH4sOFG362PrpuA6iTQIk3jC23qgeZfwpn32rvhoYkqJqabdWwiBXpEGa1tKQ4VKi3MaMaB1mdjHSIwSW2lsfJqf5SoPPOHmsExdwjBHL90HUs3sot1O8xz8qpAkPhzE7dWaGBGfPez98RiqmaLtJ7XQnkdCjnMdeFbzkhLvIg7Gzu7P1Z3DcV/PKj2ZtHmYlsgxeifiQti+Kue+3yx7TekBUU7WZyimOjvakTb5WdpLNdA91CuAGycgP2BbSg2ND+L5Hr8obcV1QZq6C+DbO7h7oq4in0NN4EV8i41EYfsqHaSb+3or/lS6cngn1Ff6M5Q7yA+kfhpQls3VYHHcgjZPiZVzja/4Yez4ZVFDd13b85fVjXZHueF2GEnbuBB3A9tIAuTcz5gyJ4ZPvKEy8lTOVkEw6UwGPVal+Ae3k5aDvs+eD1EAP1735JUIwxh3MBvDTg0aWfiHMtk9AYwLyt+3s4sL37KpEZR0iSygm88SDDhREmexvCQKPtF1C/cc76fNP2VfFsGqzH6pIoQjA5oIqUmGKa69BmvItdOo9o6tGkNfNseBxF/0Hq115ZIPG7YPJACL/SbUoAzkpeDPVLlKWGpDrHGjJus9wI+rOUp3fsxrCPy4agAnxezBAm+hmCRPdRSkn202bsvxjpD+rJ1ZJ3wn+ShXsJ1qHeUoXJfP4O4FzTGeP7LGk+UckTo7N1moUvqmVABaJqN6iri8hmVrmxSe+iWfqegTf6dQN6ER7PCbknXbthCvLVQCcBNjB2r24sUtRhfMVFuqGtZQvvbrMDTZWOMib7m3Bb32d3XwT5+uY94Z28Q/aveq6hyLxSi+yTugh2PbJf1FY4ZQlnYve9Qd7hVXEuMOyUE4/NRjtrd3r6T1EExkw5K9okkPTEElUC8DskpesJvlROWbbNWyIfzXi5FCrjDdTx+R/75s8SW/PcnyfCHeyayDV9SLnB4kg9go3LOPsNmjVjJ1wCu2JzH58kRNx7IODVvtA82Hi1LpzTbtqj4F3pNjkdLtMxU1063taSs8QtYs86eJijOtP9jRP8wxQpG5pTwcxrvxS32equKLQ3RtSWFCesB4ddYVEIO4NwmybXmm7dYyhBMOlm1gPAI+XfJA0vrPznqEbNnVCP1O8S2fekVP3VWMFHzOjUYpJWwH65jxCOAxSO6aJcMcGK/ftxSTB6V8PYe1v3kYzuj/VgsltFiEonDmYstlrWCAmlCRD04YDkkeonRKcSHbNa7CxgZl9xGnzyuahuOav+SxkxQAeDyc0TxsRCtgJ7Sq0IUX+CYgkkI=; _U=1XpsIU6aAHkFby6cI2pEse59d7AFQVGy3VvWcaPSWdxBLJRtmvPckOW7bwPvnMWVu783WjAfkaASpGJwF-VU2Z3pdmJqRrgsNI20kJvtuHk1ureUkvWYOUEVH6Bk9COkaYohYCI8B4hOkzs78BPiQeN4PvQbLeS6GLrjjbGbfNtkJlndiaA5mhjzpJWehmCNXuQGn-xPeSDdYFlyEU67YfQ; WLS=C=a6fe7921274d781d&N=Arjun; WLID=EIiNPobb2KIErV9lLgaV89uHjUnWT6NPJHbbJurPaoK8T0R+z7cPcKIiL3328j7yYzmygmM8NHr5TSycdULhjXefL5m0JFzkTCg/aLs11ck=; SUID=A; ai_session=SY0S/nH2aF7Mn5Qe1/SlP9|1680284385144|1680284465647; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wMy0zMVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6Mn0=; MSCC=NR; USRLOC=HS=1&ELOC=LAT=9.492409706115723|LON=76.33300018310547|N=Alleppey%2C%20Kerala|ELT=4|; _clck=yjvd6y|1|fad|0; _EDGE_S=F=1&SID=0165290FE560691B01E93BEAE49768F8&mkt=en-in; _BINGNEWS=SW=907&SH=737; _clsk=1vn9o5|1680284521429|2|0|s.clarity.ms/collect; SRCHHPGUSR=SRCHLANG=en&DM=0&PV=10.0.0&BRW=W&BRH=M&CW=1479&CH=754&SCW=1462&SCH=2747&DPR=1.3&UTC=330&WTS=63815881183&HV=1680284521&PRVCW=1479&PRVCH=754&EXLTT=1; _RwBf=ilt=1&ihpd=1&ispd=0&rc=26&rb=26&gb=0&rg=0&pc=23&mtu=0&rbb=0.0&g=0&cid=&clo=0&v=5&l=2023-03-31T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=0&p=BINGTRIAL5TO250P201808&c=MY00IA&t=866&s=2023-03-31T17:41:01.0182039+00:00&ts=2023-03-31T17:42:01.5054094+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&mta=0&e=X9Efaph0NFmTO1UqqR8DilgF-VWaKLToHHuFRGCOB93ExjvHwxVM5lCTf3boCoP544J34pZBFlzx4Px2x8ODlg&A=; _SS=SID=0165290FE560691B01E93BEAE49768F8&R=26&RB=26&GB=0&RG=0&RP=23&OCID=ML2BF3; SRCHHPGUSR=SRCHLANG=en&BRW=XW&BRH=M&CW=1536&CH=758&SCW=1519&SCH=3682&DPR=1.3&UTC=330&DM=1&WTS=63815849103&HV=1680252946&PRVCW=1536&PRVCH=758&PV=10.0.0; MUIDB=1C77D27D47D268B40804C09946496985'



accounts.append(cookie4)
accounts.append(cookie6)
n=35
for cookie in accounts:
    process(cookie,n)





