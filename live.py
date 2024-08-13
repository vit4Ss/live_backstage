import json

import requests
import httpx

url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=Kd_0z8YwaIL6-sXhT3KVUFZa8pDvP5rndnLWy9zL-p29Ggr_PVNrrzGxr5PGwNPM_6vXeXpfbgyN4XzZguT7L2mtzn3kliA8b_v1GDfr2oBHu6AZl71zK22y485xG0c3NJMpzQ==&X-Bogus=DFSzswVLbjqE/Ozatvy9TbJ92UIL&_signature=_02B4Z6wo00001ZaIghQAAIDDkSK3sJzSADmWiIaAAAMM1e"

resUrl = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=uYp8e9aCxZ-Ix-mD80aQmGhucDU5YPtsAngV5YXtrLoefoLY--V1tQ0b4C-TEsiJjGT0vI-B0Oo2tHVFip0aL34hL4ob_oa6SGdTB8ImcojFoNUNP5cCIapByRLlVhZdF4X3uw==&X-Bogus=DFSzswVL8jPxukGEtv8d3hJ92U17&_signature=_02B4Z6wo00001wTLrjAAAIDBA2GblSlMKScEy6qAAKefb9"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "__tea_cache_tokens_3178={%22_type_%22:%22default%22}; passport_csrf_token=e0ec4ec39115d04b4e567fb42daa509a; passport_csrf_token_default=e0ec4ec39115d04b4e567fb42daa509a; d_ticket_backstage=123f7a96d9cba27fce2fa3b25a458db77c8a3; s_v_web_id=verify_lz83q890_GdWqRDlS_4PO5_4ztR_88p9_bv7hD3SDApVr; csrf_session_id=a2c398ae990395885e7dd9bdca653d45; passport_fe_beating_status=true; _ttp=2k0Cqv4C95oUYbNdYVpTUuefvGi; odin_tt=4fa16888f53f0c0cc1073e4c50ccd5da7bc6c11bf0f22ff3a98507bf0e668d7b5f794d7f9d9707ee56c82f3e2c8bf8c636018ba1b032ac4f3f767f12c461c4b3; sid_guard_backstage=bd95ccab08f381de6a9d6710a5afaf82%7C1722411305%7C5184000%7CSun%2C+29-Sep-2024+07%3A35%3A05+GMT; uid_tt_backstage=96dc2853a4aeae5816d926534b20f4f8ac678a354cf2291c0d7de2e12c94cb70; uid_tt_ss_backstage=96dc2853a4aeae5816d926534b20f4f8ac678a354cf2291c0d7de2e12c94cb70; sid_tt_backstage=bd95ccab08f381de6a9d6710a5afaf82; sessionid_backstage=bd95ccab08f381de6a9d6710a5afaf82; sessionid_ss_backstage=bd95ccab08f381de6a9d6710a5afaf82; sid_ucp_v1_backstage=1.0.0-KDY3MTQ5NWIyOTIxNDU1ZmU3NGM0Y2UyNmY3NWRjZWVlMDVjYTk4MDUKIAiBiMKG7t2xymYQqdKntQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgYmQ5NWNjYWIwOGYzODFkZTZhOWQ2NzEwYTVhZmFmODI; ssid_ucp_v1_backstage=1.0.0-KDY3MTQ5NWIyOTIxNDU1ZmU3NGM0Y2UyNmY3NWRjZWVlMDVjYTk4MDUKIAiBiMKG7t2xymYQqdKntQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgYmQ5NWNjYWIwOGYzODFkZTZhOWQ2NzEwYTVhZmFmODI; ttwid=1%7CHvRhfCmxMfk8Hv56ba07PjMzvYWW7eWqxmoSJI87ZhI%7C1722413687%7Cdc1bbe8bba70a315e7fb8966e1c4db3662ba9145e979391f9e83ddbee236ac8d; msToken=Kd_0z8YwaIL6-sXhT3KVUFZa8pDvP5rndnLWy9zL-p29Ggr_PVNrrzGxr5PGwNPM_6vXeXpfbgyN4XzZguT7L2mtzn3kliA8b_v1GDfr2oBHu6AZl71zK22y485xG0c3NJMpzQ==; msToken=Kd_0z8YwaIL6-sXhT3KVUFZa8pDvP5rndnLWy9zL-p29Ggr_PVNrrzGxr5PGwNPM_6vXeXpfbgyN4XzZguT7L2mtzn3kliA8b_v1GDfr2oBHu6AZl71zK22y485xG0c3NJMpzQ==",
    "faction-id": "103608",
    "origin": "https://live-backstage.tiktok.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://live-backstage.tiktok.com/portal/",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "'Windows'",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-appid": "1180",
    "x-csrf-token": "undefined",
    "x-language": "zh-CN",
    "x-secsdk-csrf-token": "000100000001d8e91aafb0bc694274492e3205e2ec88709b05ad2522fef2ec7127dfd148baca17e73e1fa5fa910f",
}

data = {"DisplayIDList": ["youten517", "gotohkikuchi.510", "ruukun001", "ntk__kurusu", "sinsin0523", "uta_usagi",
                          "nanachan08082", "yuyuzaw200", "princessyurichama"]}

# with open('tiktok_XBogus.js', 'r', encoding="utf-8") as f:
#     code = f.read()
# ctx = execjs.compile(code,"node_modules")
# res_url = ctx.call("get_post_url", url, data, headers['referer'])
# print(res_url)

# print(url)
#
# response = requests.post(url, headers=headers, json=data)
#
# print(response.text)
get_url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/quota/get_broker_remain_quota/?AgencyID=103608&OperatorID=7391751617698104321&msToken=XcR0ELo_8hIp3rnBhNN4OMCU8K5Kcx_HOJN8xAFYU551kfBm4Vusmjkn-gxYYx0gHGQxyYvN1FoXvcYOrwOgz0u8LyOhykGTWF4bYPMwLiU=&X-Bogus=DFSzswVLnUKdUvGEtv0rchJ92U6q&_signature=_02B4Z6wo00001h3p0vAAAIDAGkPnVYlZq-Id6dZAAOHr7d"
with httpx.Client(http2=True, verify=False, ) as client:
    # , cookies = cookies
    response = client.post(url, headers=headers, json=data)
    # print(response.json())
    print(response.text)
