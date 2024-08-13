from DrissionPage import WebPage
from DrissionPage.common import Keys
import conn
import json

loginUrl = "https://live-backstage.tiktok.com/"
mainUrl = "https://live-backstage.tiktok.com/portal/"

account1 = "sugoivip@126.com"
password1 = "sugoi88//"

count_flag = 0


def get_login_page(current_url):
    """
    判断是否为登录界面或者直接为主页，当为登录界面时，登录账号，当为主页面时则调取主播查询
    :return:
    """
    if current_url == loginUrl:
        return 0
    if current_url == mainUrl:
        return 1
    else:
        return 0


def login_page():
    login_button = driver.ele("xpath://button/span/strong[text()='登录']")
    # 点击登录按钮
    login_button.click()
    driver.ele("#email").input(account1)
    driver.ele("#password").input(password1)
    login_buttons = driver.ele("xpath://button/span[text()='登录']")
    login_buttons.click()
    driver.wait.load_start()


def invite_anchor():
    invite_anchor_button = driver.ele("xpath://button/span/span[2][text()='邀请主播']")
    invite_anchor_button.click()
    textarea = driver.ele(".semi-input-textarea semi-input-textarea-autosize")
    textarea.click()
    set_anchor_in_textarea(textarea)


def set_anchor_in_textarea(textarea):
    anchor_list = get_anchor_list()
    anchor_lists = []
    if anchor_list is not None:
        for row in anchor_list:
            anchor_lists.append(row[0])
    print(anchor_lists)
    list_length = len(anchor_lists)
    for index, text in enumerate(anchor_lists):
        # 如果不是最后一个元素
        if index < list_length - 1:
            textarea.input(text + '\n')
        else:
            textarea.input(text)
    driver.ele("xpath://button/span[text()='下一步']").click()
    driver.wait.load_start(3)
    get_res_json()
    global count_flag
    count_flag += 1
    print("count_flag", count_flag)
    if count_flag >= 96:
        driver.quit()
    for_each_anchor()



def get_res_json():
    res = driver.listen.wait()
    json_data = res.response.body
    print(json_data)
    json_format(json_data)


updateSql1 = "UPDATE tiktokmsg.anchor_msg SET display_id = %(DisplayID)s,is_have_mcn = %(AnchorStatus)s WHERE user_id = %(UserID)s"
updateSql2 = "UPDATE tiktokmsg.anchor_msg SET is_have_mcn = %(AnchorStatus)s WHERE display_id = %(DisplayID)s"


def json_format(json_data):
    data = json.dumps(json_data)
    data = json.loads(data)
    if "data" in data:
        for datas in data["data"]["AnchorList"]:
            AnchorStatus = datas["AnchorStatus"]
            UserID = datas["UserBaseInfo"]["UserID"]
            DisplayID = datas["UserBaseInfo"]["DisplayID"]
            updateData = {'AnchorStatus': AnchorStatus, 'UserID': UserID, 'DisplayID': DisplayID}
            if UserID == '0':
                conn.sqlUpdate(updateSql2, updateData)
            else:
                conn.sqlUpdate(updateSql1, updateData)
            print(AnchorStatus, UserID, DisplayID)


def for_each_anchor():
    """
    循环95次，每天最多查询人数为3000 人，每次最多30人，每个账号最多100次
    :return:
    """
    #在查询成功之后返回上一层
    driver.ele("xpath://div/button/span[text()='返回']").click()
    driver.wait.load_start(3)
    #清空textarea
    driver.ele(".semi-input-textarea semi-input-textarea-autosize").clear()
    textarea = driver.ele(".semi-input-textarea semi-input-textarea-autosize")
    textarea.click()
    set_anchor_in_textarea(textarea)


def get_anchor_list():
    selectSql = "SELECT display_id FROM tiktokmsg.anchor_msg where is_have_mcn is null or is_have_mcn = '' limit 30"
    return conn.sqlSelect(selectSql)


if __name__ == '__main__':
    driver = WebPage()
    driver.get('https://live-backstage.tiktok.com/portal/')  #直接登录主页
    driver.listen.start('union_invite/batch_check_anchor/')
    #等待doom 加载完成，防止在加载中进行错误的判断
    driver.wait.load_start()
    current_url = driver.url
    if get_login_page(current_url) == 0:
        login_page()
        invite_anchor()
    if get_login_page(current_url) == 1:
        invite_anchor()
