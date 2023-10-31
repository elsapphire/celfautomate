import time

import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import ElementClickInterceptedException

pd = pandas.read_csv('Log In KC - Sheet1.csv')
emails = pd.to_dict()['email']
passwords = pd.to_dict()['password']
kc = pd.to_dict()['kc']

login_dict = {}
for i in range(len(emails)):
    login_dict[i] = {
        'email': emails[i],
        'password': passwords[i],
        'kc': kc[i]
    }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://celfonline.org/V3/index.php?r=Site/Login')

for n in range(len(login_dict)):
    print(f'Working on {login_dict[n]["email"]}')
    # log in
    email = driver.find_element(By.NAME, 'username')
    email.send_keys(login_dict[n]['email'])

    password = driver.find_element(By.NAME, 'password')
    password.send_keys(login_dict[n]['password'])
    password.send_keys(Keys.ENTER)

    sync = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div/strong/a')
    sync.click()

    kc_username = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/section/div[2]/input')
    kc_username.click()
    kc_username.send_keys(login_dict[n]['kc'])

    password = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/section/div[3]/div/input')
    password.send_keys('Zonalchurch22')

    log_in = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/section/div[4]/div/button')
    log_in.click()

    try:
        time.sleep(7)
        log_out = driver.find_element(By.LINK_TEXT, 'LOGOUT')
        log_out.click()
    except NoSuchElementException:
        log_out = driver.find_element(By.LINK_TEXT, 'Log out')
        log_out.click()
driver.quit()
