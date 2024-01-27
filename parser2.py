# %%
import requests

# cookies = {
#     '__Secure-ENID': '16.SE=lGW-uD29t38erBwBFbqrtpZb8viwLUguEndGHTvPdD1wcww4EjZmM4Oz27v6KnibeJPyMpoYiOrom5xtoxb1M5KjM9Vz_nuz70ymTuSKXWLroUHRfzbRI9fMomjv_c9hTBm6H6TK-ZJ_jIMR0tKDyf3frqXhEcnfq3Rmre3NjdWVR4E97Zcdud-o9PHQ0LbRFV1Jh_JRkQYiCICyFbDPBK5WcSMohVXE5aHAjp9qCd49G1qBG791g5j6OKfSF2LJ3bt7O0ufA4HRXA2pUIy879fLiY0fXGfnFWD0OeR5',
#     'S': 'billing-ui-v3=Cy-3nWmpyAZwCUcBRHtil18FwZQj68Hs:billing-ui-v3-efe=Cy-3nWmpyAZwCUcBRHtil18FwZQj68Hs',
#     'SID': 'fQhPiDjFgjK3ha1Dp8I_XvSoPcKFQ621CyBAlgq4cVivkzAPLIMXfLwUUMKcOxqSUgEq5w.',
#     '__Secure-1PSID': 'fQhPiDjFgjK3ha1Dp8I_XvSoPcKFQ621CyBAlgq4cVivkzAPRT1JWO4hWEU7YlKPU2pJPQ.',
#     '__Secure-3PSID': 'fQhPiDjFgjK3ha1Dp8I_XvSoPcKFQ621CyBAlgq4cVivkzAPRZpYihukB8h8is_uoS2QTg.',
#     'HSID': 'Avvfiy0c3fVH61sm6',
#     'SSID': 'ABt75-9YvTmMyA7s4',
#     'APISID': '60upLz5RyJi7EH9U/A4ovYX_v44dAl4Zek',
#     'SAPISID': 'KtLt_AdA6LodNleJ/A3RbRcgPxKoaoDTQJ',
#     '__Secure-1PAPISID': 'KtLt_AdA6LodNleJ/A3RbRcgPxKoaoDTQJ',
#     '__Secure-3PAPISID': 'KtLt_AdA6LodNleJ/A3RbRcgPxKoaoDTQJ',
#     'SEARCH_SAMESITE': 'CgQImpoB',
#     'OGP': '-19026792:-19015941:-19010599:',
#     'OGPC': '19008535-3:19026792-2:19015941-5:19010599-5:19026797-1:',
#     'OSID': 'fwhPiHnpyvFw3ovchAfT5tbjL04kGRGJXNWZvo4P_pQJX9TVMsTvhOKWT3nIabWJA64n2w.',
#     '__Secure-OSID': 'fwhPiHnpyvFw3ovchAfT5tbjL04kGRGJXNWZvo4P_pQJX9TVBEVZaNj2vTYqHgv-yhnrXg.',
#     'OTZ': '7400629_28_32_123600_28_436080',
#     'AEC': 'Ae3NU9Pfh0pa5-85nT9c0YMRfGK83UgskFvI7yo5t1Yoi47sp5bckmYqHw',
#     '1P_JAR': '2024-01-27-13',
#     'NID': '511=ZmWAfW6DZcszFMgIfzXLnk6-oq15XY9oYPIpg1J8zPdNcRC28NrtLjRXGGY1Il6K9v8kfLLuS9DrhGUV_L5xOGQ_FZ5SMmlGuwmHSMDWSAvjfpcw6xqqaClwZPeT3i4eTg_FSSVhi4mdR-_XuvkAYiKx8rWwuI90rvoi1ZiZqaB4y355ynAz47Bghm0GrEz6Vukl8V5Hj5xHrDRKhAqgWS4hBXXjQIG6R8ox_rBs8_YFdMvMfXzEN6_RblWFMFyawZZdJ5afiBPW0_6mshZJIFQaXz5uELwMkzoM6Ny5bNkEgOAnBKXpUCr8edP9KsyexAntzcQLGyWj6iyX8zRvCTdmK8ZxtPS19PaMtjdSJyvZloGudHYZcjHa9sPXWfWo0EbyU1GPJh4uumKahOngAM4UWMjsCox7DZDHf4FVSO_d6xKG76iwac53_4-ZiG5z8TLH3G5u0RQjWlHTM5OrZ7O0tZg',
#     '__Secure-1PSIDTS': 'sidts-CjIBPVxjSh2J9R1KCVIUBWyeoiWbyYYgJeNCXaS3NXANgzUqQleCgr452cjz1ZfM-d3plhAA',
#     '__Secure-3PSIDTS': 'sidts-CjIBPVxjSh2J9R1KCVIUBWyeoiWbyYYgJeNCXaS3NXANgzUqQleCgr452cjz1ZfM-d3plhAA',
#     'SIDCC': 'ABTWhQHyXs41PIykj1662wX85Rybg_OLaVRdslmCwd9qtyTabBVdvSdSeYHLR8QY04imfCyNTQ',
#     '__Secure-1PSIDCC': 'ABTWhQF19diTpQXGj2M75FxAu3X_UhOPHs_nBIEL_13fFSwu9rbZhe-rXGYPUPP4hYEPsczJ-sE',
#     '__Secure-3PSIDCC': 'ABTWhQGUNG4mh46EoRbqReB96V5GAXDyj3XwfGH1TDBUOt8BpLHqNpSlUc4ak1r7af6DCksIw_Sq',
# }

