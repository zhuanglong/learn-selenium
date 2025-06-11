# 基础元素查询和交互
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from urllib.parse import urlparse, parse_qs

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
assert title == "Web form"

driver.implicitly_wait(0.5)

driver.find_element(by=By.NAME, value="my-text").send_keys("Selenium")
driver.find_element(by=By.NAME, value="my-password").send_keys("Selenium123123")
Select(driver.find_element(by=By.NAME, value="my-select")).select_by_value("2")
driver.find_element(by=By.NAME, value="my-datalist").send_keys("New York")
driver.find_element(by=By.ID, value="my-check-2").click()
driver.find_element(by=By.ID, value="my-radio-2").click()
driver.find_element(by=By.NAME, value="my-colors").send_keys("#c74343")
driver.find_element(by=By.NAME, value="my-date").send_keys("08/12/2025")
driver.execute_script("document.getElementsByName('my-range')[0].value = '10'")

driver.find_element(by=By.CSS_SELECTOR, value="button").click()
message_text = driver.find_element(by=By.ID, value="message").text
assert message_text == "Received!"

parsed_url = urlparse(driver.current_url)
query_params = parse_qs(parsed_url.query)
# 获取特定参数
query_params.get('my-password', [''])[0]
print(f"URL参数: {query_params}")

driver.quit()


