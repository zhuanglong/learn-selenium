# 爬取每日热门帖子，被风控了
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

config = {
    'min_random_time': '0.1',
    'max_random_time': '0.8',
    'page_load_wait': '0.1-0.8',
    'input_wait': '0.3-0.8',
    'submit_wait': '0.5-1.5',
    'verification_code_input': '0.1-0.3',
    'verification_success_wait': '2-3',
    'verification_retry_wait': '2-3',
    'email_check_initial_wait': '4-6',
    'email_refresh_wait': '2-4',
    'settings_page_load_wait': '1-2',
    'failed_retry_time': '0.5-1',
    'retry_interval': '8-12',
    'max_timeout': '160'
}

def get_random_wait_time():
    return random.uniform(0.1, 0.8)

def scroll_to_bottom(driver):
    print('\n正在滚动到页面底部...')
    time.sleep(get_random_wait_time())
    
    # 获取页面高度
    scroll_height = driver.execute_script('return document.body.scrollHeight')
    current_position = 0
    scroll_step = 500  # 每次滚动的像素
    
    while current_position < scroll_height:
        # 使用 ActionChains 模拟鼠标滚轮
        actions = ActionChains(driver)
        actions.scroll_by_amount(0, scroll_step).perform()
        current_position += scroll_step
        
        # 随机等待一小段时间，模拟人类操作
        time.sleep(get_random_wait_time())
    
    print('\n已滚动到页面底部')

def simulate_human_input(driver):
    print('\n正在打开页面...')
    driver.get('about:blank')
    time.sleep(get_random_wait_time())
    driver.get('https://linux.do/top?period=daily')
    time.sleep(get_random_wait_time())
    print('\n页面打开成功')

def get_posts(driver):
    print('\n正在获取帖子...')
    # 等待加载动画消失
    # wait = WebDriverWait(driver, 5)  # 最多等待5秒
    # wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'preloader-image')))
    
    # 加载动画消失后再获取帖子
    # posts = driver.find_elements(By.CSS_SELECTOR, '.topic-list .topic-list-item:not(.category-feedback)')
    # for index, post_ele in enumerate(posts):
    #     link_ele = post_ele.find_element(By.CSS_SELECTOR, '.raw-link')
    #     title = link_ele.find_element(By.TAG_NAME, 'span').text
    #     href = link_ele.get_attribute('href')

    #     # 获取作者ID
    #     poster_id = post_ele.find_element(By.CSS_SELECTOR, '.posters a.latest').get_attribute('data-user-card')

    #     # 获取作者头像
    #     poster_avatar = post_ele.find_element(By.CSS_SELECTOR, '.posters .avatar').get_attribute('src')

    #     # 获取阅读数
    #     views_number = post_ele.find_element(By.CSS_SELECTOR, '.views .number').get_attribute('textContent')

    #     # 获取分类
    #     category = post_ele.find_element(By.CSS_SELECTOR, '.badge-category__name').text

    #     # 获取标签
    #     try:
    #         tags = post_ele.find_element(By.CSS_SELECTOR, '.discourse-tags').text
    #     except:
    #         tags = ''

    #     datetime = post_ele.find_element(By.CSS_SELECTOR, '.activity').get_attribute('title').split('\n')[0][5:]
    #     date = datetime[:-5].replace(' ', '')
    #     time = datetime[-5:]

    #     print(f'{index + 1}: ', {
    #         'title': title,
    #         'href': href,
    #         'category': category,
    #         'tags': tags,
    #         'datetime': date + ' ' + time,
    #         'views_number': views_number,
    #         'poster_id': poster_id,
    #         'poster_avatar': poster_avatar
    #     })
    
    scroll_to_bottom(driver)

def setup_driver():
    options = webdriver.ChromeOptions()
    # 保持打开
    options.add_experimental_option('detach', True)
    # 禁用自动化提示
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 无痕模式
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    # 去掉 webdriver 检测
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': """
            delete navigator.webdriver;
        """
    })
    
    simulate_human_input(driver)
    # get_posts(driver)

if __name__ == "__main__":
    setup_driver()