headers = {
    'authority': 'groups.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': '__Secure-ENID=16.SE=lGW-uD29t38erBwBFbqrtpZb8viwLUguEndGHTvPdD1wcww4EjZmM4Oz27v6KnibeJPyMpoYiOrom5xtoxb1M5KjM9Vz_nuz70ymTuSKXWLroUHRfzbRI9fMomjv_c9hTBm6H6TK-ZJ_jIMR0tKDyf3frqXhEcnfq3Rmre3NjdWVR4E97Zcdud-o9PHQ0LbRFV1Jh_JRkQYiCICyFbDPBK5WcSMohVXE5aHAjp9qCd49G1qBG791g5j6OKfSF2LJ3bt7O0ufA4HRXA2pUIy879fLiY0fXGfnFWD0OeR5; S=billing-ui-v3=Cy-3nWmpyAZwCUcBRHtil18FwZQj68Hs:billing-ui-v3-efe=Cy-3nWmpyAZwCUcBRHtil18FwZQj68Hs; SID=fQhPiDjFgjK3ha1Dp8I_XvSoPcKFQ621CyBAlgq4cVivkzAPLIMXfLwUUMKcOxqSUgEq5w.; __Secure-1PSID=fQhPiDjFgjK3ha1Dp8I_XvSoPcKFQ621CyBAlgq4cVivkzAPRT1JWO4hWEU7YlKPU2pJPQ.; __Secure-3PSID=fQhPiDjFgjK3ha1Dp8I_XvSoPcKFQ621CyBAlgq4cVivkzAPRZpYihukB8h8is_uoS2QTg.; HSID=Avvfiy0c3fVH61sm6; SSID=ABt75-9YvTmMyA7s4; APISID=60upLz5RyJi7EH9U/A4ovYX_v44dAl4Zek; SAPISID=KtLt_AdA6LodNleJ/A3RbRcgPxKoaoDTQJ; __Secure-1PAPISID=KtLt_AdA6LodNleJ/A3RbRcgPxKoaoDTQJ; __Secure-3PAPISID=KtLt_AdA6LodNleJ/A3RbRcgPxKoaoDTQJ; SEARCH_SAMESITE=CgQImpoB; OGP=-19026792:-19015941:-19010599:; OGPC=19008535-3:19026792-2:19015941-5:19010599-5:19026797-1:; OSID=fwhPiHnpyvFw3ovchAfT5tbjL04kGRGJXNWZvo4P_pQJX9TVMsTvhOKWT3nIabWJA64n2w.; __Secure-OSID=fwhPiHnpyvFw3ovchAfT5tbjL04kGRGJXNWZvo4P_pQJX9TVBEVZaNj2vTYqHgv-yhnrXg.; OTZ=7400629_28_32_123600_28_436080; AEC=Ae3NU9Pfh0pa5-85nT9c0YMRfGK83UgskFvI7yo5t1Yoi47sp5bckmYqHw; 1P_JAR=2024-01-27-13; NID=511=ZmWAfW6DZcszFMgIfzXLnk6-oq15XY9oYPIpg1J8zPdNcRC28NrtLjRXGGY1Il6K9v8kfLLuS9DrhGUV_L5xOGQ_FZ5SMmlGuwmHSMDWSAvjfpcw6xqqaClwZPeT3i4eTg_FSSVhi4mdR-_XuvkAYiKx8rWwuI90rvoi1ZiZqaB4y355ynAz47Bghm0GrEz6Vukl8V5Hj5xHrDRKhAqgWS4hBXXjQIG6R8ox_rBs8_YFdMvMfXzEN6_RblWFMFyawZZdJ5afiBPW0_6mshZJIFQaXz5uELwMkzoM6Ny5bNkEgOAnBKXpUCr8edP9KsyexAntzcQLGyWj6iyX8zRvCTdmK8ZxtPS19PaMtjdSJyvZloGudHYZcjHa9sPXWfWo0EbyU1GPJh4uumKahOngAM4UWMjsCox7DZDHf4FVSO_d6xKG76iwac53_4-ZiG5z8TLH3G5u0RQjWlHTM5OrZ7O0tZg; __Secure-1PSIDTS=sidts-CjIBPVxjSh2J9R1KCVIUBWyeoiWbyYYgJeNCXaS3NXANgzUqQleCgr452cjz1ZfM-d3plhAA; __Secure-3PSIDTS=sidts-CjIBPVxjSh2J9R1KCVIUBWyeoiWbyYYgJeNCXaS3NXANgzUqQleCgr452cjz1ZfM-d3plhAA; SIDCC=ABTWhQHyXs41PIykj1662wX85Rybg_OLaVRdslmCwd9qtyTabBVdvSdSeYHLR8QY04imfCyNTQ; __Secure-1PSIDCC=ABTWhQF19diTpQXGj2M75FxAu3X_UhOPHs_nBIEL_13fFSwu9rbZhe-rXGYPUPP4hYEPsczJ-sE; __Secure-3PSIDCC=ABTWhQGUNG4mh46EoRbqReB96V5GAXDyj3XwfGH1TDBUOt8BpLHqNpSlUc4ak1r7af6DCksIw_Sq',
    'origin': 'https://groups.google.com',
    'pragma': 'no-cache',
    'referer': 'https://groups.google.com/',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"122.0.2353.0"',
    'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6253.0", "Not(A:Brand";v="24.0.0.0", "Microsoft Edge";v="122.0.2353.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'x-same-domain': '1',
}

