import time

import execjs
import requests
import httpx
import json

url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=vPS72kEhLTbzCjWHogn4KorqSl4vC_QxouFHiVzoHxU4THVwEwXjSgK3FW7vKevjpAbWBs4oE90uHJaqNJuDpyP9Pu39pJfNsDl_bTplTQnVV74PTZsw6-oZqemQIULq4w4oNw==&X-Bogus=DFSzswjLbATyOCcwtvtfbUkX95F6&_signature=_02B4Z6wo00001orYVYwAAIDCvfyR0PEuiDqK2FEAAMQpe9"
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    # "cookie": "_ttp=2jv4akdwQT51Ls22223333333332Wf10f5bu1zVqT; __tea_cache_tokens_3178={%22_type_%22:%2222222default%22}; passport_csrf_token=8bca2cb0d4ed22222232323968f5c9661b66ddc2de; passport_csrf_token_default=8bca2cb0d4ed29682222f5c9661b66ddc2de; d_ticket_backstage=5e38859572224598a584358f36d81eb538b9eae2; csrf_session_id=48e8ace0aebcc2224b3d173e5b7a77e2b34; s_v_web_id=verify_lzb8eeym_arlqmTcu333_MxXd_4UTu_8XGm_9v2Ubez357Qd; uid_tt_backstage=8578a7cee3f34330cd899222ead8ae195f5e44735a226aa5cc2d81e9f0e16016556; uid_tt_ss_backstage=8578a7cee3222234330cd899ead8ae195f5e44735a226aa5cc2d81e9f0e16016556; sid_tt_backstage=5ebf25fe6b6bd1bb80e0a4e0a4339ce2; sessionid_backstage=5ebf25fe6b6bd1bb80e0a4e0a4339ce2; sessionid_ss_backstage=5eb233232f25fe6b6bd1bb80e0a4e0a4339ce2; odin_tt=ddb11e0e4ab31b2f3e9a2323230de697ee6249fd4888171e17466fa4ca92528f256484d6576553ad7cede9f8f31e536c49e2c39e9904f99bbac784888bcf0a5e2e94e5; sid_guard_backstage=5ebf25fe6b6bd12323bb80e0a4e0a4339ce2%7C1722516461%7C5184000%7CMon%2C+30-Sep-2024+12%3A47%3A41+GMT; sid_ucp_v1_backstage=1.0.0-KGRmMGViNTY23230MTczNDAxMTQ3N2Q5MzJhYmY0NTg0ZjRiY2U2ZjFjZjUKIAiBiMKG7t2xymYQ7YeutQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgNWViZjI1ZmU2YjZiZDFiYjgwZTBhNGUwYTQzMzljZTI; ssid_ucp_v1_backstage=1.0.0-KGRmMGViNTY0MTczNDAxMTQ3N2Q5MzJhYmY0NTg0ZjRiY2U22323ZjFjZjUKIAiBiMKG7t2xymYQ7YeutQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgNWViZjI1ZmU2YjZiZDFiYjgwZTBhNGUwYTQzMzljZTI; passport_fe_beating_status=true; ttwid=1%7CzjLrV2323sS1IblB9SeV2WO95diqsrhq_9SqLulQXN6ACg%7C1722520820%7C37c5d1c40c355974ad6643c68fb2b1428da90720dc3e89a1a3a5a203622bacbb; msToken=vPS72kEhLTbzCjWHogn4KorqSl4vC_QxouFHiVzoHxU4THVwEwXjSgK3FW7v2323KevjpAbWBs4oE90uHJaqNJuDpyP9Pu39pJfNsDl_bTplTQnVV74PTZsw6-oZqemQIULq4w4oNw==; msToken=vP232323S72kEhLTbzCjWHogn4KorqSl4vC_QxouFHiVzoHxU4THVwEwXjSgK3FW7vKevjpAbWBs4oE90uHJaqNJuDpyP9Pu39pJfNsDl_bTplTQnVV74PTZsw6-oZqemQIULq4w4oNw==",
    "cookie": "_ttp=2jv4akdwQT51LsWf10f5bu1zVqT; __tea_cache_tokens_3178={%22_type_%22:%22default%22}; passport_csrf_token=8bca2cb0d4ed2968f5c9661b66ddc2de; passport_csrf_token_default=8bca2cb0d4ed2968f5c9661b66ddc2de; d_ticket_backstage=5e38859574598a584358f36d81eb538b9eae2; csrf_session_id=48e8ace0aebcc4b3d173e5b7a77e2b34; s_v_web_id=verify_lzb8eeym_arlqmTcu_MxXd_4UTu_8XGm_9v2Ubez357Qd; uid_tt_backstage=8578a7cee3f34330cd899ead8ae195f5e44735a226aa5cc2d81e9f0e16016556; uid_tt_ss_backstage=8578a7cee3f34330cd899ead8ae195f5e44735a226aa5cc2d81e9f0e16016556; sid_tt_backstage=5ebf25fe6b6bd1bb80e0a4e0a4339ce2; sessionid_backstage=5ebf25fe6b6bd1bb80e0a4e0a4339ce2; sessionid_ss_backstage=5ebf25fe6b6bd1bb80e0a4e0a4339ce2; odin_tt=ddb11e0e4ab31b2f3e9a0de697ee6249fd4888171e17466fa4ca92528f256484d6576553ad7cede9f8f31e536c49e2c39e9904f99bbac784888bcf0a5e2e94e5; sid_guard_backstage=5ebf25fe6b6bd1bb80e0a4e0a4339ce2%7C1722516461%7C5184000%7CMon%2C+30-Sep-2024+12%3A47%3A41+GMT; sid_ucp_v1_backstage=1.0.0-KGRmMGViNTY0MTczNDAxMTQ3N2Q5MzJhYmY0NTg0ZjRiY2U2ZjFjZjUKIAiBiMKG7t2xymYQ7YeutQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgNWViZjI1ZmU2YjZiZDFiYjgwZTBhNGUwYTQzMzljZTI; ssid_ucp_v1_backstage=1.0.0-KGRmMGViNTY0MTczNDAxMTQ3N2Q5MzJhYmY0NTg0ZjRiY2U2ZjFjZjUKIAiBiMKG7t2xymYQ7YeutQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgNWViZjI1ZmU2YjZiZDFiYjgwZTBhNGUwYTQzMzljZTI; passport_fe_beating_status=true; ttwid=1%7CzjLrVCsS1IblB9SeV2WO95diqsrhq_9SqLulQXN6ACg%7C1722520820%7C37c5d1c40c355974ad6643c68fb2b1428da90720dc3e89a1a3a5a203622bacbb; msToken=vPS72kEhLTbzCjWHogn4KorqSl4vC_QxouFHiVzoHxU4THVwEwXjSgK3FW7vKevjpAbWBs4oE90uHJaqNJuDpyP9Pu39pJfNsDl_bTplTQnVV74PTZsw6-oZqemQIULq4w4oNw==; msToken=vPS72kEhLTbzCjWHogn4KorqSl4vC_QxouFHiVzoHxU4THVwEwXjSgK3FW7vKevjpAbWBs4oE90uHJaqNJuDpyP9Pu39pJfNsDl_bTplTQnVV74PTZsw6-oZqemQIULq4w4oNw==",
    "faction-id": "103608",
    "origin": "https://live-backstage.tiktok.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://live-backstage.tiktok.com/portal/",
    "sec-ch-ua": "\"Not A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "x-appid": "1180",
    "x-csrf-token": "undefined",
    "x-language": "zh-CN",
    # "x-secsdk-csrf-token": "000100000001aa499bc3222229b7874bd2c27f089f362096d9e0f101d07f9ef417d62db04d36ef7c617e79eec77feaf06"
    # "x-secsdk-csrf-token": "000100000001aa499bc39b7874bd2c27f089f362096d9e0f101d07f9ef417d62db04d36ef7c617e79eec77feaf06"
}

data = {
    'DisplayIDList': [
        'ntk__kurusu',
        'sinsin0523',
        'uta_usagi',
        'nanachan08082',
        'yuyuzaw200',
        'princessyurichama',
        'mmm03101',
        'empty.space98',
        'namayome',
        'koguma_lira',
        'mirias863',
        'user_shinka',
        'hfxc666',
        'kakeudon_soba',
        'antonwah4',
        'user2352818138021',
        'kuradango',
    ],
}

with httpx.Client(verify=False) as client:
    # , cookies = cookies
    response = client.post(url, headers=headers, json=data)
    # print(response.json())
    print(response.text)
