import httpx
import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': '__tea_cache_tokens_3178={%22_type_%22:%22default%22}; passport_csrf_token=e0ec4ec39115d04b4e567fb42daa509a; passport_csrf_token_default=e0ec4ec39115d04b4e567fb42daa509a; d_ticket_backstage=123f7a96d9cba27fce2fa3b25a458db77c8a3; s_v_web_id=verify_lz83q890_GdWqRDlS_4PO5_4ztR_88p9_bv7hD3SDApVr; csrf_session_id=a2c398ae990395885e7dd9bdca653d45; passport_fe_beating_status=true; _ttp=2k0Cqv4C95oUYbNdYVpTUuefvGi; odin_tt=4fa16888f53f0c0cc1073e4c50ccd5da7bc6c11bf0f22ff3a98507bf0e668d7b5f794d7f9d9707ee56c82f3e2c8bf8c636018ba1b032ac4f3f767f12c461c4b3; sid_guard_backstage=bd95ccab08f381de6a9d6710a5afaf82%7C1722411305%7C5184000%7CSun%2C+29-Sep-2024+07%3A35%3A05+GMT; uid_tt_backstage=96dc2853a4aeae5816d926534b20f4f8ac678a354cf2291c0d7de2e12c94cb70; uid_tt_ss_backstage=96dc2853a4aeae5816d926534b20f4f8ac678a354cf2291c0d7de2e12c94cb70; sid_tt_backstage=bd95ccab08f381de6a9d6710a5afaf82; sessionid_backstage=bd95ccab08f381de6a9d6710a5afaf82; sessionid_ss_backstage=bd95ccab08f381de6a9d6710a5afaf82; sid_ucp_v1_backstage=1.0.0-KDY3MTQ5NWIyOTIxNDU1ZmU3NGM0Y2UyNmY3NWRjZWVlMDVjYTk4MDUKIAiBiMKG7t2xymYQqdKntQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgYmQ5NWNjYWIwOGYzODFkZTZhOWQ2NzEwYTVhZmFmODI; ssid_ucp_v1_backstage=1.0.0-KDY3MTQ5NWIyOTIxNDU1ZmU3NGM0Y2UyNmY3NWRjZWVlMDVjYTk4MDUKIAiBiMKG7t2xymYQqdKntQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgYmQ5NWNjYWIwOGYzODFkZTZhOWQ2NzEwYTVhZmFmODI; ttwid=1%7CHvRhfCmxMfk8Hv56ba07PjMzvYWW7eWqxmoSJI87ZhI%7C1722411337%7C337ec4cff312a7dcc0fc0c5e199daa1d9529dd0d95b34ab7879732778f27980c; msToken=ARJmN9iUBY6YMAbuTfoB-5eSZVXUugvUo_0WlyKnDDDoIGjtc8KNy6iKeoiMbOyDUCt85HAIl_rs-ODuI2J1I_yEQ-0Bp-6NNqagoh9JcdVJN_P7I-2oa9oHfl07cPgHSeKlzw==; msToken=ARJmN9iUBY6YMAbuTfoB-5eSZVXUugvUo_0WlyKnDDDoIGjtc8KNy6iKeoiMbOyDUCt85HAIl_rs-ODuI2J1I_yEQ-0Bp-6NNqagoh9JcdVJN_P7I-2oa9oHfl07cPgHSeKlzw==',
    'faction-id': '103608',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://live-backstage.tiktok.com/portal/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'x-appid': '1180',
    'x-csrf-token': 'undefined',
    'x-language': 'zh-CN',
}


url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/platform_account/check_user_sessions/?msToken=ARJmN9iUBY6YMAbuTfoB-5eSZVXUugvUo_0WlyKnDDDoIGjtc8KNy6iKeoiMbOyDUCt85HAIl_rs-ODuI2J1I_yEQ-0Bp-6NNqagoh9JcdVJN_P7I-2oa9oHfl07cPgHSeKlzw==&X-Bogus=DFSzswjLmURdUUxjtvyzdXJ92U6r&_signature=_02B4Z6wo00001-iM6MgAAIDB7ybdbs7Ao2.ojOxAAJyUf4"


def check_user_sessions():
    with httpx.Client(verify=False) as client:
        # , cookies = cookies
        response = client.get(url, headers=headers)
        # print(response.json())
        return response.json()
