import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # 指定使用基于Chromium的Edge浏览器
# edge_options.add_argument("headless")  # 无界面模式
# edge_options.add_argument("disable-gpu")  # 禁用GPU加速
# edge_options.add_argument("window-size=1200x600")  # 设置窗口大小
edge_options.add_experimental_option('detach', True)
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
#button.click()
# 将鼠标移动到元素上
actions.move_to_element(button).perform()
# 在移动后的位置点击元素
actions.click(button).perform()

# 定位到用户名输入框并输入用户名
username_input = edge_driver.find_element(By.ID, "email")
username_input.send_keys(account1)  # 请替换为你的用户名

# 定位到密码输入框并输入密码
password_input = edge_driver.find_element(By.ID, "password")
password_input.send_keys(password1)  # 请替换为你的密码
# 定位到登录按钮并点击

login_button = edge_driver.find_element(By.XPATH, "//button/span[text()='登录']")
login_button.click()

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
add_anhor = edge_driver.find_element(By.XPATH, "//button/span/span[2][text()='添加主播']")
add_anhor.click()


# enterHostArea-VlrwXO