params = {
    # 'rpcids': 'UE3t1d,R7j1ae,KS4ZPe,Dq0xse,FEQDwf,C2aDwd',
    'source-path': '/g/fido7.sport.other',
    # 'f.sid': '-3078643617398008504',
    # 'bl': 'boq_groupsfrontendserver_20240122.04_p1',
    # 'hl': 'en',
    # 'soc-app': '696',
    # 'soc-platform': '1',
    # 'soc-device': '1',
    # '_reqid': '58170990',
    # 'rt': 'c',
}

data = 'f.req=%5B%5B%5B%22UE3t1d%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%5D%22%2Cnull%2C%221%22%5D%2C%5B%22R7j1ae%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%5D%22%2Cnull%2C%222%22%5D%2C%5B%22KS4ZPe%22%2C%22%5B%5Bnull%2C%5C%22fido7.sport.other%40googlegroups.com%5C%22%5D%5D%22%2Cnull%2C%224%22%5D%2C%5B%22Dq0xse%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%2C30%2C%5C%22%5C%22%2C%5B%5D%2C0%5D%22%2Cnull%2C%225%22%5D%2C%5B%22FEQDwf%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%5D%22%2Cnull%2C%229%22%5D%2C%5B%22C2aDwd%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%2Cnull%2C%5B3%5D%5D%22%2Cnull%2C%2215%22%5D%5D%5D&at=AAjqxmrugcoOsGlhMNhOZTSyb0zE%3A1706359382849&'
data = 'f.req=%5B%5B%5B%22Dq0xse%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%2C30%2C%5C%22CMzkwJHs%2FYMDEB4aGkBbgK2D1L%2BxykBXUESeVFzghoNKA0eGJWNH%5C%22%2C%5B%5D%2C0%5D%22%2Cnull%2C%224%22%5D%2C%5B%22C2aDwd%22%2C%22%5B%5C%22fido7.sport.other%40googlegroups.com%5C%22%2Cnull%2C%5B3%5D%5D%22%2Cnull%2C%2214%22%5D%5D%5D&at=AAjqxmrugcoOsGlhMNhOZTSyb0zE%3A1706359382849&'
response = requests.post(
    'https://groups.google.com/_/GroupsFrontendUi/data/batchexecute',
    params=params,
    # cookies=cookies,
    headers=headers,
    data=data,
)

print(len(response.text))
# %%
import json

def load_json(line):
    return json.loads(line)

data = []

for a in json.loads(response.text.splitlines()[2]):
    try:
        if (a[2] != None):
            data.append(a[2])
    except:
        pass

data.sort(key=len)
json.loads(data[-1])[2]

# %%
