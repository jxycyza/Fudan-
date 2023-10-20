from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usrname = ''
password = ''

driver = webdriver.Edge()
driver.implicitly_wait(10)  # Implicit wait for 10 seconds

url = "http://ce.fudan.edu.cn"
driver.get(url)

usr = driver.find_element(By.ID, 'username')
pwd = driver.find_element(By.ID, 'password')
submit = driver.find_element(By.ID, 'idcheckloginbtn')

usr.send_keys(usrname)
pwd.send_keys(password)
submit.click()

while 1:
    driver.get("http://ce.fudan.edu.cn/")
    driver.find_element(By.CLASS_NAME, 'evaluateMyTask').click()
    time.sleep(1)
    driver.switch_to.frame("iframepage")

    # Using WebDriverWait to ensure the element is clickable before interaction
    a = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tblQuestion > tbody > tr:nth-child(1) > td.operate > a.mcopen')))
    a.click()
    
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])

    radios = driver.find_elements(By.CLASS_NAME, 'jqTransformRadioWrapper')
    checkboxes = driver.find_elements(By.CLASS_NAME, 'jqTransformCheckboxWrapper')
    cnt = 0

    # 先选择其他单选按钮
    for i in reversed(radios):  # 排除最后一个单选按钮
        if i.is_displayed():
            i.click()

    # 然后选择 "仅提供了参考资料（书目、教学视频等）"
    specific_option_label = driver.find_element(By.XPATH, "//label[contains(text(), '仅提供了参考资料（书目、教学视频等）')]")
    specific_option_label.click()

    label_element = driver.find_element(By.XPATH, "//label[contains(text(), '1. 总体评价')]")
    label_element.click()


    for i in checkboxes:
        if i.is_displayed():
            cnt += 1
            i.click()
        if cnt >= 8: break

    text = driver.find_elements(By.TAG_NAME, 'textarea')
    for i in text:
        i.send_keys('好')

    # Using JavaScript to click the 'next_button' element
    next_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'next_button')))
    driver.execute_script("arguments[0].click();", next_button)

    buttons = driver.find_elements(By.TAG_NAME, 'button')
    for i in buttons:
        if i.get_attribute('data-id') == 'ok':
            # Using JavaScript to click the button with data-id 'ok'
            driver.execute_script("arguments[0].click();", i)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'evaluateMyTask')))  # Assuming evaluateMyTask button will appear again
