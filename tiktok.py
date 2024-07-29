import execjs
import requests
import httpx
import json

url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=J3RWabcbegNghkCL0YXAo6tXXCKro32Zt-eNG0cSewq1PvY0B_mEMJ9drWNavZDvaFbgmNv2XaL9QM60vyB9CinSBl5Qg35hfoZzhrUXsxuHK4P8Yll-0ILkWRF-9kXpPMT3Rg=="


headers = {
    'content-Type': "application/json; charset=utf-8;",
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': '__tea_cache_tokens_3178={%22_type_%22:%22default%22}; passport_csrf_token=a3a5072f70c952afb74a65370cb8d292; passport_csrf_token_default=a3a5072f70c952afb74a65370cb8d292; d_ticket_backstage=962754c0711e1769f1fb9d7f934705ae8eb36; _ttp=2jZaYKbCeLJ8x0QFD0wBH2QDIBw; msToken=J3RWabcbegNghkCL0YXAo6tXXCKro32Zt-eNG0cSewq1PvY0B_mEMJ9drWNavZDvaFbgmNv2XaL9QM60vyB9CinSBl5Qg35hfoZzhrUXsxuHK4P8Yll-0ILkWRF-9kXpPMT3Rg==; odin_tt=b04557a993d4eb07f6ffb1f615cec2962b865a6b33eb222beec5b596c2f2cdf3a6fd4bfcdad43e1392f0dc94487463e66654a2b87314756f34e68bdb360ab6c7; sid_guard_backstage=486d58be32dacc56f647ca6affb5b1c0%7C1721927901%7C5184000%7CMon%2C+23-Sep-2024+17%3A18%3A21+GMT; uid_tt_backstage=b602219e4acd5b7f85bfc8bddacd461870e62e35ddab12cbb0dc5b4640e790bb; uid_tt_ss_backstage=b602219e4acd5b7f85bfc8bddacd461870e62e35ddab12cbb0dc5b4640e790bb; sid_tt_backstage=486d58be32dacc56f647ca6affb5b1c0; sessionid_backstage=486d58be32dacc56f647ca6affb5b1c0; sessionid_ss_backstage=486d58be32dacc56f647ca6affb5b1c0; sid_ucp_v1_backstage=1.0.0-KGZiNWJhZTQ5YmZiNmEyNGM0NmQ0MDgwMzdhMjAwMzM2ZTM2ZGM5ZTMKIAiBiMKG7t2xymYQ3ZGKtQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgNDg2ZDU4YmUzMmRhY2M1NmY2NDdjYTZhZmZiNWIxYzA; ssid_ucp_v1_backstage=1.0.0-KGZiNWJhZTQ5YmZiNmEyNGM0NmQ0MDgwMzdhMjAwMzM2ZTM2ZGM5ZTMKIAiBiMKG7t2xymYQ3ZGKtQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgNDg2ZDU4YmUzMmRhY2M1NmY2NDdjYTZhZmZiNWIxYzA; msToken=oC9dSGZd0U8o_sZubkSgP0eYjwQOhdL5pqA-ZyAFv3KQUQX75rLBeXKMRXCZqhu-hId8JgEeHlqeUjvwZIwQ_TiiSSOgXXmsRO4MqflwH_7sW95IaLXAu-3I8jA0s-2ymc2CnA==; csrf_session_id=d797ada0064e3c0314c99149bd08db61; s_v_web_id=verify_lz5ds0e5_HWlcorKw_Kiei_4E1k_AoaL_B45HZ7Gf9yE3; ttwid=1%7CEtIW8sJlCrayXGfl9JddmuguewpHzd5huKgi4PLaYMI%7C1722191439%7C09872c7cddd4a0bd80a3a208abfa5fbd567dcf5d64110110df4dde5f06dac4b9; passport_fe_beating_status=true',
    'faction-id': '103608',
    'origin': 'https://live-backstage.tiktok.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://live-backstage.tiktok.com/portal/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-appid': '1180',
    'x-csrf-token': 'undefined',
    'x-language': 'zh-CN',
    'x-secsdk-csrf-token': '000100000001bfe563d5b53e4113489237e7c66932f4c7e9209fc99ef4b3d8a0bb3d49edf5db17e65abbeb1d81c6',
    "accept-encoding": "gzip, deflate, br, zstd",
    "Connection": "keep-alive",
}

data = {
    "DisplayIDList": ["newarnimaiya6", "kotemarurun", "user4853450601197", "itshkvcsgww", "yuuuuki_521", "bts124jin","hinata._.bochi"]
}

with open('tiktok_XBogus.js', 'r', encoding="utf-8") as f:
    code = f.read()
ctx = execjs.compile(code)
res_url = ctx.call("get_post_url", url, data, headers['referer'])
print(res_url)

with httpx.Client(http2=True, verify=False, ) as client:
    # , cookies = cookies
    response = client.post(res_url, headers=headers, json=data)
    print(response.text)
# print(response.text)
