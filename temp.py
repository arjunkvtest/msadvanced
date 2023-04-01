import http.client

conn = http.client.HTTPSConnection("www.bing.com")
payload = ''
headers = {
  'authority': 'www.bing.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9',
  'avail-dictionary': '5WIuc1mB',
  'cookie': '_EDGE_V=1; SRCHD=AF=SHORUN; SRCHUID=V=2&GUID=B2EE1C79C2904519B9C8F227DB317C08&dmnchg=1; MUID=3691EDCB2A10670626D1FF2D2BB66610; MUIDB=3691EDCB2A10670626D1FF2D2BB66610; _UR=QS=0&TQS=0; ipv6=hit=1680342138422&t=4; MicrosoftApplicationsTelemetryDeviceId=b0f91c6c-5d7a-4195-aaad-36e8250e3fd6; CSRFCookie=a0ff5903-ad69-4070-ad76-f905f15b1710; SRCHUSR=DOB=20230401&T=1680338536000&POEX=W; ANON=A=3384BF297D47A3E09DAFAB27FFFFFFFF&E=1c2a&W=1; NAP=V=1.9&E=1bd0&C=gCpe7J00wpXqTBFVL49KckCPVqHljKmFH6LX5O5dd0aU5iW59zMsLg&W=1; PPLState=1; KievRPSSecAuth=FABqBBRaTOJILtFsMkpLVWSG6AN6C/svRwNmAAAEgAAACOB/RQwWNQ/nKAT231aqu6gbTev1qhjCHzshf7D61cAobpMe+tdy7I8GBZinAYMS+bj9mHjAGvT7uTRbh1TD32IVDohyJElA431RENKZhejSxsc/D4DTeupmOXLtKYmNa7x24FhQzMhhYau0tmzZRtwTgzKa3GHlt+++yzQjRIcLge0jW8jHCVdCUSEWXsg9VMt0GBTYktV/0pzQv95luombuy4Zm3BWrQMnZSs2tvuBEV0kkwdMbhCjJVpllQWABSdKXuSkizzYXKUDJ6pU41m9BN3fbaECh9w83X/36Rq0q+THJy0PmTH2VkrkgyrTqX2HIIYpEuSFurLDS/SWKKaGd9ce+rT4Vf+qARTgGnEBQ63va20C8KQBKGYvQSUb+PBr2lszkMCumBDlWV6jvIbWIFx+VO6QnpUZWPbsCyd07jTH9oPCvncMCXI+SrvLCQvh1GK2mwiA3iza0CWDI4GbMI7jBF0CHCUkGvdbqcgNkulMqq0cXvA4am9zUFnUMcRjMwl1KocINvJxutxD3/8NqZMgdPnBHM31KccsvJ7nl+qc3g9lL+hTF500Z8pyaehn0nO3AFOT/LV5Xse+jvvvEdUjcDVUSbvlXSNJANga+U83O0NuxWWk8u49yvprRtnqlDn4vVIyS3odrAUKEw+zxABldPhCPNNv36LjE3D8UMqRt5KylZJjoNnM5WnyIDirTznz7jywWtgBTjdh2UnWHy0dsuwUdf/zNSkbH4RqwJXhrMGmjp/5j2vpfVafjW94r4mY6Vpmo40Rt1vZ8gkwCSHewxPtm/rhBCz7GP3Tfz2y7dVziZllgU91DaCVUcO8wz8606U4Ke+CkMZ3fMPrEeNCPL6zl6NEER5cgR5mhB5Uj0ZD6sP7opXMBLnF74yk1a8L5BRltGo5/AlLFY9GeqRm/2p6vzdIzSwYKzp62RVBxCGJDDfEB76va5RABBsiJeseNj1dEnWzhuWwmlzIhf35EqxUd5Sfu0lkl4jVgnqRAqgqaT+tsHhOX9+QcGDqrHZpXiB5thSo+Z8Ybkes8lzE94mtxTl8aCWNoEL6xHhMc0+LrJw0q4oeCnNZ5LkRfHm9tx6LVUnLEVRDEcPWw7QSUiRfiTc+8S882xi84bEpj/r4UcD3HMPtNUglZSOnE9gexRBctGCZ23PFNn9CgE4xJwdmihXsxJn0jTfkR3/ZACZEGGnQWY0CjfP1WGmAgBix1+hORBFwueJ4a6dZD73nDhdWegvEmHOOdtfl0+MVdZsXAOBkgj+QaQESM/qYQPmfvntOLnVNlzOPNhoUmqTK1iFcxY2limPDZHlwsFG0TB7a7Am29aimXkUpH019CG5OUFPlzeH/FZLSuXtXH1cnCy/0DXiwzVoiKByY5Df/n8zCus/nLQX6ZxmSilCQz0AxQ4NsEzHE05gbcTmRBxQAJyw6e0A+cV+fJ4oWsLRpKGJEwL0=; _U=1tUtFEqrpwZFNq8DIXv8IpoboLDtV5VjDD6TJt1oXzuZugYF-mV_zr-Cpz3UOjzCBTIitd-jEwuoHpSfyx_UHlx_SGomYZLxwB2ZMx8L4iCoPb9FL-KDs9I5fYcrxrsQr7SusE04K4EW8Mcri7vEzYpIA0hRbxRbLzGuh3JYhRB_wHODaVu-Aeok_ra8i00F1k9fG6Ag9izbHHBEv-EVqww; WLS=C=91720160502ec7db&N=Arjun; WLID=fOmgUpdfsRelAlMrGyQgYJd4FRcp+8fLPd/TmEysH9856Us6BnxADILMLdtLltC7WQj9+PnUNVJb5oQNiMlfUiK1XaL9thiDXiTPCFEambY=; SUID=A; MSCC=NR; _clck=cfb03l|1|fae|1; ABDEF=V=13&ABDV=11&MRNB=1680339878666&MRB=0; _EDGE_S=F=1&SID=2D2FC630BD3B6141254AD4D6BC9D60B8&mkt=en-us&ui=en-us; USRLOC=HS=1&ELOC=LAT=9.959205627441406|LON=76.25028991699219|N=Kochi%2C%20Kerala|ELT=1|; ANIMIA=FRE=1; dsc=order=ShopOrderDefault; _uetsid=4dece370d06a11ed84f53ba3115856ab; _uetvid=4ded4040d06a11eda63e4fde898f1788; _clsk=1jbeb4l|1680340834931|37|1|r.clarity.ms/collect; _SS=SID=2D2FC630BD3B6141254AD4D6BC9D60B8&R=892&RB=892&GB=0&RG=0&RP=892&OCID=ML2DSU&BTQID=-&BTSTKey=-&RA=-&BTOID=-&BTQN=-&BTEC=-&BTMC=-&BTCQC=-&BTIOM=-&BTCO=-&BTRACI=-&BTTC=-; _HPVN=CS=eyJQbiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MSwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyMy0wNC0wMVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIkRmdCI6bnVsbCwiTXZzIjowLCJGbHQiOjAsIkltcCI6MjJ9; ai_session=cBhBRyTU/B/RnTtkc2T9jf|1680338539509|1680340922328; SRCHHPGUSR=SRCHLANG=en&DM=0&PV=11&BRW=MW&BRH=MT&CW=394&CH=851&SCW=394&SCH=851&DPR=2.8&UTC=330&WTS=63815935336&HV=1680340923&PRVCW=768&PRVCH=1662&EXLTT=25; _RwBf=ilt=1&ihpd=1&ispd=0&rc=892&rb=892&gb=0&rg=0&pc=892&mtu=0&mte=0&rbb=0.0&g=0&cid=&clo=0&v=45&l=2023-04-01T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&o=16&p=BINGTRIAL5TO250P201808&c=MY00IA&t=5189&s=2023-04-01T08:43:45.5381828+00:00&ts=2023-04-01T09:22:02.5026212+00:00&rwred=0&wls=2&lka=0&lkt=0&TH=&mta=0&e=1kxyramreO3M6V9FwHTmxOCAPx42dgFSjjY5Mmk68AzRdLLtvZy4BlaqaglIqZORL7_zopA7DyVTPFAHxiPUHw&A=3384BF297D47A3E09DAFAB27FFFFFFFF; SRCHHPGUSR=SRCHLANG=en&BRW=XW&BRH=M&CW=1536&CH=758&SCW=1519&SCH=3682&DPR=1.3&UTC=330&DM=1&WTS=63815849103&HV=1680252946&PRVCW=1536&PRVCH=758&PV=11; MUIDB=3691EDCB2A10670626D1FF2D2BB66610',
  'referer': 'https://www.bing.com/?toWww=1&redig=60CC44C30804490CBAAD44357FA3A171',
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
conn.request("GET", "/search?q=fu6787jsdksjdksn&form=QBLH&sp=-1&lq=0&pq=fun&sc=10-3&qs=n&sk=&cvid=0A19B1D7681C473C816E73BE0BEC05EB&ghsh=0&ghacc=0&ghpl=", payload, headers)
res = conn.getresponse()
print(res.status)