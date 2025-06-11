# 填写 cursor 注册表单
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker

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

def get_random_wait_time(timing_type='page_load_wait'):
    try:  
        if timing_type == 'random':
            min_time = float(config.get('min_random_time', fallback='0.1'))
            max_time = float(config.get('max_random_time', fallback='0.8'))
            return random.uniform(min_time, max_time)
            
        time_value = config.get(timing_type, fallback='0.1-0.8')
        
        # Check if it's a fixed time value
        if '-' not in time_value and ',' not in time_value:
            return float(time_value)  # Return fixed time
            
        # Process range time
        min_time, max_time = map(float, time_value.split('-' if '-' in time_value else ','))
        return random.uniform(min_time, max_time)
    except:
        return random.uniform(0.1, 0.8)  # Return default value when error

def simulate_human_input(driver):
    print('\n🚀 正在打开注册页面...')
    driver.get('about:blank')
    time.sleep(get_random_wait_time('page_load_wait'))
    driver.get('https://authenticator.cursor.sh/sign-up')
    time.sleep(get_random_wait_time('page_load_wait'))

def fill_signup_form(driver):
    print('\n正在填写注册表单...')
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = '2766428466@qq.com'
    
    driver.find_element(By.NAME, 'first_name').send_keys(first_name)
    time.sleep(get_random_wait_time('input_wait'))
    driver.find_element(By.NAME, 'last_name').send_keys(last_name)
    time.sleep(get_random_wait_time('input_wait'))
    driver.find_element(By.NAME, 'email').send_keys(email)
    time.sleep(get_random_wait_time('input_wait'))
    driver.find_element(By.CSS_SELECTOR, 'button[value="sign-up"]').click()
    time.sleep(get_random_wait_time('submit_wait'))
    print('\n✅ 填写注册表单成功')

def setup_driver():
    options = webdriver.ChromeOptions()
    # 保持打开
    options.add_experimental_option('detach', True)
    # 禁用自动化提示
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('useAutomationExtension', False)
    # 无痕模式
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    
    simulate_human_input(driver)
    fill_signup_form(driver)

if __name__ == "__main__":
    setup_driver()