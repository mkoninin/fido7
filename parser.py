# %%

# парсер списка тем

import json
import datetime    
import requests

def dl_group(date_after, date_before, echo_conf, big_param):


    data = f'f.req=%5B%5B%5B%22P14lVb%22%2C%22%5B%5C%22%5C%22%2C%5B%5Bnull%2Cnull%2Cnull%2C%5B%5C%22{date_after}%5C%22%5D%5D%2C%5Bnull%2Cnull%2C%5B%5C%22{date_before}%5C%22%5D%5D%5D%2C%5B%5B%5C%22{echo_conf}%40googlegroups.com%5C%22%5D%5D%2C%5C%22{big_param}%5C%22%2C30%2Cnull%2C1%5D%22%2Cnull%2C%221%22%5D%2C%5B%22C2aDwd%22%2C%22%5B%5C%22{echo_conf}%40googlegroups.com%5C%22%2Cnull%2C%5B3%5D%5D%22%2Cnull%2C%2211%22%5D%5D%5D'

    headers = {
        'authority': 'groups.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
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
        # 'rpcids': 'P14lVb,C2aDwd',
        'source-path': f'/g/{echo_conf}/search',
        # 'f.sid': '-2346844013451334959',
        # 'bl': 'boq_groupsfrontendserver_20240122.04_p1',
        # 'hl': 'en',
        # 'soc-app': '696',
        # 'soc-platform': '1',
        # 'soc-device': '1',
        # '_reqid': '764529',
        # 'rt': 'c',
    }

    response = requests.post(
        'https://groups.google.com/_/GroupsFrontendUi/data/batchexecute',
        params=params,
        # cookies=cookies,
        headers=headers,
        data=data,
    )
    print(len(response.text))

    return(response)



# %%

big_param = ''
big_param2 = ''

date_after = '1997-03-26'
date_before = '2023-03-27'
echo_conf = 'fido7.nsk.general'

i = 0

with open(f'{echo_conf}.txt', 'a') as fp:
    while(big_param == big_param2):
        i+=1
        print(i, datetime.datetime.now())
        response = dl_group(date_after, date_before, echo_conf, big_param)
        fp.write(response.text)
        data = []

        for i, txt in enumerate(response.text.splitlines()):
            try:
                data.append(json.loads(txt))
            except:
                # print(f'строка {i} плохая')
                pass
        big_param2 = json.loads(data[0][1][2])[-6]
        if big_param != big_param2:
            print('новый параметр')
            big_param = big_param2

# %%
