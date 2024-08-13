import base64
import time

import ddddocr
from PIL import Image
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conn

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # 指定使用基于Chromium的Edge浏览器
# edge_options.add_argument("headless")  # 无界面模式
edge_options.add_argument("disable-gpu")  # 禁用GPU加速
# edge_options.add_argument("window-size=1200x600")  # 设置窗口大小
edge_options.add_experimental_option('detach', True)
# edge_options.add_argument("--headless")
# ... 其他配置 ...

account1 = "sugoivip@126.com"
password1 = "sugoi88//"

# 创建WebDriver对象
edge_driver = webdriver.Edge(options=edge_options)

edge_driver.get('https://live-backstage.tiktok.com/portal/')
# 创建ActionChains对象
actions = ActionChains(edge_driver)

try:
    element = WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "semi-button"))
    )
    # 一旦元素可见，就可以进行后续操作了
    print("元素已可见，可以执行后续操作了")
except Exception as e:
    print("等待超时或发生错误:", e)

button = edge_driver.find_element(By.XPATH, "//button/span/strong[text()='登录']")
# 将鼠标移动到元素上
actions.move_to_element(button).click(button).perform()


# 定位到用户名输入框并输入用户名
username_input = edge_driver.find_element(By.ID, "email")
actions.move_to_element(username_input).click(username_input).perform()
username_input.send_keys(account1)

# 定位到密码输入框并输入密码
password_input = edge_driver.find_element(By.ID, "password")
actions.move_to_element(password_input).click(password_input).perform()
password_input.send_keys(password1)
# 定位到登录按钮并点击

login_button = edge_driver.find_element(By.XPATH, "//button/span[text()='登录']")
actions.move_to_element(login_button).click(password_input).perform()
actions.click(login_button).perform()

try:
    element = WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "semi-popover"))
    )
    # 一旦元素可见，就可以进行后续操作了
    print("元素已可见，可以执行后续操作了")
except Exception as e:
    print("等待超时或发生错误:", e)
time.sleep(1)
edge_driver.switch_to.active_element.send_keys(Keys.ESCAPE)

# 添加主播
add_anhor = edge_driver.find_element(By.XPATH, "//button/span/span[2][text()='邀请主播']")
actions.move_to_element(add_anhor).click(add_anhor).perform()


def bot_cert():
    # 获取验证码图片背景大图
    captcha = edge_driver.find_element(By.CLASS_NAME, 'sc-jzJRlG')
    captcha_img = captcha.get_attribute('src')
    captcha_size = (captcha.size['width'], captcha.size['height'])
    handle_img(captcha_img, 'bg', captcha_size, 'bg_sized')
    # 获取滑块小图
    wrap = edge_driver.find_element(By.CLASS_NAME, 'sc-kAzzGY')
    wrap_img = wrap.get_attribute('src')
    wrap_size = (wrap.size['width'], wrap.size['height'])
    handle_img(wrap_img, 'sm', wrap_size, 'sm_sized')
    get_distance(captcha_img, wrap_img)


try:
    element = WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "semi-input-textarea"))
    )
    # 一旦元素可见，就可以进行后续操作了
    print("元素已可见，可以执行后续操作了")
except Exception as e:
    print("等待超时或发生错误:", e)


def get_anchor():
    textarea = edge_driver.find_element(By.CLASS_NAME, "semi-input-textarea")
    edge_driver.execute_script("arguments[0].focus();", textarea)
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
            textarea.send_keys(text + Keys.RETURN)
        else:
            textarea.send_keys(text)


def get_anchor_list():
    selectSql = "SELECT display_id FROM tiktokmsg.anchor_msg where is_have_mcn != '0' OR is_have_mcn IS NULL limit 30"
    return conn.sqlSelect(selectSql)


get_anchor()
next_step = edge_driver.find_element(By.XPATH, "//button/span[text()='下一步']")
actions.move_to_element(next_step).click(next_step).perform()


try:
    element = WebDriverWait(edge_driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "captcha_verify_container"))
    )
    #bot_cert()
    # 一旦元素可见，就可以进行后续操作了
    print("需要进行人机验证")
except NoSuchElementException:
    #get_anchor()
    print("不需要人机验证")





def handle_img(img_src: str, name: str, size: tuple, name_sized: str):
    """
    对下载的验证码图片进行处理
    :param img_src: 原图片编码
    :param name: 保存名称
    :param size: 调整的大小，元组(width, height)
    :param name_sized: 调整后的图片名
    :return: 无
    """
    s_img = img_src.replace('data:image/png;base64,', '')
    img_byte = base64.b64decode(s_img)
    with open(f"../images/{name}.png", "wb") as f:
        f.write(img_byte)
    img = Image.open(f"../images/{name}.png")
    res_img = img.resize(size)
    res_img.save(f"../images/{name_sized}.png")


def get_distance(tg_img, bg_img):
    """
    获取滑动距离
    :param bg_img: 底层大图片
    :param tg_img: 滑块小图片
    :return: 返回距离
    """
    # 读取图片
    with open(f"../images/{tg_img}.png", "rb") as f:
        tg = f.read()
    with open(f"../images/{bg_img}.png", "rb") as f:
        bg = f.read()

    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    # 目标图无多余背景，需要加入simple_target参数
    res = det.slide_match(tg, bg, simple_target=True)
    return res['target'][0]




