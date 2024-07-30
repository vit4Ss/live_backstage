import json

import requests
import httpx

url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=J4GpvmINfaEpaX8mzuYaGapgAb8y2uFZ0wX4iTJ08rDBYDAhwsF4aZk8naq24X-U9BypEtQYNel0fr5GC81ccm1MIysQ5i62BbPu0U2WWCuHvv_48S-BwEKXjS2JnjwAWVjrHA==&X-Bogus=DFSzswVLXF-j8vGEtv0SDXJ92U18&_signature=_02B4Z6wo00001EeC6AAAAIDCQCjdpCRNlUBHguyAAHdOdd"

resUrl = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/union_invite/batch_check_anchor/?msToken=uYp8e9aCxZ-Ix-mD80aQmGhucDU5YPtsAngV5YXtrLoefoLY--V1tQ0b4C-TEsiJjGT0vI-B0Oo2tHVFip0aL34hL4ob_oa6SGdTB8ImcojFoNUNP5cCIapByRLlVhZdF4X3uw==&X-Bogus=DFSzswVL8jPxukGEtv8d3hJ92U17&_signature=_02B4Z6wo00001wTLrjAAAIDBA2GblSlMKScEy6qAAKefb9"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "cookie": "_ttp=2jvO14T05n9h8rNWfVwxAIIp2m3; __tea_cache_tokens_3178=^{^%^22_type_^%^22:^%^22default^%^22^}; s_v_web_id=verify_lz73fls4_aoNtC6cf_MYAT_4cuf_96t6_4PDaYgU0qf4z; passport_csrf_token=df108f5491575d37f74611d16e6ad855; passport_csrf_token_default=df108f5491575d37f74611d16e6ad855; d_ticket_backstage=b6410fb81f0ec0adb42aa109a2867ee77e3a1; odin_tt=f78fa9719b466d439b9165480b517c5189ec5f4a98e3aa32e4d42ef96c7e979c4758ce7bbe0b6142f758b5e76cb94f50ddeacf454c1f2976a5067eeaaed62659; sid_guard_backstage=d26e76b0ba8e3b6e005b8b8465be05e0^%^7C1722263880^%^7C5184000^%^7CFri^%^2C+27-Sep-2024+14^%^3A38^%^3A00+GMT; uid_tt_backstage=1f7e49fa678486b455f2263a3ca004d4f06f6d84f88002758e21f3cc4d6b16ef; uid_tt_ss_backstage=1f7e49fa678486b455f2263a3ca004d4f06f6d84f88002758e21f3cc4d6b16ef; sid_tt_backstage=d26e76b0ba8e3b6e005b8b8465be05e0; sessionid_backstage=d26e76b0ba8e3b6e005b8b8465be05e0; sessionid_ss_backstage=d26e76b0ba8e3b6e005b8b8465be05e0; sid_ucp_v1_backstage=1.0.0-KGI5YzIzOWVhNzU5ZmVmOWFjMTkzNjMwM2IxZWNlMTIzMTQ3YWI0ODcKIAiBiMKG7t2xymYQyNKetQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgZDI2ZTc2YjBiYThlM2I2ZTAwNWI4Yjg0NjViZTA1ZTA; ssid_ucp_v1_backstage=1.0.0-KGI5YzIzOWVhNzU5ZmVmOWFjMTkzNjMwM2IxZWNlMTIzMTQ3YWI0ODcKIAiBiMKG7t2xymYQyNKetQYYwTUgDDCjjtO0BjgBQOsHEAMaA3NnMSIgZDI2ZTc2YjBiYThlM2I2ZTAwNWI4Yjg0NjViZTA1ZTA; passport_fe_beating_status=true; csrf_session_id=48e8ace0aebcc4b3d173e5b7a77e2b34; ttwid=1^%^7CnVeJ0nsWAMlvvg6gPtWfzvnqg1FvTtuu5uu3uqKATWU^%^7C1722264248^%^7C26c3445ec7217a50ee765f7b89eed48cd772cd0ff52a78973c5849b4a8d82e89; msToken=omFAEx1uvG_jsgkPSIqHCBJIHnfoODlCkDDER_NRJGDUWZHRKezX3-Yj9vGgvokWaVwf7BRmjg8owHWgEoCUy6zJFEa8B1Ng4TV7qOskKFokYpb8zMTjg-beiTE6-wZHwOMxEg==; msToken=omFAEx1uvG_jsgkPSIqHCBJIHnfoODlCkDDER_NRJGDUWZHRKezX3-Yj9vGgvokWaVwf7BRmjg8owHWgEoCUy6zJFEa8B1Ng4TV7qOskKFokYpb8zMTjg-beiTE6-wZHwOMxEg==^",
    "faction-id": "103608",
    "origin": "https://live-backstage.tiktok.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://live-backstage.tiktok.com/portal/",
    "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
    "x-appid": "1180",
    "x-csrf-token": "undefined",
    "x-language": "zh-CN",
    "x-secsdk-csrf-token": "000100000001f8c9c4faf619fb5d2af61e2d44b49e44b623309d45f80e93ee70f41dab5ec3d417e6b635990f895f"
}

data = {"DisplayIDList": ["20tg01", "user1717918140309", "denden_kp", "16zozozo61", "tanariochan_", "chiaki_romance",
                          "daiyaxxx", "mieu.ngoan", "linnmeozz", "bigbang5_5n1c", "trn.thin.9436", "dongpc2405",
                          "maid_elvis", "n._r25"]}

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
json.dumps(data)
get_url = "https://live-backstage.tiktok.com/creators/live/union_platform_api/agency/quota/get_broker_remain_quota/?AgencyID=103608&OperatorID=7391751617698104321&msToken=XcR0ELo_8hIp3rnBhNN4OMCU8K5Kcx_HOJN8xAFYU551kfBm4Vusmjkn-gxYYx0gHGQxyYvN1FoXvcYOrwOgz0u8LyOhykGTWF4bYPMwLiU=&X-Bogus=DFSzswVLnUKdUvGEtv0rchJ92U6q&_signature=_02B4Z6wo00001h3p0vAAAIDAGkPnVYlZq-Id6dZAAOHr7d"
with httpx.Client(http2=True, verify=False, ) as client:
    # , cookies = cookies
    response = client.post(url, headers=headers, json=data)
    #print(response.json())
    print(response.text)
